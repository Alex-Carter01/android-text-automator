from outgoingtext import type_message
from incomingtext import receive_sms

import os
import openai
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

# Custom exception
class CustomError(Exception):
    pass

main_char = "Alice"
char_list = ["Alice", "Bob", "Carly"]

user_content_template = "I want you to write a story with {} speaking characters: {}. Write this script to be as lengthy as you can.  {} is \"the main character\", all dialogue should include {} as either CharacterNameSpeaking or CharacterNameReceiving. This story should be communicated entirely over text messages. do not include parenthetical comments, stage directions, or information about the characters, just their text-message based dialogue. Please use common text abbreviations, lots of emojis, etc. It should involve relationships, gossip, and be very trashy. the more unexpected twists the better. The story should be formatted as\n(CharacterNameSpeaking, CharacterNameReceiving) Dialogue\n Lengthy pieces of dialogue can be broken to multiple lines, each prefaced with the same (CharacterNameSpeaking, CharacterNameReceiving) tag"
user_content = user_content_template.format(len(char_list), ', '.join(char_list), main_char, main_char)

# Define the conversation history
conversation = [
    {"role": "system", "content": "You are a contemporary drama writer, skilled in creating dialogue that is captivating and full of surprises. Stylistically, you begin every line of dialogue with a (CharacterNameSpeaking, CharacterNameReceiving) tag. Stylistcally, you often breakdown one piece of dialogue into two shorter messages, with the same (CharacterNameSpeaking, CharacterNameReceiving) tag"},
    {"role": "user", "content": user_content}
]

# Initial script API call
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=conversation
)

script = completion.choices[0]['message']['content']
print(script)

# Validate script format
script_lines = script.splitlines()

if len(script_lines) < 20:
    print("ERROR script too short")
    raise CustomError("script too short")

# regex for character tag
pattern = r'\(([^,]+),\s*([^)]+)\)\s*(.+)'

# Validate Main character use and existance of speaking characters
for line in script_lines:
    if len(line) < 3:
        continue
    print("line",  line)
    match = re.match(pattern, line)
    if match:
        character1 = match.group(1)
        character2 = match.group(2)
        dialogue = match.group(3)
        print(f"Character1: {character1}, Character2: {character2}, Dialogue: {dialogue}")
        if not (character1 == main_char or character2 == main_char):
            print("ERROR main character not involved in dialogue")
            #raise CustomError("main character not involved in dialogue")
            #break
        if not (character1 in char_list):
            print("ERROR character1 does not exist")
            #raise CustomError("character1 does not exist")
            #break
        if not (character2 in char_list):
            print("ERROR character2 does not exist")
            #raise CustomError("character2 does not exist")
            #break
    else:
        print("ERROR line does not contain valid tag")
        raise CustomError("line does not contain valid tag")
        break

print("Validation successful, writing script to file...")

# Define the name of the environment variable
env_var_name = "FILE_COUNTER"

# Get the current counter value from the environment variable
counter = int(os.getenv(env_var_name, 0))

# Increment the counter for the next file
counter += 1

# Update the environment variable with the new counter value
os.environ[env_var_name] = str(counter)

# Create the file name with an incremented counter
file_name = f"script{counter}.txt"

with open(file_name, 'w') as file:
    file.write(main_char + "\n")
    file.write(str(char_list) + "\n")
    file.write(script)

print(f"Script and data has been written to {file_name}")