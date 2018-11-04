import os
import sendsms
import subprocess
import venmopush

file = open('response.json','r')

line1 = file.readline()
data = eval(line1)

text = data["text"][0]
sender = data["msisdn"][0]
command = text.split(" ")

all_functions = ['#charge', '#split']
function, amount, users, message_array, message = '', '', [], [], ''

# parses through code, splits into the function, amount, users, and an optional message
def parse(command_array):
    global function, amount, message
    if command_array[0] in all_functions: #see if fn is not one of our pre-defined functions
        function = command_array[0]
    try:
        amount = (str(int(command[1])))
    except ValueError:
        print('error') #fix this
        #exit the function - display 'invalid amt'
    #amount = command_array[1] #see if this is a valid number - do try/catch later
    for elem in command_array[2:]:
        try:
            users.append(str(int(elem)))
        except ValueError:
            message_array.append(elem)
    for message_part in message_array:
        message += message_part + ' '
    if message == '':
        message = 'default message'

parse(command)
venmopush.maketransaction(function, amount, users, message)

file.close()
