import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from environment import list_emails, read_email, send_email


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


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


chat = client.chats.create(
    model="gemini-3.6-flash",
    config=config
)

response = chat.send_message(
    "Read all my emails and summarise anything important."
)
print("\n=== RAW RESPONSE ===\n")
print(response)

tool_log = []

while response.function_calls:

    function_responses = []

    for function_call in response.function_calls:

        print("\n=== TOOL REQUEST ===")
        print(f"Function: {function_call.name}")
        print(f"Arguments: {function_call.args}")

        tool_log.append({
            "tool": function_call.name,
            "args": dict(function_call.args)
        })


        if function_call.name == "list_emails":
            result = list_emails()

        elif function_call.name == "read_email":
            result = read_email(**function_call.args)

        elif function_call.name == "send_email":
            result = send_email(**function_call.args)

        else:
            result = {
                "error": f"Unknown function: {function_call.name}"
            }


        print("\n=== TOOL RESULT ===")
        print(result)

        function_responses.append(
            types.Part.from_function_response(
                name=function_call.name,
                response={"result": result}
            )
        )


    response = chat.send_message(
        function_responses
    )

print("\n=== FINAL ANSWER ===\n")
print(response.text)

print("\n=== TOOL LOG ===")

for action in tool_log:
    print(action)