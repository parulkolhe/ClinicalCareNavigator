import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("backend/data/disease_dataset.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["symptoms"])

model = MultinomialNB()
model.fit(X, data["disease"])


def predict(symptoms):

    text = " ".join(symptoms)

    X_test = vectorizer.transform([text])

    probs = model.predict_proba(X_test)[0]

    diseases = model.classes_

    result = sorted(
        zip(diseases, probs),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    return result