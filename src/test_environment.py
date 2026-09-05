from environment import list_emails, read_email, send_email


print("=== INBOX ===")

for email in list_emails():
    print(email)


print("\n=== READING EMAIL ===")

email = read_email("email_1")

print(email)


print("\n=== SENDING EMAIL ===")

send_email(
    "friend@example.com",
    "My flight leaves at 8:30 AM."
)