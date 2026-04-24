import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(
    page_title="Workforce Performance Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- PREMIUM DASHBOARD CSS ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #eaf7fb 0%, #f4fbff 100%);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #073b46 0%, #0b5663 100%);
    color: white;
    padding-top: 20px;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: white !important;
}

.sidebar-title {
    color: white;
    font-size: 24px;
    font-weight: 900;
    margin-bottom: 25px;
}

.main-title {
    background: linear-gradient(90deg, #073b46, #0e7490);
    padding: 24px;
    border-radius: 18px;
    color: white;
    text-align: center;
    font-size: 34px;
    font-weight: 900;
    box-shadow: 0 8px 22px rgba(0,0,0,0.18);
    margin-bottom: 25px;
}

.kpi-card {
    background: #073b46;
    color: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.18);
    border-left: 6px solid #38bdf8;
}

.kpi-label {
    font-size: 14px;
    color: #bdefff;
    font-weight: 700;
}

.kpi-value {
    font-size: 34px;
    font-weight: 900;
    color: white;
}

.chart-card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(15,23,42,0.12);
    margin-top: 20px;
}

.prediction-card {
    background: white;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(15,23,42,0.12);
    margin-top: 20px;
}

.rank-card {
    background: linear-gradient(180deg, #073b46, #0e7490);
    color: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.18);
    text-align: center;
    min-height: 230px;
}

.rank-card h3 {
    color: white;
    margin-bottom: 5px;
}

.rank-subtext {
    font-size: 13px;
    color: #d9faff;
    margin: 4px 0;
}

.rank-line {
    border: 0.5px solid #67e8f9;
}

.stButton > button {
    background: #0e7490;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 18px;
    font-weight: 700;
    width: 100%;
}

.stButton > button:hover {
    background: #155e75;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD FILES ----------------
df = pd.read_csv("data/final_dashboard_data.csv")
model = joblib.load("models/model.pkl")
encoder = joblib.load("models/encoder.pkl")
columns = joblib.load("models/columns.pkl")

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

def go(page):
    st.session_state.page = page
    st.rerun()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown('<div class="sidebar-title">📊 PERFORMANCE HUB</div>', unsafe_allow_html=True)

    if st.button("🏠 Dashboard"):
        go("Dashboard")

    if st.button("📈 Performance"):
        go("Performance")

    if st.button("🤖 AI Prediction"):
        go("AI Prediction")

# ---------------- CHART STYLE ----------------
def style_chart(fig):
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="#073b46", size=13),
        title_font=dict(size=18, color="#073b46"),
        margin=dict(l=30, r=30, t=50, b=30),
        height=380,
        showlegend=True
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="#dbeafe")
    return fig

