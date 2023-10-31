import os
import requests

# Set your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")\

print(api_key)

api_key = "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"

# Define the conversation history
conversation = [
    {"role": "system", "content": "You are a contemporary drama writer, skilled in creating dialogue that is captivating and full of surprises. Stylistically, you begin every line of dialogue with a (CharacterNameSpeaking, CharacterNameReceiving) tag. Stylistically, you do not add extra linebreaks between different characters speaking. Stylistically, you often breakdown one piece of dialogue into two shorter messages, with the same (CharacterNameSpeaking, CharacterNameReceiving) tag"},
    {"role": "user", "content": "I want you to write a story with 3 speaking characters: Alice, Bob, and Carly as long as you can.  I want you to pick one of the character who is \"the main character\", all dialogue should include them as either speaker or receiver. This story should be communicated entirely over text messages. do not include parenthetical comments, stage directions, or information about the characters, just their text-message based dialogue. Do not add empty lines between dialogue. Please use common text abbreviations, lots of emojis, etc. It should involve relationships, gossip, and be very trashy. the more unexpected twists the better. The story should be formatted as\n(CharacterNameSpeaking, CharacterNameReceiving) Dialogue\n Lengthy pieces of dialogue can be broken to multiple lines, each prefaced with the same (CharacterNameSpeaking, CharacterNameReceiving) tag"}
]

# Define the data for the API request
data = {
    "model": "gpt-3.5-turbo",
    "messages": conversation
}

# Define the headers with the API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Make the API request
response = requests.post("https://api.openai.com/v1/engines/gpt-3.5-turbo/completions", json=data, headers=headers)

# Check the response status code
if response.status_code == 200:
    script = response.json()["choices"][0]["message"]["content"]
    print(script)
else:
    print(f"API request failed with status code: {response.status_code}")