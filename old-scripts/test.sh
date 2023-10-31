#!/usr/bin/env bash
read -r -p "Enter string: " string    # prompt user to input string
string="${string// /%s}"              # replace spaces in string with '%s'
printf -v string "%q" "${string}"  
echo ${string}
adb emu sms send "5128377500" "${string}"