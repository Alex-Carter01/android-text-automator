from uiautomator import device as d
import time

#debug
#export ANDROID_HOME=/Users/alexcarter/Library/Android/sdk

#(0,658) > (720,1088)
#column_width = 72
#row_height = 86

#list top, left corner coordinate
coord_map = {
'q': [0,751], 'w': [72,751], 'e': [72*2,751], 'r': [72*3,751], 't': [72*4,751], 'y': [72*5,751], 'u': [72*6,751], 'i': [72*7,751], 'o': [72*8,751], 'p': [72*9,751],
'a': [0+36,751+86], 's': [72+36,751+86], 'd': [72*2+36,751+86], 'f': [72*3+36,751+86], 'g': [72*4+36,751+86], 'h': [72*5+36,751+86], 'j': [72*6+36,751+86], 'k': [72*7+36,751+86], 'l': [72*8+36,751+86],
'z': [72+36,751+86*3], 'x': [72*2+36,751+86*3], 'c': [72*3+36,751+86*3], 'v': [72*4+36,751+86*3], 'b': [72*5+36,751+86*3], 'n': [72*6+36,751+86*3], 'm': [72*7+36,751+86*3],
',': [72+36,751+86*4], ' ': [72*4+36,751+86*4], '.': [72*7+36,751+86*4],
'1': [0,751], '2': [72,751], '3': [72*2,751], '4': [72*3,751], '5': [72*4,751], '6': [72*5,751], '7': [72*6,751], '8': [72*7,751], '9': [72*8,751], '0': [72*9,751],
'@': [0+36,751+86], '#': [72+36,751+86], '$': [72*2+36,751+86], '%': [72*3+36,751+86], '&': [72*4+36,751+86], '-': [72*5+36,751+86], '+': [72*6+36,751+86], '(': [72*7+36,751+86], ')': [72*8+36,751+86],
'*': [72+36,751+86*3], '"': [72*2+36,751+86*3], '\'': [72*3+36,751+86*3], ':': [72*4+36,751+86*3], ';': [72*5+36,751+86*3], '!': [72*6+36,751+86*3], '?': [72*7+36,751+86*3],
}

num_list = {'@', '#', '$', '%', '&', '-', '+', '(', ')',
'*', '"', '\'', ':', ';', '!', '?',
}

def press_shift():
    x = 0
    y = 751+86*3
    x += 36
    y += 43
    d.click(x, y)

def press_num():
    x = 0
    y = 751+86*4
    x += 36
    y += 43
    d.click(x, y)

def type_message(message):
    text_editor = d(resourceId="com.android.mms:id/embedded_text_editor")
    shift_state = True
    first_pass = True
    #add caps loc, special characters
    #for c in message:
    for pos in range(len(message)):
        c = message[pos]
        if c.isalpha():
            #print(c, shift_state, c.islower(), c.isupper())
            if c.islower() and shift_state:
                press_shift()
                shift_state = False
                if pos == 0:
                    shift_state = False
                    first_pass = False
            elif c.isupper() and not shift_state:
                if pos < len(message) - 1 and message[pos + 1].isupper():
                    press_shift()
                    shift_state = True
                press_shift()
            elif pos == 0 and c.isupper() and pos < len(message) - 1 and message[pos + 1].isupper():
                print("weiird")
                press_shift()
                time.sleep(0.2)
                press_shift()
                press_shift()
            x = coord_map[c.lower()][0]
            y = coord_map[c.lower()][1]
            #offset to key center                
            x += 36
            y += 43
            d.click(x, y)
        elif c in {' ', ',', '.'}:
            x = coord_map[c][0]
            y = coord_map[c][1]
            #offset to key center                
            x += 36
            y += 43
            d.click(x, y)
        elif c in num_list:
            press_num()
            x = coord_map[c][0]
            y = coord_map[c][1]
            #offset to key center                
            x += 36
            y += 43
            d.click(x, y)
            press_num()
        elif c == '\n':
            d(resourceId="com.android.mms:id/send_button_sms").click()
        else:
            text_editor.set_text(message[:pos+1])
        if pos == 0:
            first_pass = False
        

    # Click on the send button.
    d(resourceId="com.android.mms:id/send_button_sms").click()



#misceelaneous ADB UI things

# Open the messaging app.
#d(text="Messaging").click()

# Click on the new message button.
#d(description="New message").click()

# Enter the phone number.
#d(resourceId="com.android.mms:id/recipients_editor").set_text('1234567890')

# Enter the message.
#d(resourceId="com.android.mms:id/embedded_text_editor").set_text('Hello, World!')

# Get the reference to the text editor element
#text_editor = d(resourceId="com.android.mms:id/embedded_text_editor")

# Clear the existing text in the text editor
#text_editor.clear()