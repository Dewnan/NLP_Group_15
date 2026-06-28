import pandas as pd
import re

def load_and_merge(true_path='data/True.csv', false_path='data/Fake.csv'):

    real_df = pd.read_csv(true_path)
    fake_df = pd.read_csv(false_path)
    
    real_df['label'] = 0  # real
    fake_df['label'] = 1  # fake
    
    merged_df = pd.concat([real_df, fake_df], ignore_index=True)
    merged_df = merged_df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return merged_df


def text_cleaner(text):
    text = str(text)
    text = re.sub(r'https?://\S+', '', text) # remove URLs
    text = re.sub(r'pic\.twitter\.com/\w+', '', text) # remove twitter pic links# remove embedded JS (fb sdk etc)
    text = re.sub(r'\((IMAGE|VIDEO|PHOTO)\)', '', text) # remove media tags
    text = re.sub(r'Featured\s+\w+\s+via\s+\S+(?:\s+\S+){0,5}', '', text) # remove image credit lines
    text = re.sub(r'\(@\w+\)', '', text) # remove user handles
    text = re.sub(r'#\w+', '', text) # remove hashtags
    text = re.sub(r'\s+', ' ', text).strip() # remove extra whitespace
    return text