# ---------------- DASHBOARD PAGE ----------------
if st.session_state.page == "Dashboard":

    st.markdown(
        '<div class="main-title">Workforce Performance Intelligence Dashboard</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">TOTAL EMPLOYEES</div>
            <div class="kpi-value">{len(df):,}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">TOTAL PROJECTS</div>
            <div class="kpi-value">{int(df["projects"].sum()):,}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">TOTAL TASKS</div>
            <div class="kpi-value">{int(df["tasks"].sum()):,}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">COMPLETION RATE</div>
            <div class="kpi-value">{df["completion_pct"].mean():.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        dept_score = df.groupby("department")["performance_score"].mean().reset_index()

        fig = px.bar(
            dept_score,
            x="department",
            y="performance_score",
            title="Average Performance Score by Department",
            color="department",
            color_discrete_sequence=["#0e7490", "#38bdf8", "#0891b2"]
        )

        st.plotly_chart(style_chart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        salary_role = df.groupby("job_role")["salary"].mean().reset_index()

        fig = px.bar(
            salary_role,
            x="job_role",
            y="salary",
            title="Average Salary by Job Role",
            color="job_role",
            color_discrete_sequence=["#073b46", "#0e7490", "#0891b2", "#38bdf8", "#67e8f9"]
        )

        st.plotly_chart(style_chart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- ENHANCED TOP PERFORMERS ----------------
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    st.subheader("🏆 Top Performers")
    st.caption("Best performing employees ranked by performance score")

    top_df = df.sort_values("performance_score", ascending=False).head(10).copy()
    top_df = top_df.reset_index(drop=True)
    top_df.insert(0, "Rank", range(1, len(top_df) + 1))

    top4 = top_df.head(4)
    card_cols = st.columns(4)
    medals = ["🥇", "🥈", "🥉", "🏅"]

    for i, (_, row) in enumerate(top4.iterrows()):
        with card_cols[i]:
            st.markdown(f"""
            <div class="rank-card">
                <div style="font-size: 38px;">{medals[i]}</div>
                <h3>Rank {int(row['Rank'])}</h3>
                <p style="font-size: 15px; margin: 4px 0;"><b>{row['job_role']}</b></p>
                <p class="rank-subtext">{row['department']}</p>
                <hr class="rank-line">
                <p style="margin: 4px 0;">Score: <b>{row['performance_score']:.2f}</b></p>
                <p style="margin: 4px 0;">Completion: <b>{row['completion_pct']:.2f}%</b></p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    display_df = top_df[
        [
            "Rank",
            "job_role",
            "department",
            "salary",
            "projects",
            "tasks",
            "tasks_completed",
            "completion_pct",
            "performance_score",
            "performance_band"
        ]
    ].copy()

    display_df.rename(columns={
        "job_role": "Job Role",
        "department": "Department",
        "salary": "Salary",
        "projects": "Projects",
        "tasks": "Tasks",
        "tasks_completed": "Tasks Completed",
        "completion_pct": "Completion %",
        "performance_score": "Performance Score",
        "performance_band": "Performance Band"
    }, inplace=True)

    display_df["Completion %"] = display_df["Completion %"].round(2)
    display_df["Performance Score"] = display_df["Performance Score"].round(2)

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PERFORMANCE PAGE ----------------
elif st.session_state.page == "Performance":

    st.markdown(
        '<div class="main-title">Performance Analytics</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        fig = px.pie(
            df,
            names="performance_band",
            title="Performance Band Distribution",
            color_discrete_sequence=["#0e7490", "#38bdf8", "#ff5a5f"]
        )

        st.plotly_chart(style_chart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)

        fig = px.box(
            df,
            x="performance_band",
            y="salary",
            color="performance_band",
            title="Salary Distribution by Performance Band",
            color_discrete_sequence=["#0e7490", "#38bdf8", "#ff5a5f"]
        )

        st.plotly_chart(style_chart(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- AI PREDICTION PAGE ----------------
elif st.session_state.page == "AI Prediction":

    st.markdown(
        '<div class="main-title">AI Employee Performance Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="prediction-card">', unsafe_allow_html=True)

    sample = df.iloc[0].drop(["performance_band", "performance_score"])
    inputs = {}

    st.subheader("Enter Employee Details")

    col1, col2 = st.columns(2)

    input_columns = list(sample.index)

    for i, col in enumerate(input_columns):
        target_col = col1 if i % 2 == 0 else col2

        with target_col:
            if df[col].dtype == "object":
                inputs[col] = st.selectbox(
                    col,
                    df[col].dropna().unique()
                )
            else:
                value = float(sample[col])

                if col == "Age":
                    inputs[col] = st.number_input(
                        "Age",
                        min_value=18,
                        max_value=65,
                        value=int(value),
                        step=1
                    )
                elif col == "projects":
                    inputs[col] = st.number_input(
                        col,
                        min_value=1,
                        max_value=20,
                        value=int(value),
                        step=1
                    )
                elif col == "tasks":
                    inputs[col] = st.number_input(
                        col,
                        min_value=1,
                        max_value=200,
                        value=int(value),
                        step=1
                    )
                elif col == "tasks_completed":
                    inputs[col] = st.number_input(
                        col,
                        min_value=0,
                        max_value=200,
                        value=int(value),
                        step=1
                    )
                else:
                    inputs[col] = st.number_input(
                        col,
                        value=float(value),
                        step=1.0
                    )

    input_df = pd.DataFrame([inputs])

    if "tasks" in input_df.columns and "tasks_completed" in input_df.columns:
        if input_df.loc[0, "tasks_completed"] > input_df.loc[0, "tasks"]:
            input_df.loc[0, "tasks_completed"] = input_df.loc[0, "tasks"]

        input_df["completion_pct"] = (
            input_df["tasks_completed"] / input_df["tasks"]
        ) * 100

    input_encoded = pd.get_dummies(input_df)

    for col in columns:
        if col not in input_encoded:
            input_encoded[col] = 0

    input_encoded = input_encoded[columns]

    if st.button("Predict Performance"):

        pred = model.predict(input_encoded)[0]
        label = encoder.inverse_transform([pred])[0]

        if label == "High":
            st.success(f"Prediction: {label} Performer")
        elif label == "Medium":
            st.warning(f"Prediction: {label} Performer")
        else:
            st.error(f"Prediction: {label} Performer")

        st.subheader("Why this prediction?")

        reasons = []

        if "job_satisfaction" in inputs and inputs["job_satisfaction"] <= 2:
            reasons.append("Low job satisfaction may reduce employee performance.")

        if "work_life_balance" in inputs and inputs["work_life_balance"] <= 2:
            reasons.append("Poor work-life balance may indicate burnout risk.")

        if "completion_pct" in input_df.columns and input_df.loc[0, "completion_pct"] < 60:
            reasons.append("Low task completion rate affects productivity.")

        if "OverTime" in inputs and inputs["OverTime"] == "Yes":
            reasons.append("Overtime may increase stress and reduce long-term performance.")

        if not reasons:
            reasons.append("Employee indicators are balanced across workload, satisfaction, and productivity.")

        for reason in reasons:
            st.write(f"- {reason}")

        st.subheader("Recommended HR Action")

        if label == "Low":
            st.write("- Schedule manager one-on-one discussion.")
            st.write("- Assign mentoring or coaching support.")
            st.write("- Review workload and satisfaction levels.")
            st.write("- Create a 30-day performance improvement plan.")
        elif label == "Medium":
            st.write("- Monitor performance monthly.")
            st.write("- Provide targeted training.")
            st.write("- Give project ownership opportunities.")
        else:
            st.write("- Consider reward or recognition.")
            st.write("- Evaluate for promotion readiness.")
            st.write("- Assign leadership or high-impact projects.")

    st.markdown('</div>', unsafe_allow_html=True)