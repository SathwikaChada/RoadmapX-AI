"""Train TF-IDF + Logistic Regression career classifier."""
import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

DATA_PATH = "data/career_profiles.csv"
MODEL_PATH = "models/career_model.joblib"


def profile_to_text(skills, specialization, education, certifications) -> str:
    return f"{skills} | {specialization} | {education} | {certifications}"


def build_text(df: pd.DataFrame) -> pd.Series:
    df = df.fillna("")
    return df.apply(lambda r: profile_to_text(r["skills"], r["specialization"], r["education"], r["certifications"]), axis=1)


def train():
    if not os.path.exists(DATA_PATH):
        import generate_data
        generate_data.main()
    df = pd.read_csv(DATA_PATH)
    X, y = build_text(df), df["career"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), token_pattern=r"[^,|]+", lowercase=True, sublinear_tf=True)),
        ("clf", LogisticRegression(max_iter=1000, C=5.0)),
    ])
    model.fit(X_tr, y_tr)
    pred = model.predict(X_te)
    acc = accuracy_score(y_te, pred)
    print(f"Test accuracy: {acc:.3f}")
    print(classification_report(y_te, pred))
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return model, acc


if __name__ == "__main__":
    train()
