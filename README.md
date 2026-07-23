# Fake News Detection using Natural Language Processing (NLP)

## Module

**CCS3356 – Natural Language Processing**

## Project Type

Group Assignment

## Group Name

NLP_Group_15

---

# Project Overview

This project develops a Fake News Detection system using Natural Language Processing (NLP) techniques. The system classifies news articles as either **Fake** or **Real** by applying text preprocessing, feature engineering, machine learning, and deep learning models.

The project follows the complete NLP pipeline, including data preprocessing, exploratory data analysis (EDA), feature extraction, model development, evaluation, and comparison.

---

# Problem Statement

The rapid spread of fake news through online platforms can mislead the public and create misinformation. This project aims to build an automated Fake News Detection system capable of classifying news articles accurately using NLP techniques.

---

# Dataset

**Dataset Name**

Fake and Real News Dataset

**Source**

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Files used:

- Fake.csv
- True.csv

---

# Group Members

| Member | Student ID | Name | ML Model | DL Model |
|---------|------------|------|----------|----------|
| Member 1 | CIT-24-01-0258 | Pesara | Support Vector Machine (SVM) | Long Short-Term Memory (LSTM) |
| Member 2 | CIT-24-01-0185 | Sahan | Random Forest | GRU |
| Member 3 | CIT-24-01-0020 | Dewnan | Logistic Regression | CNN |

---

# Project Structure

```
project-root/

│

├── data/

├── notebooks/

├── src/

├── models/

├── reports/

├── screenshots/

├── videos/

├── requirements.txt

├── README.md

└── .gitignore
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- TensorFlow / Keras
- Jupyter Notebook
- Git
- GitHub

---

# NLP Pipeline

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. TF-IDF Feature Engineering
5. Machine Learning Model (SVM)
6. Deep Learning Model (LSTM)
7. Model Evaluation
8. Model Comparison

---

# Individual Models

## Member 1

Machine Learning

- Support Vector Machine (SVM)

Deep Learning

- Long Short-Term Memory (LSTM)

## Member 2

Machine Learning

- Random Forest

Deep Learning

- GRU

## Member 3

Machine Learning

- Logistic Regression

Deep Learning

- CNN

---

# Evaluation Metrics

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# Setup Instructions

Clone the repository:

```bash
git clone https://github.com/Dewnan/NLP_Group_15.git
```

Open the project folder.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the notebooks in the following order:

1. 01_Dataset_Preprocessing.ipynb

2. 02_EDA.ipynb

3. 03_TFIDF_Feature_Engineering.ipynb

4. 04_SVM_Model.ipynb

5. 05_LSTM_Model.ipynb

6. 06_Model_Comparison.ipynb

Running the notebooks in this order ensures that all required datasets, models, and intermediate files are generated automatically.

---

# Results Summary

The project compares six different machine learning and deep learning models developed by the three group members.

The best-performing model will be selected based on:

- Accuracy
- Precision
- Recall
- F1 Score

The selected model will be integrated into the final application.

---

# Repository

https://github.com/Dewnan/NLP_Group_15

---

# License

This repository was developed for academic purposes as part of the CCS3356 Natural Language Processing module at Sri Lanka Technology Campus.