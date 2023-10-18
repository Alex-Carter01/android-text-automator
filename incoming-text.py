import telnetlib
import os

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

def send_sms(tn, phone_number, message):
    # Send the sms send command.
    tn.write(f"sms send {phone_number} {message}\n".encode('ascii'))

tn = open_connection(5554)
send_sms(tn, '1234567890', 'm1')
send_sms(tn, '1234567890', 'm2')
send_sms(tn, '1234567890', 'm3')
#send_sms(tn, '0987654321', 'Goodbye, World!')
close_connection(tn)