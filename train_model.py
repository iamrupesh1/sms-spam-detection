import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# Set paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "spam.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "spam_model.pkl")

# Load data
df = pd.read_csv(CSV_PATH, encoding="latin-1")
df = df[['v1', 'v2']]  # Keep only label and message
df.columns = ['label', 'message']

# Map labels to 'spam' and 'ham'
df['label'] = df['label'].map({'ham': 'Not Spam', 'spam': 'Spam'})

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42
)

# Vectorize text
vectorizer = CountVectorizer()
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vect, y_train)

# Save vectorizer + model as a tuple
os.makedirs(os.path.join(BASE_DIR, "models"), exist_ok=True)
with open(MODEL_PATH, "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Training complete. Model saved at:", MODEL_PATH)
