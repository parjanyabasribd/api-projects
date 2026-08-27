import requests
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def country_info(country_name: str) -> str:
    """Get information(population, capital, languages, etc.) about a country using the REST Countries API"""
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    if response.status_code != 200:
        return f"Could not find information for country '{country_name}'."
    data = response.json()[0]
    return (
        f"{data['name']['common']} is located in {data['region']}. "
        f"It has a population of {data['population']} and its capital is {data['capital'][0]}. "
        f"The official languages are: {', '.join(data['languages'].values())}."
    )

def open_lib(book_title: str) -> str:
    """Get book information (title, author, publish date, etc.) when book title is provided using the Open Library API"""
    response = requests.get(f"https://openlibrary.org/search.json?title={book_title}")
    if response.status_code != 200 or not response.json().get("docs"):
        return f"Could not find information for book '{book_title}'."
    data = response.json()["docs"][0]
    authors = ', '.join(data.get('author_name', ['N/A']))
    return (
        f"Title: {data.get('title', 'N/A')}\n"
        f"Authors: {authors}\n"
        f"Publish Date: {data.get('first_publish_year', 'N/A')}\n"
        f"Number of Pages: {data.get('number_of_pages', 'N/A')}"
    )

def num_fact(num: int) -> str:
    """Get a fact about given number using the Numbers API"""
    response = requests.get(f"http://numbersapi.com/{num}")
    if response.status_code != 200:
        return f"Could not find a fact for number '{num}'."
    return response.text

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config={"temperature": 0.2, "tools": [country_info, open_lib, num_fact]})

while True:
    user_input = input("Enter your text : ")
    exit_check = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=f"Does {user_input} indicate the user wants to end the conversation? Answer only 'yes' or 'no'.\nMessage: {user_input}",
    config={"temperature": 0}
)
    if "yes" in exit_check.text.lower(): 

        print("Thank you for using the chat! Goodbye.")
        break

    else:
        response = chat.send_message(user_input)
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