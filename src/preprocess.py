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

sample = "Donald Trump Sends Out Embarrassing New Year’s Eve Message; This is Disturbing, Donald Trump just couldn t wish all Americans a Happy New Year and leave it at that. Instead, he had to give a shout out to his enemies, haters and  the very dishonest fake news media.  The former reality show star had just one job to do and he couldn t do it. As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, and even the very dishonest Fake News Media, a Happy and Healthy New Year,  President Angry Pants tweeted.  2018 will be a great year for America! As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, and even the very dishonest Fake News Media, a Happy and Healthy New Year. 2018 will be a great year for America!  Donald J. Trump (@realDonaldTrump) December 31, 2017Trump s tweet went down about as welll as you d expect.What kind of president sends a New Year s greeting like this despicable, petty, infantile gibberish? Only Trump! His lack of decency won t even allow him to rise above the gutter long enough to wish the American citizens a happy new year!  Bishop Talbert Swan (@TalbertSwan) December 31, 2017no one likes you  Calvin (@calvinstowell) December 31, 2017Your impeachment would make 2018 a great year for America, but I ll also accept regaining control of Congress.  Miranda Yaver (@mirandayaver) December 31, 2017Do you hear yourself talk? When you have to include that many people that hate you you have to wonder? Why do the they all hate me?  Alan Sandoval (@AlanSandoval13) December 31, 2017Who uses the word Haters in a New Years wish??  Marlene (@marlene399) December 31, 2017You can t just say happy new year?  Koren pollitt (@Korencarpenter) December 31, 2017Here s Trump s New Year s Eve tweet from 2016.Happy New Year to all, including to my many enemies and those who have fought me and lost so badly they just don t know what to do. Love!  Donald J. Trump (@realDonaldTrump) December 31, 2016This is nothing new for Trump. He s been doing this for years.Trump has directed messages to his  enemies  and  haters  for New Year s, Easter, Thanksgiving, and the anniversary of 9/11. pic.twitter.com/4FPAe2KypA  Daniel Dale (@ddale8) December 31, 2017Trump s holiday tweets are clearly not presidential.How long did he work at Hallmark before becoming President?  Steven Goodine (@SGoodine) December 31, 2017He s always been like this . . . the only difference is that in the last few years, his filter has been breaking down.  Roy Schulze (@thbthttt) December 31, 2017Who, apart from a teenager uses the term haters?  Wendy (@WendyWhistles) December 31, 2017he s a fucking 5 year old  Who Knows (@rainyday80) December 31, 2017So, to all the people who voted for this a hole thinking he would change once he got into power, you were wrong! 70-year-old men don t change and now he s a year older.Photo by Andrew Burton/Getty Images."

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

def preprocess(df):
    # Combine title and text into a single coulmn and remove other coulmns because
    # Title alone is too short, text alone loses the headline signal
    # together they give the model the full picture of the article
    
    df['content'] = df['title'] + ' ' + df['text']
    df['content'] = df['content'].apply(text_cleaner)
    df = df.drop(columns=['title', 'text', 'subject', 'date'])
    return df

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def tokenize_and_lemmatize(text):
    text = text.lower() # Lowercase here because text_cleaner() regex depends on letter casing.
    tokens = word_tokenize(text)
    
    cleaned_tokens = []
    for token in tokens:
        if token not in stop_words:
            lemmatized = lemmatizer.lemmatize(token)
            cleaned_tokens.append(lemmatized)
    
    return ' '.join(cleaned_tokens)

def apply_tokenize(df):
    df['content'] = df['content'].apply(tokenize_and_lemmatize)
    return df
