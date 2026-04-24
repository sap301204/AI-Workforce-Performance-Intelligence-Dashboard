import pandas as pd

def load_data(path="data/employee_performance_dataset.csv"):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df = df.dropna()

    # Remove impossible values
    df = df[df["tasks"] >= df["tasks_completed"]]

    # Create completion %
    df["completion_pct"] = (df["tasks_completed"] / df["tasks"]) * 100

    return df

def feature_engineering(df):

    # Performance score (synthetic logic)
    df["performance_score"] = (
        df["job_satisfaction"] * 20 +
        df["work_life_balance"] * 20 +
        df["completion_pct"] * 0.5 +
        df["salary"] * 0.0001
    )

    # Convert to band
    def band(score):
        if score >= 120:
            return "High"
        elif score >= 80:
            return "Medium"
        else:
            return "Low"

    df["performance_band"] = df["performance_score"].apply(band)

    return df

def save_final(df):
    df.to_csv("data/final_dashboard_data.csv", index=False)
    print("✅ Final dataset saved")