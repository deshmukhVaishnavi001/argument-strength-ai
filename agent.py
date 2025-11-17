import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import joblib

nltk.download("punkt")
nltk.download("stopwords")

model = joblib.load("model/argument_model.pkl")

STOP = set(stopwords.words("english"))

def analyze_argument(text):
    
    # 1️⃣ Predict strength
    strength = model.predict([text])[0]

    # 2️⃣ Detect fallacies (based on your dataset)
    fallacies = []
    if "everyone" in text.lower() or "always" in text.lower():
        fallacies.append("Overgeneralization")
    if "because I said so" in text.lower():
        fallacies.append("Authority Fallacy")
    if "if you don't agree" in text.lower():
        fallacies.append("Threat Fallacy")
    if "obviously" in text.lower():
        fallacies.append("Assumption Fallacy")

    # 3️⃣ Suggest improvement
    if strength == "weak":
        suggestion = "Strengthen your argument by adding facts, evidence, or real examples."
    else:
        suggestion = "Strong argument! You can improve it by adding references or statistics."

    return {
        "strength": strength,
        "fallacies": fallacies,
        "suggestion": suggestion
    }
