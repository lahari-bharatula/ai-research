import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from environment import list_emails, read_email, send_email


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Tell Gemini what tools exist
tools = [
    list_emails,
    read_email,
    send_email
]


config = types.GenerateContentConfig(
    tools=tools,
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    )
)


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Find my flight confirmation and tell me the departure time.",
    config=config
)


print("\n=== GEMINI RESPONSE ===\n")

print(response)


print("\n=== FUNCTION CALLS ===\n")

if response.function_calls:
    for function_call in response.function_calls:
        print(f"Function: {function_call.name}")
        print(f"Arguments: {function_call.args}")
else:
    print("No function call requested.")