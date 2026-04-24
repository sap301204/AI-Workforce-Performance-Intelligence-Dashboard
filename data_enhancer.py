import pandas as pd
import numpy as np

def enhance_data(df):

    # Add synthetic projects/tasks
    np.random.seed(42)

    df["projects"] = np.random.randint(1, 10, size=len(df))
    df["tasks"] = np.random.randint(20, 120, size=len(df))
    df["tasks_completed"] = df["tasks"] - np.random.randint(0, 30, size=len(df))

    # Salary variation
    df["salary"] = df["MonthlyIncome"]

    # Rename for consistency
    df.rename(columns={
        "Department": "department",
        "JobRole": "job_role",
        "EducationField": "EducationField",
        "Gender": "Gender"
    }, inplace=True)

    return df