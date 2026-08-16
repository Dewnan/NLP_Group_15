import os
import sys
import pickle
import numpy as np
import pandas as pd

# Add parent directory to sys.path to import src.preprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocess import normalize_text, tokenize_and_lemmatize

# Path references
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MODELS_DIR = os.path.join(BASE_DIR, 'models')

MODEL_CONFIGS = {
    "CNN (Best Overall DL)": {
        "dir": os.path.join(MODELS_DIR, "CNN"),
        "model_file": "cnn_model.keras",
        "tokenizer_file": "cnn_tokenizer.pkl",
        "type": "keras"
    },
    "Logistic Regression (Best ML)": {
        "dir": os.path.join(MODELS_DIR, "LogReg"),
        "model_file": "logreg_model.pkl",
        "vectorizer_file": "tfidf_vectorizer.pkl",
        "type": "sklearn"
    },
    "SVM": {
        "dir": os.path.join(MODELS_DIR, "SVM"),
        "model_file": "svm_model.pkl",
        "vectorizer_file": "tfidf_vectorizer.pkl",
        "type": "sklearn"
    },
    "Random Forest": {
        "dir": os.path.join(MODELS_DIR, "RandomForest"),
        "model_file": "random_forest_model.pkl",
        "vectorizer_file": "tfidf_vectorizer.pkl",
        "type": "sklearn"
    },
    "GRU": {
        "dir": os.path.join(MODELS_DIR, "GRU"),
        "model_file": "gru_model.keras",
        "tokenizer_file": "gru_tokenizer.pkl",
        "type": "keras"
    },
    "LSTM": {
        "dir": os.path.join(MODELS_DIR, "LSTM"),
        "model_file": "lstm_model.keras",
        "tokenizer_file": "lstm_tokenizer.pkl",
        "type": "keras"
    }
}

_CACHE = {}

def preprocess_news_text(title: str, text: str) -> tuple:
    """Combines title and text, normalizes and lemmatizes."""
    raw_content = (str(title).strip() + ' ' + str(text).strip()).strip()
    normalized = normalize_text(raw_content)
    cleaned = tokenize_and_lemmatize(normalized)
    return normalized, cleaned

def load_model_assets(model_key: str):
    """Loads and caches model assets."""
    if model_key in _CACHE:
        return _CACHE[model_key]

    config = MODEL_CONFIGS[model_key]
    model_type = config["type"]

    assets = {"config": config}

    if model_type == "sklearn":
        import joblib
        model_path = os.path.join(config["dir"], config["model_file"])
        vec_path = os.path.join(config["dir"], config["vectorizer_file"])
        
        assets["model"] = joblib.load(model_path)
        assets["vectorizer"] = joblib.load(vec_path)

    elif model_type == "keras":
        import tensorflow as tf
        model_path = os.path.join(config["dir"], config["model_file"])
        tok_path = os.path.join(config["dir"], config["tokenizer_file"])

        assets["model"] = tf.keras.models.load_model(model_path)
        with open(tok_path, 'rb') as f:
            assets["tokenizer"] = pickle.load(f)

    _CACHE[model_key] = assets
    return assets

def predict_news(title: str, text: str, model_key: str) -> dict:
    """Executes model inference and returns prediction result."""
    normalized_text, cleaned_text = preprocess_news_text(title, text)
    if not cleaned_text.strip():
        return {
            "error": "The input text is empty after preprocessing. Please provide valid text content."
        }

    assets = load_model_assets(model_key)
    config = assets["config"]
    model_type = config["type"]

    if model_type == "sklearn":
        vectorizer = assets["vectorizer"]
        model = assets["model"]

        vec_input = vectorizer.transform([cleaned_text])
        prediction = model.predict(vec_input)[0]

        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(vec_input)[0]
            fake_prob, real_prob = float(probs[0]), float(probs[1])
        elif hasattr(model, "decision_function"):
            decision = model.decision_function(vec_input)[0]
            real_prob = float(1 / (1 + np.exp(-decision)))
            fake_prob = float(1.0 - real_prob)
        else:
            real_prob = float(prediction)
            fake_prob = float(1.0 - real_prob)

    elif model_type == "keras":
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        tokenizer = assets["tokenizer"]
        model = assets["model"]

        max_len = getattr(model, 'input_shape', [None, 300])[1] or 300
        sequences = tokenizer.texts_to_sequences([cleaned_text])
        padded = pad_sequences(sequences, maxlen=max_len, padding='post', truncating='post')

        prob = float(model.predict(padded, verbose=0)[0][0])
        
        # Determine sigmoid vs 2-class output shape
        if hasattr(model, 'output_shape') and model.output_shape[-1] == 2:
            probs = model.predict(padded, verbose=0)[0]
            fake_prob, real_prob = float(probs[0]), float(probs[1])
            prediction = 1 if real_prob >= 0.5 else 0
        else:
            real_prob = prob
            fake_prob = 1.0 - prob
            prediction = 1 if real_prob >= 0.5 else 0

    label = "Real News" if prediction == 1 else "Fake News"
    confidence = real_prob if prediction == 1 else fake_prob

    return {
        "label": label,
        "prediction": int(prediction),
        "confidence": confidence,
        "real_probability": real_prob,
        "fake_probability": fake_prob,
        "model_name": model_key,
        "cleaned_text": cleaned_text
    }
