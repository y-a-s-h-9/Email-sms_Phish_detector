import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.stem.porter import PorterStemmer
import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = re.findall(r'\b\w+\b', text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

# Load the dataset
df = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'text']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Transform the text
df['transformed_text'] = df['text'].apply(transform_text)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    df['transformed_text'], df['label'], test_size=0.2, random_state=42)

# Vectorization
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Accuracy (optional)
predictions = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, predictions))

# Save model and vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Training complete. Model and vectorizer saved.")
