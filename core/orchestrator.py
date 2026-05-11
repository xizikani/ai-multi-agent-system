
from core.state import create_state
from agents import requirement_agent, architecture_agent, code_agent, review_agent

def run_pipeline(requirement: str):
    state = create_state(requirement)

    # Agent 1: requirement analysis
    state = requirement_agent.run(state)

    # Agent 2: architecture design
    state = architecture_agent.run(state)

    # Agent 3: code generation
    state = code_agent.run(state)

    # Agent 4: review
    state = review_agent.run(state)

    if state["review"]["status"] != "PASS":
        state["iteration"] += 1
        state["code"]["FIX"] = "Auto fix required (iteration loop simulated)"

    return state
