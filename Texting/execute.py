import os
file = open('response.json','r')

line1 = file.readline()
data = eval(line1)

text = data["text"][0]
command = text.split(" ")

if command[0] == 'Split':
    value = command[1]
    users = command[2:]
    for user in users:
        str = 'venmo charge ' + str(user) + ' ' + str(round(amount/(len(users)-1), 2)) + ' nb' #switch to manual message later
        print(str)
        os.system(str)
    # print("Splitting " + text[6:])
    # total = float(text[6:])
    # print(total/4)

if command[0] == 'Request':
    amount = command[1]
    user = command[2]
    str = 'venmo charge ' + str(user) + ' ' + str(amount) + ' thanks'
    print(str)
    os.system(str)
