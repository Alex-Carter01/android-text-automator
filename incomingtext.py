import subprocess

def escape_emojis(text):
    def unicode_to_utf16_surrogate(unicode_code_point):
        # Subtract 0x10000 from the Unicode code point
        value = unicode_code_point - 0x10000

        # Calculate the high and low surrogates
        high_surrogate = 0xD800 + ((value & 0xFFC00) >> 10)
        low_surrogate = 0xDC00 + (value & 0x003FF)

        # Convert the surrogates to Unicode escape sequences
        high_surrogate_str = '\\u' + format(high_surrogate, '04x')
        low_surrogate_str = '\\u' + format(low_surrogate, '04x')

        # Return the surrogate pair
        return high_surrogate_str + low_surrogate_str

    result = ''
    for char in text:
        if ord(char) > 0xFFFF:
            result += unicode_to_utf16_surrogate(ord(char))
        else:
            result += char
    return result

def receive_sms(from_number, message):
    message = escape_emojis(message)

    # Construct the ADB command
    adb_command = f'adb emu sms send {from_number} "{message}"'

    # Run the ADB command
    subprocess.call(adb_command, shell=True)