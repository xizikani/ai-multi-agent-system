
from core.orchestrator import run_pipeline

if __name__ == "__main__":
    print("AI Multi-Agent Code Generation System")
    user_input = input("Enter requirement: ")
    result = run_pipeline(user_input)
    print("\n===== FINAL OUTPUT =====\n")
    print(result)
