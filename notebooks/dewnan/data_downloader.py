import os
import kagglehub

def download_dataset(dataset_path="data"):
    false_file = os.path.join(dataset_path, "Fake.csv")
    true_file = os.path.join(dataset_path, "True.csv")

    if os.path.exists(false_file) and os.path.exists(true_file):
        print("Dataset already exists, skipping download.")
        return dataset_path

    try:
        os.makedirs(dataset_path, exist_ok=True)
        kagglehub.dataset_download("clmentbisaillon/fake-and-real-news-dataset", output_dir=dataset_path)
        return dataset_path
    except Exception as exc:
        raise RuntimeError("Download failed.") from exc