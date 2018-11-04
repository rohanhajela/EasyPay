import os
#import sendsms
import subprocess
import venmopush
file = open('response.json','r')

line1 = file.readline()
data = eval(line1)

text = data["text"][0]
##charge 1 14085042986
#text = '#billpay 20 15106485141 14085042986 14088939075'
sender = data["msisdn"][0]
command = text.split(" ")

all_functions = ['#charge', '#split', '#billpay']
function, amount, users, message_array, message = '', '', [], [], ''

new_data = []
venmo_database = {"Andy": 15103585981}


def parse_NLU():
    global new_data
    #Change 1st Line
    parameter = open('parameters.json', 'r')
    cur = parameter.readlines()
    #print(cur[1])
    cur[1] = cur[1][:13] + data["text"][0] + '",' + "\n"
    #print(cur[1])
    parameter.close()

    #Update ResponseJson
    parameter = open('parameters.json', 'w')
    parameter.writelines(cur)
    parameter.close()

    command = 'curl -X POST \
    -H "Content-Type: application/json" \
    -u "apikey:a3jHgMchnTE0W1ZIH3IemDKNUZpuqq6D3_4345HXkLVZ" \
    -d @parameters.json \
    "https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-03-19"'
    output = subprocess.check_output(command, shell=True)
    output = eval(output)
    user = output["entities"][0]["text"]
    user = venmo_database.get(user, 0)
    function = output["entities"][1]["text"]
    if function == "owe":
        function = "#charge"
    elif function == "pay":
        function = "#charge"
    amount = output["entities"][2]["text"]
    if amount[:1] == "$":
        amount = amount[1:]
    reason = output["entities"][3]["text"]

    new_data = [function, amount, user, reason]

parse_NLU()
#print(new_data)

# parses through code, splits into the function, amount, users, and an optional message
def parse(command_array):
    global function, amount, message
    if command_array[0] in all_functions: #see if fn is not one of our pre-defined functions
        function = command_array[0]
    try:
        amount = (str(int(command_array[1])))
    except ValueError:
        print('error') #fix this
        #exit the function - display 'invalid amt'
    #amount = command_array[1] #see if this is a valid number - do try/catch later
    for elem in command_array[2:]:
        try:
            users.append(str(int(elem))) #make sure they are in order as well
        except ValueError:
            message_array.append(elem)
    for message_part in message_array:
        message += message_part + ' '
    if message == '':
        message = 'default'

parse(new_data)
#print(message)
venmopush.maketransaction(function, amount, users, message, sender)

file.close()
