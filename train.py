import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("data/arguments.csv")

X = df["argument"]
y = df["strength"]   # strong / weak

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "model/argument_model.pkl")

print("Model saved at: model/argument_model.pkl")
