# Fake News Detection using NLP
## CCS3356 – Natural Language Processing (NLP)

### Branch Information

**Repository:** NLP_Group_15

**Branch:** `feature/CIT-24-01-0258-model`

**Member:** Pesara

**Student ID:** CIT-24-01-0258

---

# Project Overview

This branch contains the individual implementation of my assigned Machine Learning and Deep Learning models for the Fake News Detection project.

The project applies the complete Natural Language Processing (NLP) pipeline to classify news articles as **Fake** or **Real** using a publicly available dataset.

---

# Individual Contribution

### Machine Learning Model

- Support Vector Machine (SVM)

### Deep Learning Model

- Long Short-Term Memory (LSTM)

---

# NLP Pipeline

The following stages have been completed.

## Notebook 1

Dataset Collection & Preprocessing

Tasks:

- Load dataset
- Merge datasets
- Clean text
- Remove punctuation
- Remove stop words
- Lemmatization
- Save cleaned dataset

---

## Notebook 2

Exploratory Data Analysis (EDA)

Tasks:

- Class distribution
- Word frequency
- Article length analysis
- Visualizations
- Dataset insights

---

## Notebook 3

TF-IDF Feature Engineering

Tasks:

- Train/Test Split
- TF-IDF Vectorization
- Save vectorizer
- Save processed datasets

---

## Notebook 4

Support Vector Machine (SVM)

Tasks:

- Train SVM
- Generate predictions
- Evaluate model
- Save trained model

Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Notebook 5

Long Short-Term Memory (LSTM)

Tasks

- Tokenization
- Sequence Padding
- LSTM Architecture
- Model Training
- Model Evaluation
- Save trained model

Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Notebook 6

Model Comparison

Tasks

- Load saved models
- Generate predictions
- Compare SVM and LSTM
- Automatic evaluation
- Export comparison table
- Select best-performing model

---

# Folder Structure

```
data/
│
├── raw/
├── processed/
│
models/
│
notebooks/
│
reports/
│
screenshots/
│
src/
│
videos/
│
requirements.txt
README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow / Keras
- Matplotlib
- Joblib
- Jupyter Notebook

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

# Installation
# Environment Setup

## Requirements

* Python 3.x
* VS Code
* Jupyter Notebook
* Git

---

# Clone Repository

Open terminal:

```bash
git clone https://github.com/Dewnan/NLP_Group_15.git
```

Move into project folder:

```bash
cd NLP_Group_15
```

---

# Switch to Member 1 Branch

```bash
git checkout feature/CIT-24-01-0258-model
```

---

# Create Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

---

# Activate Virtual Environment

## Windows PowerShell

```bash
venv\Scripts\activate
```

After activation:

```
(venv)
```

will appear in the terminal.

Example:

```
(venv) PS D:\NLP_Group_15>
```

---

# Install Required Libraries

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Notebooks

Open the project using VS Code.

Select:

```
Python Interpreter
        ↓
venv
```

Open Jupyter notebooks.

Run:

```
Kernel
   ↓
Restart Kernel
   ↓
Run All
```

Execute notebooks from:

```
01_Dataset_Preprocessing.ipynb
```

to

```
06_Model_Comparison.ipynb
```

---



# Running the Project

Run the notebooks in the following order.

1. 01_Dataset_Preprocessing.ipynb

2. 02_EDA.ipynb

3. 03_TFIDF_Feature_Engineering.ipynb

4. 04_SVM_Model.ipynb

5. 05_LSTM_Model.ipynb

6. 06_Model_Comparison.ipynb

Each notebook generates the files required for the next notebook.

---

# Models Implemented

Machine Learning

- Support Vector Machine (SVM)

Deep Learning

- Long Short-Term Memory (LSTM)

---

# Output

The project automatically generates

- Clean dataset
- TF-IDF Vectorizer
- SVM Model
- LSTM Model
- Model Comparison
- Evaluation Metrics
- Confusion Matrices

---
# result summary
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Model</th>
      <th>Accuracy</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1 Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SVM</td>
      <td>0.994965</td>
      <td>0.996217</td>
      <td>0.993164</td>
      <td>0.994688</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LSTM</td>
      <td>0.983889</td>
      <td>0.978738</td>
      <td>0.987506</td>
      <td>0.983103</td>
    </tr>
  </tbody>
</table>
</div>
# Author

Pesara

Student ID: CIT-24-01-0258

Branch

feature/CIT-24-01-0258-model

Sri Lanka Technology Campus
CCS3356 – Natural Language Processing
