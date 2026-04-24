import pandas as pd
from src.data_enhancer import enhance_dataset
from src.model_train import train_performance_model

df = pd.read_csv("data/employee_performance_dataset.csv")

df = enhance_dataset(df)

df.to_csv("data/final_dashboard_data.csv", index=False)

train_performance_model()

print("Full pipeline done")