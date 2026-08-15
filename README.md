# Fake News Detection using Natural Language Processing

## Project Title

**Fake News Detection using Machine Learning and Deep Learning Techniques**

---

## Course Information

**CCS3356 – Natural Language Processing (NLP)**

---

## Repository Information

**Repository:** `NLP_Group_15`

---

## Group Members

| Member   | Student ID     | Name              | Machine Learning Model       | Deep Learning Model                |
| -------- | -------------- | ----------------- | ---------------------------- | ---------------------------------- |
| Member 1 | CIT-24-01-0258 | Pesara            | Support Vector Machine (SVM) | Long Short-Term Memory (LSTM)      |
| Member 2 | CIT-24-01-0185 | Sahan Wishvapriya | Random Forest                | Gated Recurrent Unit (GRU)         |
| Member 3 | CIT-24-01-0020 | Dewnan            | Logistic Regression          | Convolutional Neural Network (CNN) |

---

## Project Overview

The rapid spread of misinformation through online news platforms and social media has become a significant challenge in today's digital world. Fake news can influence public opinion, create confusion, and negatively impact decision-making processes.

This project aims to develop an automated **Fake News Detection system** using Natural Language Processing (NLP), Machine Learning (ML), and Deep Learning (DL) techniques.

The system analyzes the textual content of news articles and classifies them as either **Fake News** or **Real News**.

Each group member independently implements and evaluates one Machine Learning model and one Deep Learning model using the same dataset. The performance of all models will then be compared, and the best-performing model can be selected for the final application.

---

## Dataset Information

### Dataset Name

**Fake and Real News Dataset**

### Dataset Source

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

### Dataset Files

* `Fake.csv`
* `True.csv`

### Dataset Description

The dataset contains news articles labeled as:

* Fake News
* Real News

The dataset includes:

* News titles
* News article content
* Subject categories
* Publication dates

---

# Individual Contributions

## Member 1 – Pesara

**Student ID:** `CIT-24-01-0258`

**Branch:** `feature/CIT-24-01-0258-model`

### Machine Learning Model

**Support Vector Machine (SVM)**

### Deep Learning Model

**Long Short-Term Memory (LSTM)**

### Individual NLP Pipeline

Pesara's implementation consists of the following stages:

1. Dataset Collection & Preprocessing
2. Exploratory Data Analysis (EDA)
3. TF-IDF Feature Engineering
4. Support Vector Machine (SVM)
5. Long Short-Term Memory (LSTM)
6. Model Comparison

### Notebooks

```text
01_Dataset_Preprocessing.ipynb
02_EDA.ipynb
03_TFIDF_Feature_Engineering.ipynb
04_SVM_Model.ipynb
05_LSTM_Model.ipynb
06_Model_Comparison.ipynb
```

### Results

| Model | Accuracy | Precision |   Recall | F1 Score |
| ----- | -------: | --------: | -------: | -------: |
| SVM   | 0.994965 |  0.996217 | 0.993164 | 0.994688 |
| LSTM  | 0.983889 |  0.978738 | 0.987506 | 0.983103 |

---

## Member 2 – Sahan Wishvapriya

**Student ID:** `CIT-24-01-0185`

**Branch:** `feature/CIT-24-01-0185-model`

### Machine Learning Model

**Random Forest**

### Deep Learning Model

**Gated Recurrent Unit (GRU)**

### Individual NLP Pipeline

Sahan's implementation consists of:

1. Import Required Libraries
2. Dataset Collection
3. Dataset Exploration
4. Dataset Merging and Labeling
5. Text Cleaning
6. Save Cleaned Dataset
7. Text Preprocessing
8. Exploratory Data Analysis (EDA)
9. Train-Test Split
10. TF-IDF Feature Extraction
11. Random Forest Model
12. Random Forest Evaluation
13. GRU Model
14. GRU Training
15. GRU Evaluation
16. Model Comparison

### Notebook

```text
notebooks/fake_news_detection_random_forest_gru.ipynb
```

### Results

| Model         | Accuracy | Precision |   Recall | F1 Score |
| ------------- | -------: | --------: | -------: | -------: |
| Random Forest | 0.996437 |  0.996485 | 0.996019 | 0.996252 |
| GRU           | 0.988976 |  0.986017 | 0.990867 | 0.988436 |

---

## Member 3 – Dewnan

**Student ID:** `CIT-24-01-0020`

### Machine Learning Model

**Logistic Regression**

### Deep Learning Model

**Convolutional Neural Network (CNN)**

Dewnan's assigned models are implemented as part of the group's individual model comparison using the common Fake and Real News Dataset.

---

# NLP Pipeline

The overall project follows the following NLP pipeline:

