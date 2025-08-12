# scripts/train_model.py

from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    print("Training model...")
