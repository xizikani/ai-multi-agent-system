
import json

def create_state(requirement: str):
    return {
        "requirement": requirement,
        "analysis": None,
        "architecture": None,
        "code": None,
        "review": None,
        "iteration": 0
    }

def to_json(state):
    return json.dumps(state, ensure_ascii=False, indent=2)
