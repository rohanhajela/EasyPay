import os
#import sendsms
#import subprocess
import time

#calls functions in venmopush
def maketransaction(function, amount, users, message):
    if function == 'Charge' and len(users) == 1:
        charge(amount, users[0], message)
    elif function == 'Charge' and len(users) > 1:
        chargemultiple(amount, users, message)
    elif function == '#split':
        split(amount, users, message)
    elif function == '#billpay':
        periodicpay(amount, users, message)

# format of command: '#charge 5 15106485141'
def charge(amount, user, message):
    str = 'venmo charge ' + user + ' ' + amount + ' ' + message
    #output = subprocess.check_output(str, shell=True)
    print(str)
    os.system(str)
    #sendsms.send(sender, output)

# format of command: '#charge 20 15106485141 14085042986 14088939075'
def chargemultiple(amount, users, message):
    for user in users:
        charge(amount, user, message)

# format of a command: '#split 40 15106485141 14085042986 14088939075'
def split(amount, users, message):
    chargemultiple(round(int(amount)/(len(users)+1), 2), users, message)
    # for user in users:
    #     msg = 'venmo charge ' + user + ' ' + str(round(int(amount)/(len(users)+1), 2)) + " 'for beers brooo'" #switch to manual message later
    #     print(msg)
    #     os.system(msg)

# format of a command: '#billpay 20 15106485141 14085042986 14088939075
def periodicpay(amount, users, message):
    for _ in range(2):
        chargemultiple(amount, users, message)
        time.sleep(15)
