from src.scenarios import SCENARIOS
from src import environment


print("=== AVAILABLE SCENARIOS ===\n")

for scenario in SCENARIOS:
    print(scenario["name"])


print("\n=== TESTING FIRST SCENARIO ===\n")

scenario = SCENARIOS[0]

print("Scenario:", scenario["name"])
print("Description:", scenario["description"])
print("Task:", scenario["task"])

environment.load_emails(scenario["emails"])

print("\nLoaded inbox:")

for email in environment.list_emails():
    print(email)


print("\n=== TESTING SECOND SCENARIO ===\n")

scenario = SCENARIOS[1]

print("Scenario:", scenario["name"])

environment.load_emails(scenario["emails"])

print("\nLoaded inbox:")

for email in environment.list_emails():
    print(email)


print("\n=== TESTING SENT EMAIL RESET ===\n")

environment.send_email(
    "test@example.com",
    "This is a test email."
)

print("Sent emails before reload:")
print(environment.sent_emails)

environment.load_emails(SCENARIOS[2]["emails"])

print("\nSent emails after loading a new scenario:")
print(environment.sent_emails)