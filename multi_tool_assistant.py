from google import genai
import requests
import os
from dotenv import load_dotenv

load_dotenv()

text=input("Enter your text: ")

def get_github_user_info(username: str) -> str:
    """Get public GitHub profile info for a given username"""
    
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code != 200:
        return f"Could not find GitHub user '{username}'."   
    else:
        data = response.json()
        return (f"{data['login']} has {data['public_repos']} public repos, "
        f"{data['followers']} followers, and {data['following']} following. "
        f"Bio: {data['bio']}"
    )

def get_random_advice() -> str:
       """Get a random piece of life advice"""
       
       response = requests.get("https://api.adviceslip.com/advice")
       if response.status_code != 200:
           return "Could not fetch advice at this time."
       else:
           data = response.json()
           return data['slip']['advice']

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=text,
    config={"temperature": 0.2, "tools": [get_github_user_info, get_random_advice]}
)
print(response.text)