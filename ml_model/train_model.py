from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load dataset
dataset = load_dataset("dair-ai/emotion")
texts = dataset['train']['text']
labels = dataset['train']['label']

# Label mapping for human-readable mood
label_map = dataset['train'].features['label'].names  # List like ['sadness', 'joy', ...]

# Vectorize text
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(texts)
y = labels

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
clf = LogisticRegression(max_iter=200)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=label_map))

# Save model & vectorizer
joblib.dump(clf, "ml_model/emotion_model.pkl")
joblib.dump(vectorizer, "ml_model/vectorizer.pkl")
joblib.dump(label_map, "ml_model/label_map.pkl")

