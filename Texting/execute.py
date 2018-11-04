import os
import sendsms
import subprocess
file = open('response.json','r')

line1 = file.readline()
data = eval(line1)

text = data["text"][0]
sender = data["msisdn"][0]
command = text.split(" ")

"""if text[:5] == 'Split':
    print("Splitting " + text[6:])
    total = float(text[6:])
    print(total/4)"""

if command[0] == 'Request':
    value = command[1]
    number = command[2]
    str = "venmo charge " + str(number) + ' ' + str(value) + " thanks"
    output = subprocess.check_output(str, shell=True)
    print(output)
    sendsms.send(sender, output)

file.close()
