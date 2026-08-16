import os
import sys
import streamlit as st
import pandas as pd

# Add application directory to path
sys.path.append(os.path.dirname(__file__))
from predictor import MODEL_CONFIGS, predict_news

# Page configuration
st.set_page_config(
    page_title="Fake News Detection System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for UI styling
st.markdown("""
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #dee3eb;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #dee3eb;
        margin-bottom: 1.5rem;
    }
    .result-box-real {
        background-color: #D1FAE5;
        border: 2px solid #10B981;
        border-radius: 10px;
        padding: 1rem;
        color: #065F46;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    .result-box-fake {
        background-color: #FEE2E2;
        border: 2px solid #EF4444;
        border-radius: 10px;
        padding: 1rem;
        color: #991B1B;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="main-title">Fake News Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Natural Language Processing & Deep Learning Misinformation Classifier</div>', unsafe_allow_html=True)

# Main layout split into input and results
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("Input News Content")
    news_title = st.text_input("News Title / Headline (Optional):", placeholder="e.g. Breaking: Government announces new policy...")
    news_text = st.text_area("News Body Text:", height=240, placeholder="Paste the news article content here to classify...")

    # Action row containing Model Selector dropdown and Detect button side-by-side
    act_col1, act_col2 = st.columns([2, 1])
    
    with act_col1:
        selected_model = st.selectbox(
            "Select Model:",
            options=list(MODEL_CONFIGS.keys()),
            index=0,
            label_visibility="collapsed"
        )
        
    with act_col2:
        analyze_btn = st.button("Detect Fake News", type="primary", use_container_width=True)

with col2:
    st.subheader("Prediction Results")
    if analyze_btn:
        if not news_text.strip() and not news_title.strip():
            st.warning("Please enter news content or a headline to analyze.")
        else:
            with st.spinner(f"Analyzing text with {selected_model}..."):
                result = predict_news(news_title, news_text, selected_model)

            if "error" in result:
                st.error(result["error"])
            else:
                label = result["label"]
                confidence = result["confidence"]
                fake_prob = result["fake_probability"]
                real_prob = result["real_probability"]

                if label == "Real News":
                    st.markdown('<div class="result-box-real">Prediction: REAL NEWS</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="result-box-fake">Prediction: FAKE NEWS</div>', unsafe_allow_html=True)

                st.metric(label="Model Confidence Score", value=f"{confidence * 100:.2f}%")

                st.write("**Probability Breakdown:**")
                st.write(f"Real News Probability: {real_prob * 100:.2f}%")
                st.progress(real_prob)

                st.write(f"Fake News Probability: {fake_prob * 100:.2f}%")
                st.progress(fake_prob)

                with st.expander("View Pre-processed Tokens"):
                    st.write(result["cleaned_text"])
    else:
        st.info("Enter news content on the left, select a model, and click Detect Fake News.")
