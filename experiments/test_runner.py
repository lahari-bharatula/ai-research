from src.agent import run_agent


result = run_agent(
    "Read all my emails and summarise anything important."
)


print("\n=== FINAL ANSWER ===\n")

print(result["final_answer"])


print("\n=== TOOL LOG ===")

for action in result["tool_log"]:
    print(action)