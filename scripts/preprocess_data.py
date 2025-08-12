# scripts/preprocess_data.py

import pandas as pd

def load_data(path):
    return pd.read_csv(path)

if __name__ == "__main__":
    print("Preprocessing data...")
