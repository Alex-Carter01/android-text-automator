from outgoingtext import type_message
from incomingtext import receive_sms

import time

###########################
# High Level Script Parser
# Input: Script file with main character, character list header
# Action: Orchestrates everything needed for a conversation
#       Creates android contact cards, iterates script lines, decides typing actions
###########################

# Custom exception
class CustomError(Exception):
    pass

# TODO create contacts

pattern = r'\(([^,]+),\s*([^)]+)\)\s*(.+)'

f = open("demo-meta1.txt", "r")

lines = file.readlines()
if len(lines < 3):
    print("script too short AND VALIDATION ERROR")
    raise CustomError("script too short AND VALIDATION ERROR")

main_char = lines[0]
char_list = lines[1]

#converse lines
for line in lines[2:]:
    match = re.match(pattern, line)
    if match:
        character1 = match.group(1)
        character2 = match.group(2)
        dialogue = match.group(3)
        if character1 == main_char:
            type_message(line)
        elif character2 == main_char:
            receive_sms(number, line)
        else:
            print("main character not involved in dialogue AND VALIDATION FAIL")
            break
    else:
        print("line does not contain valid tag AND VALIDATION FAIL")


#TODO delete contacts / logs