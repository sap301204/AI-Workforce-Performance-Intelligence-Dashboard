# 🚀 AI Workforce Performance Intelligence Dashboard

An end-to-end **AI-powered HR Analytics Dashboard** that not only visualizes employee data but also **predicts performance, explains outcomes, and suggests actionable HR decisions.**

---

## 🎯 Project Overview

Most dashboards stop at visualization.

This project goes beyond that by combining:
- 📊 Data Analytics
- 🤖 Machine Learning
- 🧠 Explainable Insights
- 🎯 Decision Support

👉 Result: A **smart workforce intelligence system**

---

## ✨ Key Features

### 📊 Dashboard Analytics
- Total Employees, Projects, Tasks, Completion %
- Department-wise performance analysis
- Salary distribution by job roles
- Top performers identification

### 🤖 AI Prediction System
- Predict employee performance (Low / Medium / High)
- Uses trained ML model (Scikit-learn)

### 🧠 Explainability Layer
- “Why this prediction?” section
- Highlights key factors like:
  - Work-life balance
  - Job satisfaction
  - Task completion rate
  - Overtime impact

### 🎯 HR Decision Support
- Automated recommendations:
  - Performance improvement plan
  - Monitoring strategy
  - Promotion readiness

---

## 🛠️ Tech Stack

- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **Streamlit**
- **Plotly**
- **Joblib**

---

## 📁 Project Structure
├── data/
│ ├── employee_performance_dataset.csv
│ └── final_dashboard_data.csv
│
├── models/
│ ├── model.pkl
│ ├── encoder.pkl
│ └── columns.pkl
│
├── src/
│ ├── data_enhancer.py
│ ├── model_train.py
│ ├── preprocess.py
│ ├── predict.py
│ └── utils.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Run

1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/AI-Workforce-Performance-Intelligence-Dashboard.git
cd AI-Workforce-Performance-Intelligence-Dashboard
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Requirements
pip install -r requirements.txt
4️⃣ Run Application
streamlit run app.py
