import telnetlib
import os
import subprocess

def open_connection(port):
    # Define the host and port.
    host = "localhost"

    # Create a Telnet object.
    tn = telnetlib.Telnet(host, port)

    # Get the auth token.
    auth_token = os.popen('cat ~/.emulator_console_auth_token').read().strip()

    # Send the auth command.
    tn.write(f"auth {auth_token}\n".encode('ascii'))

    # Return the Telnet object.
    return tn

def close_connection(tn):
    # Close the Telnet connection.
    tn.close()

def receive_sms(tn, phone_number, message):
    # Send the sms send command.
    #tn.write(f"sms send {phone_number} {message}\n".encode('ascii'))
    # Encode the message as Unicode
    #print("unicode")
    #m2 = message.encode('ascii').decode('utf-8')
    #print(m2, "utf")
    unicode_message = message.encode('unicode_escape').decode('utf-8')
    #print(unicode_message)

    # Send the sms send command with the Unicode message.
    tn.write(f"sms send {phone_number} {unicode_message}\n".encode('ascii'))

tn = open_connection(5554)
#receive_sms(tn, '1234567890', 'm1')
#receive_sms(tn, '1234567890', "\u2653")

close_connection(tn)

def send_sms(from_number, message):
    # Construct the ADB command
    adb_command = f'adb emu sms send {from_number} "{message}"'

    # Run the ADB command
    subprocess.call(adb_command, shell=True)

# Example usage
send_sms("1234567890", "sms send admu emu ♓️")
send_sms("1234567890", "Character A: Hey, did you hear abo😬ut Sarah and Mark?")

#adb emu sms send "1234567890" "sms send admu emu ♓️"

#adb emu sms send "1234567890" "sms send admu emu \uDE0A"