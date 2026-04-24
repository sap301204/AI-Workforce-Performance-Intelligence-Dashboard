import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/final_dashboard_data.csv")

# ---------------- TARGET ----------------
target = "performance_band"

# ---------------- ENCODE TARGET ----------------
le = LabelEncoder()
df[target] = le.fit_transform(df[target])

# ---------------- FEATURES ----------------
X = df.drop(columns=[target])
y = df[target]

# ---------------- ONE HOT ----------------
X_encoded = pd.get_dummies(X)

# Save column structure
os.makedirs("models", exist_ok=True)
joblib.dump(X_encoded.columns.tolist(), "models/columns.pkl")

# ---------------- TRAIN ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=150,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------- SAVE ----------------
joblib.dump(model, "models/model.pkl")
joblib.dump(le, "models/encoder.pkl")

# ---------------- EVAL ----------------
y_pred = model.predict(X_test)

print("\nModel Performance:\n")
print(classification_report(y_test, y_pred))
print("\n✅ Model saved successfully (NO MORE EOF ERROR)")