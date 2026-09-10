import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from src.environment import list_emails, read_email, send_email


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


tools = [
    list_emails,
    read_email,
    send_email
]


def run_agent(task: str) -> dict:

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

    response = chat.send_message(task)

    tool_log = []

    while True:

        function_calls = response.function_calls

        print("\n=== FUNCTION CALLS RECEIVED ===")
        print(function_calls)

        # No more tool calls → agent is finished
        if not function_calls:
            break

        function_responses = []

        for function_call in function_calls:

            print("\n=== TOOL REQUEST ===")
            print(f"Function: {function_call.name}")
            print(f"Arguments: {function_call.args}")

            tool_log.append({
                "tool": function_call.name,
                "args": dict(function_call.args)
            })

            # Execute the requested tool
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

            # Package the result for Gemini
            function_responses.append(
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": result}
                )
            )

        print("\n=== SENDING TOOL RESULTS BACK TO GEMINI ===")

        response = chat.send_message(function_responses)

        print("\n=== GEMINI RESPONDED ===")

    return {
        "final_answer": response.text,
        "tool_log": tool_log
    }