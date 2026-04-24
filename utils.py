def generate_explanation(inputs):

    reasons = []

    if inputs.get("job_satisfaction", 3) <= 2:
        reasons.append("Low job satisfaction")

    if inputs.get("work_life_balance", 3) <= 2:
        reasons.append("Poor work-life balance")

    if inputs.get("completion_pct", 100) < 60:
        reasons.append("Low task completion")

    if inputs.get("OverTime") == "Yes":
        reasons.append("High overtime")

    if not reasons:
        reasons.append("Balanced performance indicators")

    return reasons