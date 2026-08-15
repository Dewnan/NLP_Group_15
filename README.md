# Fake News Detection using Natural Language Processing

## Project Title

Fake News Detection using Machine Learning and Deep Learning Techniques

---

## Group Members

| Member   | Student ID | Name   | ML Model                     | DL Model                           |
| -------- | ---------- | ------ | ---------------------------- | ---------------------------------- |
| Member 1 | 0258       | Pesara | Support Vector Machine (SVM) | Long Short-Term Memory (LSTM)      |
| Member 2 | 0185       | Sahan  | Random Forest                | Gated Recurrent Unit (GRU)         |
| Member 3 | 0020       | Dewnan | Logistic Regression          | Convolutional Neural Network (CNN) |

---

## Problem Statement

The rapid spread of misinformation through online news platforms and social media has become a significant challenge in today's digital world. Fake news can influence public opinion, create confusion, and negatively impact decision-making processes.

This project aims to develop an automated Fake News Detection system using Natural Language Processing (NLP), Machine Learning (ML), and Deep Learning (DL) techniques. The system will analyze the textual content of news articles and classify them as either Real News or Fake News.

Each group member will independently implement and evaluate different ML and DL models using a common dataset. The performance of all models will be compared, and the best-performing model will be integrated into the final application.

---

## Dataset Information

### Dataset Name

Fake and Real News Dataset

### Dataset Source

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

### Dataset Description

The dataset contains news articles labeled as either:

* Fake News
* Real News

The dataset includes:

* News titles
* News article content
* Subject categories
* Publication dates

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd NLP_Group_15
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 4. Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

# VS Code Setup

1. Install Visual Studio Code from https://code.visualstudio.com/
2. Install these VS Code extensions:
   - Python (by Microsoft)
   - Jupyter (by Microsoft)
3. Open the project folder in VS Code:
```bash
   code NLP_Group_15
```
4. Open the Command Palette (`Ctrl+Shift+P`) and select **Python: Select Interpreter**.
5. Choose the interpreter inside your virtual environment (`venv\Scripts\python.exe`).
6. Open `notebooks/fake_news_detection_random_forest_gru.ipynb` from the Explorer panel.
7. Click **Select Kernel** in the top-right corner of the notebook and choose the same virtual environment interpreter.

---

# Running the Notebook

1. Open the project in VS Code.
2. Select the Python interpreter (see VS Code Setup above).
3. Open `notebooks/fake_news_detection_random_forest_gru.ipynb`.
4. Select the Jupyter kernel.
5. Click **Run All** to execute all cells.

---

# Models Implemented

### Machine Learning

- Random Forest

### Deep Learning

- Gated Recurrent Unit (GRU)

---

# Output

The notebook generates:

- Cleaned Dataset
- Clean_Text Column
- Train-Test Split
- TF-IDF Features
- Random Forest Model
- GRU Model
- Classification Reports
- Confusion Matrices
- Model Comparison Results

---

# Result Summary

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Random Forest | 0.996437 | 0.996485 | 0.996019 | 0.996252 |
| GRU | 0.988976 | 0.986017 | 0.990867 | 0.988436 |

---

# Author

**Sahan Wishvapriya**

Student ID: **CIT-24-01-0185**

Branch: **feature/CIT-24-01-0185-model**

Sri Lanka Technology Campus

**CCS3356 – Natural Language Processing**
