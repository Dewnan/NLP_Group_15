# Fake News Detection using NLP

**CCS3356 – Natural Language Processing (NLP)**

-------------------------------------------------------------------------------------------------------

# Branch Information

**Repository:** NLP_Group_15

**Branch:** feature/CIT-24-01-0185-model

**Member:** K. Sahan Wishvapriya

**Student ID:** CIT-24-01-0185

---

# Project Overview

This branch contains my individual implementation of the assigned Machine Learning and Deep Learning models for the Fake News Detection project.

The project applies Natural Language Processing (NLP) techniques to classify news articles as **Fake** or **True** using a publicly available dataset.

---

# Individual Contribution

## Machine Learning Model

- Random Forest

## Deep Learning Model

- Gated Recurrent Unit (GRU)

---

# Notebook Structure

**Notebook**

- `notebooks/sahan_random_forest.ipynb`

### Sections Included

1. Import Required Libraries
2. Dataset Collection
3. Dataset Exploration
4. Dataset Merging and Labeling
5. Text Preprocessing
6. Exploratory Data Analysis (EDA)
7. TF-IDF Feature Extraction
8. Train-Test Split
9. Random Forest Model
10. Random Forest Evaluation
11. GRU Model
12. GRU Training
13. GRU Evaluation
14. Model Comparison

---

# NLP Pipeline

The notebook performs the following tasks:

- Load Fake.csv and True.csv
- Merge datasets
- Assign labels
- Convert text to lowercase
- Remove punctuation
- Remove numbers
- Remove stop words
- Lemmatization
- Create `Clean_Text`
- Exploratory Data Analysis (EDA)
- TF-IDF Feature Extraction
- Train-Test Split
- Train Random Forest Model
- Evaluate Random Forest
- Build and Train GRU Model
- Evaluate GRU
- Compare both models

---

# Folder Structure

```text
NLP_Group_15/
│
├── data/
│   ├── Fake.csv
│   └── True.csv
│
├── models/
├── notebooks/
│   └── sahan_random_forest.ipynb
│
├── reports/
├── screenshots/
├── src/
├── videos/
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- TensorFlow / Keras
- Matplotlib
- Jupyter Notebook
- Git
- GitHub

---

# Dataset

### Dataset Name

Fake and Real News Dataset

### Source

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

### Files Used

- Fake.csv
- True.csv

---

# Requirements

- Python 3.x
- VS Code
- Jupyter Notebook Extension
- Git

---

# Clone Repository

```bash
git clone https://github.com/Dewnan/NLP_Group_15.git
```

Move into the project folder:

```bash
cd NLP_Group_15
```

---

# Switch to My Branch

```bash
git checkout feature/CIT-24-01-0185-model
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Notebook

1. Open the project in VS Code.
2. Select the Python interpreter.
3. Open `notebooks/sahan_random_forest.ipynb`.
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
- TF-IDF Features
- Random Forest Model
- GRU Model
- Classification Reports
- Confusion Matrices
- Model Comparison Results

---

# Result Summary

| Model | Accuracy |
|--------|----------|
| Random Forest | 99.69% |
| GRU | *(Add your final GRU accuracy here)* |

---

# Author

**Sahan Wishvapriya**

Student ID: **CIT-24-01-0185**

Branch: **feature/CIT-24-01-0185-model**

Sri Lanka Technology Campus

**CCS3356 – Natural Language Processing**