from outgoingtext import type_message
import time
import subprocess

def receive_sms(from_number, message):
    # Construct the ADB command
    adb_command = f'adb emu sms send {from_number} "{message}"'

    # Run the ADB command
    subprocess.call(adb_command, shell=True)


receive_sms("1234567890", "sms send admu emu ♓️")
receive_sms("1234567890", "Character A: Hey, did you hear abo😬ut Sarah and Mark?")

f = open("demo-script2.txt", "r")
for x in f:
    message = x[13:]
    if x[:11] == "Character B":
        type_message(message)
    else:
        receive_sms(5128377500, message)
        time.sleep(2)