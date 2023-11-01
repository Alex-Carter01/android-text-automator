import os
import re
import subprocess
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# Custom exception
class CustomError(Exception):
    pass

main_char = "Alice"
char_list = ["Alice", "Bob", "Carly"]

user_content_template = "I want you to write a story with {} speaking characters: {}. Write this script to be as lengthy as you can.  {} is \"the main character\", all dialogue should include {} as either CharacterNameSpeaking or CharacterNameReceiving. This story should be communicated entirely over text messages. do not include parenthetical comments, stage directions, or information about the characters, just their text-message based dialogue. Please use common text abbreviations, lots of emojis, etc. It should involve relationships, gossip, and be very trashy. the more unexpected twists the better. The story should be formatted as\n(CharacterNameSpeaking, CharacterNameReceiving) Dialogue"
user_content = user_content_template.format(len(char_list), ', '.join(char_list), main_char, main_char)

# Define the conversation history
conversation = [
    {"role": "system", "content": "You are a contemporary drama writer, skilled in creating dialogue that is captivating and full of surprises. Stylistically, you begin every line of dialogue with a (CharacterNameSpeaking, CharacterNameReceiving) tag."},
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
valid_lines = []
for line in script_lines:
    if len(line) < 3:
        #print("Error, line too short")
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
            continue
        if not (character1 in char_list and character2 in char_list):
            print("ERROR character does not exist")
            #raise CustomError("character does not exist")
            continue
        valid_lines.append(line)
    else:
        print("ERROR line does not contain valid tag")
        continue

print("Validation successful, writing script to file...")

# Read counter from a file
with open('counter.txt', 'r') as file:
    counter = int(file.read())

# Increment the counter
counter += 1

# Write the updated counter back to the file
with open('counter.txt', 'w') as file:
    file.write(str(counter))

# Create the file name with an incremented counter
file_name = f"script{counter}.txt"

with open("scripts/" + file_name, 'w') as file:
    file.write(main_char + "\n")
    file.write(str(char_list) + "\n")
    file.write('\n'.join(valid_lines))

print(f"Script and data has been written to scripts/{file_name}")