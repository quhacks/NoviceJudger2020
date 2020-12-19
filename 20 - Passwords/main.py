import sys

accounts = {} #a dictionary for username/password pairs

registrations = sys.stdin.readline()
for i in range(int(registrations)):
    username, password = sys.stdin.readline().split()
    if username in accounts: #if the username is already registered, it's bad
        print('Bad Username')
    else: #otherwise, register it
        accounts[username] = password
        print('Success')

print() #blank line for clarity

logins = sys.stdin.readline()
for i in range(int(logins)):
    username, password = sys.stdin.readline().split()
    if username not in accounts: #if the username is not registered, it's bad
        print('Bad Username')
    else: #otherwise, check the password
        print('Success' if accounts[username] == password else 'Bad Password') #python lets you use if statements as expressions