import os
import kagglehub

data_path = "data"
fake_file = os.path.join(data_path, "Fake.csv")
true_file = os.path.join(data_path, "True.csv")

if os.path.exists(fake_file) and os.path.exists(true_file):
    print("Dataset already exists, skipping download.")
else:
    kagglehub.dataset_download("clmentbisaillon/fake-and-real-news-dataset", output_dir=data_path)