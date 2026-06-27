import pandas as pd

def load_and_merge(true_path='data/True.csv', false_path='data/Fake.csv'):

    fake_dataFrame = pd.read_csv(false_path)
    real_dataFrame = pd.read_csv(true_path)

    real_dataFrame['label'] = 0  # real
    fake_dataFrame['label'] = 1  # fake

    mergedDataFrame = pd.concat([real_dataFrame, fake_dataFrame], ignore_index=True) # Add 2 data frames in to one and mix them randomly
    mergedDataFrame = mergedDataFrame.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return mergedDataFrame