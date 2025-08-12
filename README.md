# Cancer Gene Expression Classifier

## Project Overview
This project builds a machine learning classifier to predict cancer types from RNA-seq gene expression profiles using TCGA dataset.

## Dataset
Source: [TCGA Gene Expression Data on Kaggle](https://www.kaggle.com/datasets/fireballbyedimyrnmom/us-gene-expression-cancer-rnaseq)

## Goals
- Preprocess RNA-seq data
- Perform feature selection (variance threshold, PCA)
- Train and evaluate classification models
- Visualize feature importance and model performance

## Folder Structure
```
data/raw           -> Raw datasets downloaded from Kaggle
data/processed     -> Cleaned and preprocessed data
notebooks          -> Jupyter notebooks for exploration and model building
scripts            -> Python scripts for preprocessing and training
results/figures    -> Visualizations and plots
results/models     -> Saved trained models
docs               -> Additional documentation and references
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage
1. Download dataset into `data/raw`
2. Run preprocessing script:
```bash
python scripts/preprocess_data.py
```
3. Train model:
```bash
python scripts/train_model.py
```

## License
MIT License
