
def run(state):
    code = state["code"]
    issues = []

    for k, v in code.items():
        if "{}" in v:
            issues.append(f"{k} 代码不完整")

    state["review"] = {
        "issues": issues,
        "status": "PASS" if not issues else "NEEDS_FIX"
    }
    return state
