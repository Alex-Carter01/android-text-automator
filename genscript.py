#llm api
#validate into [characters], main characterr, [(c1,c2)dialogue]
#create contacts
#send to convo
#delete contacts / logs

from outgoingtext import type_message
from conversation import receive_sms

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the conversation history
conversation = [
    {"role": "system", "content": "You are a contemporary drama writer, skilled in creating dialogue that is captivating and full of surprises. Stylistically, you begin every line of dialogue with a (CharacterNameSpeaking, CharacterNameReceiving) tag. Stylistically, you do not add extra linebreaks between different characters speaking. Stylistcally, you often breakdown one piece of dialogue into two shorter messages, with the same (CharacterNameSpeaking, CharacterNameReceiving) tag"},
    {"role": "user", "content": "I want you to write a story with 3 speaking characters: Alice, Bob, and Carly as long as you can.  I want you to pick one of the character who is \"the main character\", all dialogue should include them as either speaker or receiver. This story should be communicated entirely over text messages. do not include parenthetical comments, stage directions, or information about the characters, just their text-message based dialogue. Do not add empty lines between dialogue. Please use common text abbreviations, lots of emojis, etc. It should involve relationships, gossip, and be very trashy. the more unexpected twists the better. The story should be formatted as\n(CharacterNameSpeaking, CharacterNameReceiving) Dialogue\n Lengthy pieces of dialogue can be broken to multiple lines, each prefaced with the same (CharacterNameSpeaking, CharacterNameReceiving) tag"}
]


# Initial script API call
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=conversation
)

script = completion.choices[0]['message']['content']
print(script)

mc_question = "I am looking for a one word answer: who is the main character? do not include any extra words"
conversation.append({"role": "user", "content": mc_question})

# Make another API call with the extended conversation
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=conversation
)

main_character = completion.choices[0]['message']['content']
print(main_character)

chars_question = "please give a set of the characters in the format [character1, character2, character3]. do not include any unncessary words"
conversation.append({"role": "user", "content": chars_question})

# Make another API call with the extended conversation
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=conversation
)

# Extract and print the response to the follow-up question
char_list = completion.choices[0]['message']['content']
print(char_list)