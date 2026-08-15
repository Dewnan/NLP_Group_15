import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

def load_and_merge(true_path='data/True.csv', false_path='data/Fake.csv'):

    real_df = pd.read_csv(true_path)
    fake_df = pd.read_csv(false_path)
    
    real_df['label'] = 1  # real
    fake_df['label'] = 0  # fake
    
    merged_df = pd.concat([real_df, fake_df], ignore_index=True)
    merged_df = merged_df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return merged_df

def normalize_text(text):
    text = str(text)
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'https?://\S+', '', text) # remove URLs
    text = re.sub(r'pic\.twitter\.com/\w+', '', text) # remove twitter pic links
    text = re.sub(r'\((IMAGE|VIDEO|PHOTO)\)', '', text) # remove media tags
    text = re.sub(r'Featured\s+\w+\s+via\s+\S+(?:\s+\S+){0,5}', '', text) # remove image credit lines
    text = re.sub(r'\(@\w+\)', '', text) # remove user handles
    text = re.sub(r'@\w+', '', text)  # remove handles without ()
    text = re.sub(r'#\w+', '', text) # remove hashtags
    text = re.sub(r'[^a-zA-Z\s]', ' ', text) # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip() # remove extra whitespace
    return text

def drop_duplicate_rows(df, column):
    df_len_before = len(df)
    df = df.drop_duplicates(subset=[column]).reset_index(drop=True) # Dropping duplicate rows from content
    dropped_count = df_len_before- len(df)
    print(f"Dropped {dropped_count} duplicate rows")
    
    return df

def drop_short_content(df, min_words=5):
    df_len_before = len(df)
    df = df[df['content'].str.split().str.len() >= min_words].reset_index(drop=True) # dropping empty rows and rows with less than 5 charactors
    print(f"Dropped {df_len_before - len(df)} rows with empty or near empty content")

    return df

def build_content_and_clean(df):
    # Combine title and text into a single column and remove other columns
    df = df.copy()
    df['content'] = (df['title'].fillna('') + ' ' + df['text'].fillna('')).str.strip() # fill NaN
    df['content'] = df['content'].apply(normalize_text)
    df = df.drop(columns=['title', 'text', 'subject', 'date'])
    
    df = drop_duplicate_rows(df, column='content')
    df = drop_short_content(df, 5)
    
    return df

stop_words = set(stopwords.words('english'))
custom_stopwords = {"u", "reuters"}
stop_words.update(custom_stopwords)

lemmatizer = WordNetLemmatizer()

def tokenize_and_lemmatize(text):
    text = text.lower() # Lowercase here because normalize_text() regex depends on letter casing.
    tokens = word_tokenize(text)
    
    cleaned_tokens = []
    for token in tokens:
        if token not in stop_words:
            lemmatized = lemmatizer.lemmatize(token)
            cleaned_tokens.append(lemmatized)
    
    return ' '.join(cleaned_tokens)

def apply_tokenize(df):
    df = df.copy()
    df['content'] = df['content'].apply(tokenize_and_lemmatize)
    return df
