import os
file = open('response.json','r')

line1 = file.readline()
data = eval(line1)

# text = data["text"][0]
# command = text.split(" ")

# format of a command: 'Split 40 1234567890 5105101234 4081234789'
text = '#split 40 15106485141 14085042986 14088939075'
command = text.split(" ")
if command[0] == '#split':
    amount = command[1]
    users = command[2:]
    for user in users:
        msg = 'venmo charge ' + user + ' ' + str(round(int(amount)/(len(users)+1), 2)) + " 'for beers brooo'" #switch to manual message later
        print(msg)
        os.system(msg)
    # print("Splitting " + text[6:])
    # total = float(text[6:])
    # print(total/4)

if command[0] == 'Request':
    amount = command[1]
    user = command[2]
    str = 'venmo charge ' + user + ' ' + amount + ' thanks'
    print(str)
    os.system(str)
