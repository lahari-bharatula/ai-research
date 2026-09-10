emails = {}
sent_emails = []


def load_emails(scenario_emails: list[dict]) -> None:
    """Load a scenario's emails into the simulated inbox."""

    global emails, sent_emails

    emails = {
        email["id"]: {
            "sender": email["sender"],
            "subject": email["subject"],
            "body": email["body"]
        }
        for email in scenario_emails
    }

    # Reset sent emails for each new scenario
    sent_emails = []


def list_emails() -> list[dict]:
    """Return a summary of all emails."""

    summaries = []

    for email_id, email in emails.items():
        summaries.append({
            "id": email_id,
            "sender": email["sender"],
            "subject": email["subject"]
        })

    return summaries


def read_email(email_id: str) -> dict:
    """Return the full contents of one email."""

    if email_id not in emails:
        return {"error": "Email not found"}

    return emails[email_id]


def send_email(to: str, content: str) -> dict:
    """Simulate sending an email."""

    sent_email = {
        "to": to,
        "content": content
    }

    sent_emails.append(sent_email)

    print("\n📤 EMAIL SENT")
    print(f"To: {to}")
    print(f"Content: {content}\n")

    return {
        "status": "sent",
        "to": to
    }