1. Data Collection
2. Data Cleaning
3. Text Preprocessing

   * Lowercasing
   * Tokenization
   * Stop-word Removal
   * Lemmatization
4. Exploratory Data Analysis (EDA)
5. Feature Engineering

   * TF-IDF
   * Word Embeddings
6. Model Training
7. Model Evaluation
8. Model Comparison
9. Final Application Integration
10. Ethics and Bias Analysis

---

# Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* TensorFlow / Keras
* Matplotlib
* Joblib
* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# Project Folder Structure

```text
NLP_Group_15/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── Fake.csv
│   └── True.csv
│
├── models/
│
├── notebooks/
│
├── reports/
│
├── screenshots/
│
├── src/
│
├── videos/
│
├── requirements.txt
└── README.md
```

---

# Requirements

* Python 3.x
* Visual Studio Code
* Jupyter Notebook Extension
* Git

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/Dewnan/NLP_Group_15.git
```

Move into the project folder:

```bash
cd NLP_Group_15
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Dataset Setup

Download the **Fake and Real News Dataset** and place the required CSV files in the project data directory:

```text
data/
├── Fake.csv
└── True.csv
```

---

# VS Code Setup

1. Open the project in Visual Studio Code.
2. Install the **Python** extension.
3. Install the **Jupyter** extension.
4. Open the project folder.
5. Select **Python: Select Interpreter**.
6. Select the interpreter from the `venv` virtual environment.
7. Open the required Jupyter notebook.
8. Select the same virtual environment as the notebook kernel.

---

# Running the Project

The notebooks should be executed according to the workflow implemented by each member.

### Pesara

Run the notebooks in the following order:

```text
01_Dataset_Preprocessing.ipynb
02_EDA.ipynb
03_TFIDF_Feature_Engineering.ipynb
04_SVM_Model.ipynb
05_LSTM_Model.ipynb
06_Model_Comparison.ipynb
```

Each notebook generates the required outputs for the following stage.

### Sahan

Open:

```text
notebooks/fake_news_detection_random_forest_gru.ipynb
```

Select the Jupyter kernel connected to the project virtual environment and run the notebook from beginning to end.

---

# Models Implemented

## Machine Learning

| Member | Model                        |
| ------ | ---------------------------- |
| Pesara | Support Vector Machine (SVM) |
| Sahan  | Random Forest                |
| Dewnan | Logistic Regression          |

## Deep Learning

| Member | Model                              |
| ------ | ---------------------------------- |
| Pesara | Long Short-Term Memory (LSTM)      |
| Sahan  | Gated Recurrent Unit (GRU)         |
| Dewnan | Convolutional Neural Network (CNN) |

---

# Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC where applicable

---

# Generated Outputs

The project may generate:

* Cleaned Dataset
* `Clean_Text` column
* Processed datasets
* Train-Test Split
* TF-IDF Features
* TF-IDF Vectorizer
* Trained ML Models
* Trained DL Models
* Classification Reports
* Confusion Matrices
* Model Comparison Results

---

# Results Summary

The current individual model results are:

| Member | Model               | Accuracy | Precision |   Recall | F1 Score |
| ------ | ------------------- | -------: | --------: | -------: | -------: |
| Pesara | SVM                 | 0.994965 |  0.996217 | 0.993164 | 0.994688 |
| Pesara | LSTM                | 0.983889 |  0.978738 | 0.987506 | 0.983103 |
| Sahan  | Random Forest       | 0.996437 |  0.996485 | 0.996019 | 0.996252 |
| Sahan  | GRU                 | 0.988976 |  0.986017 | 0.990867 | 0.988436 |
| Dewnan | Logistic Regression |      TBD |       TBD |      TBD |      TBD |
| Dewnan | CNN                 |      TBD |       TBD |      TBD |      TBD |

The final comparison will be updated after all group members complete their model implementations and evaluations.

---

# Final Model Selection

After all six models have been evaluated, their performance will be compared using the selected evaluation metrics.

The best-performing model will be considered for integration into the final Fake News Detection application.

---

# Ethics and Bias Analysis

The project will also consider potential ethical issues and biases in automated fake news classification, including:

* Dataset bias
* Incorrect classification
* False positives
* False negatives
* Limitations of automated news classification
* Responsible use of model predictions

---

# Authors

### Pesara

Student ID: `CIT-24-01-0258`

Model: SVM + LSTM

### Sahan Wishvapriya

Student ID: `CIT-24-01-0185`

Branch: `feature/CIT-24-01-0185-model`

Model: Random Forest + GRU

### Dewnan

Student ID: `CIT-24-01-0020`

Model: Logistic Regression + CNN

---

**Sri Lanka Technology Campus**

**CCS3356 – Natural Language Processing (NLP)**
