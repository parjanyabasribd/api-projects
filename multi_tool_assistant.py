import os
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_github_user_info(username: str) -> str:
    """Get public GitHub profile info for a given username"""
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code != 200:
        return f"Could not find GitHub user '{username}'."
    data = response.json()
    return (
        f"{data['login']} has {data['public_repos']} public repos, "
        f"{data['followers']} followers, and {data['following']} following. "
        f"Bio: {data['bio']}"
    )


def get_random_advice() -> str:
    """Get a random piece of life advice"""
    response = requests.get("https://api.adviceslip.com/advice")
    if response.status_code != 200:
        return "Could not fetch advice at this time."
    data = response.json()
    return data['slip']['advice']


client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config={"temperature": 0.2, "tools": [get_github_user_info, get_random_advice]}
)

text = input("Enter your text: ")
response = chat.send_message(text)

print("\nFINAL ANSWER:")
print(response.text)

tools_used = []
for item in response.automatic_function_calling_history:
    for part in item.parts:
        if part.function_call:
            tools_used.append(f"{part.function_call.name}({part.function_call.args})")

if tools_used:
    print("\n--- TOOLS USED ---")
    for call in tools_used:
        print(f"✓ {call}")
else:
    print("\n(No tools were used for this question — answered directly.)")