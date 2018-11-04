import os

#calls functions in venmopush
def maketransaction(function, amount, users, message):
    if function == '#charge' and len(users) == 1:
        charge(amount, users)
    elif function == '#charge' and len(users) > 1:
        chargemultiple(amount, users)
    elif function == '#split':
        split(amount, users)

# format of command: '#charge 5 15106485141'
def charge(amount, user):
    str = 'venmo charge ' + user[0] + ' ' + amount + ' thanks'
    #output = subprocess.check_output(str, shell=True)
    print(str)
    os.system(str)
    #sendsms.send(sender, output)

# format of command: '#charge 20 15106485141 14085042986 14088939075'
def chargemultiple(amount, users):
    for user in users:
        charge(amount, user)

# format of a command: '#split 40 15106485141 14085042986 14088939075'
def split(amount, users):
    chargemultiple(round(int(amount)/(len(users)+1), 2), users)
    # for user in users:
    #     msg = 'venmo charge ' + user + ' ' + str(round(int(amount)/(len(users)+1), 2)) + " 'for beers brooo'" #switch to manual message later
    #     print(msg)
    #     os.system(msg)
