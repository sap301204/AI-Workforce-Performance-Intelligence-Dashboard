import joblib
import pandas as pd

model = joblib.load("models/model.pkl")
encoder = joblib.load("models/encoder.pkl")
columns = joblib.load("models/columns.pkl")

def predict_employee(data_dict):

    df = pd.DataFrame([data_dict])
    df = pd.get_dummies(df)

    for col in columns:
        if col not in df:
            df[col] = 0

    df = df[columns]

    pred = model.predict(df)[0]
    label = encoder.inverse_transform([pred])[0]

    return label