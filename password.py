import time
import os

'''
Notes for Shekar:
a) I made it so I can skip this cuz it was annoying to type it in every single time
b) if statements don't need parentheses around the arguments
c) when using a boolean, you don't have to say "== False" or "== True", 
   a simple "if boolean" or "if not boolean" will suffice
d) when you have an input, you can put something in the parentheses for it to print that thing,
   then take the input after it finishes printing. You don't have to define functions to print
   what you want printed for the input.
e) this thing runs twice for some reason
f) I'm not good at naming variables either, but things that you'll use multiple times should be named
   something better than "oogabooga" or "xyz"
g) probably set something up for new usernames/passwords
'''

OOGABOOGA = 1


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

username_credentials = ["Kyle", "Shekar", "GUEST", "GUEST", "Devam", "Colin", "David"]

"""
Kyle's password is kyleiscool
Shekar's password is thegoat
David's password is penspinner
Colin's password is java
Devam's password is scrummaster
GUEST's password is GUEST
"""


def password_code():
    password_input = ""

    z = 1
    y = True
    x = False
    w = False
    username_input = input("\nFirst authorized user is player 1 (white)\nSecond authorized user is player 2 (black)\nPlease enter username: \nType GUEST to use guest account: ")
    while username_input not in username_credentials:
        if z == 1:
            print(bcolors.FAIL + bcolors.BOLD + "invalid" + bcolors.ENDC)
            username_input = input("\nFirst authorized user is player 1 (white)\nSecond authorized user is player 2 (black)\nPlease enter username: \nType GUEST to use guest account: ")
            if username_input in username_credentials:
                password_input = input("Please enter password: \nType GUEST to use guest account: ")
                if (password_input == "kyleiscool") and (username_input == "Kyle"):
                    x = True
                if (password_input == "thegoat") and (username_input == "Shekar"):
                    x = True
                if (password_input == "GUEST") and (username_input == "GUEST"):
                    x = True
                if (password_input == "scrummaster") and (username_input == "Devam"):
                    x = True
                if (password_input == "java") and (username_input == "Colin"):
                    x = True
                if (password_input == "penspinner") and (username_input == "David"):
                    x = True
                y = False
                while not x:
                    print(bcolors.FAIL + bcolors.BOLD + "invalid" + bcolors.ENDC)
                    password_input = input("Please enter password: \nType GUEST to use guest account: ")
                    y = False
                    if (password_input == "kyleiscool") and (username_input == "Kyle"):
                        x = True
                    if (password_input == "thegoat") and (username_input == "Shekar"):
                        x = True
                    if (password_input == "GUEST") and (username_input == "GUEST"):
                        x = True
                    if (password_input == "scrummaster") and (username_input == "Devam"):
                        x = True
                    if (password_input == "java") and (username_input == "Colin"):
                        x = True
                    if (password_input == "penspinner") and (username_input == "David"):
                        x = True
    if y:
        password_input = input("Please enter password: \nType GUEST to use guest account: ")
        x = False
        if (password_input == "kyleiscool") and (username_input == "Kyle"):
            x = True
        if (password_input == "thegoat") and (username_input == "Shekar"):
            x = True
        if (password_input == "GUEST") and (username_input == "GUEST"):
            x = True
        if (password_input == "scrummaster") and (username_input == "Devam"):
            x = True
        if (password_input == "java") and (username_input == "Colin"):
            x = True
        if (password_input == "penspinner") and (username_input == "David"):
            x = True
        while not x:
            print(bcolors.FAIL + bcolors.BOLD + "invalid" + bcolors.ENDC)
            password_input = input("Please enter password: \nType GUEST to use guest account: ")
            if (password_input == "kyleiscool") and (username_input == "Kyle"):
                x = True
            if (password_input == "thegoat") and (username_input == "Shekar"):
                x = True
            if (password_input == "GUEST") and (username_input == "GUEST"):
                x = True
            if (password_input == "scrummaster") and (username_input == "Devam"):
                x = True
            if (password_input == "java") and (username_input == "Colin"):
                x = True
            if (password_input == "penspinner") and (username_input == "David"):
                x = True

    print(bcolors.OKGREEN + bcolors.BOLD + "PLAYER " + str(OOGABOOGA) + " SUCCESSFULLY LOGGED IN" + bcolors.ENDC)
    if password_input == "GUEST":
        print(bcolors.OKGREEN + "You are using temporary guest account" + bcolors.ENDC)
        w = True
    if not w:
        print(bcolors.OKGREEN + "Hello " + username_input + bcolors.ENDC)

    return username_input


def password_code2():
    password_input = ""

    z = 1
    y = True
    x = False
    w = False
    username_input2 = input("\nFirst authorized user is player 1 (white)\nSecond authorized user is player 2 (black)\nPlease enter username: \nType GUEST to use guest account: ")
    while username_input2 not in username_credentials:
        if z == 1:
            print(bcolors.FAIL + bcolors.BOLD + "invalid" + bcolors.ENDC)
            username_input2 = input("\nFirst authorized user is player 1 (white)\nSecond authorized user is player 2 (black)\nPlease enter username: \nType GUEST to use guest account: ")
            if username_input2 in username_credentials:
                password_input = input("Please enter password: \nType GUEST to use guest account: ")
                if (password_input == "kyleiscool") and (username_input2 == "Kyle"):
                    x = True
                if (password_input == "thegoat") and (username_input2 == "Shekar"):
                    x = True
                if (password_input == "GUEST") and (username_input2 == "GUEST"):
                    x = True
                if (password_input == "scrummaster") and (username_input2 == "Devam"):
                    x = True
                if (password_input == "java") and (username_input2 == "Colin"):
                    x = True
                if (password_input == "penspinner") and (username_input2 == "David"):
                    x = True
                y = False
                while not x:
                    print(bcolors.FAIL + bcolors.BOLD + "invalid" + bcolors.ENDC)
                    password_input = input("Please enter password: \nType GUEST to use guest account: ")
                    y = False
                    if (password_input == "kyleiscool") and (username_input2 == "Kyle"):
                        x = True
                    if (password_input == "thegoat") and (username_input2 == "Shekar"):
                        x = True
                    if (password_input == "GUEST") and (username_input2 == "GUEST"):
                        x = True
                    if (password_input == "scrummaster") and (username_input2 == "Devam"):
                        x = True
                    if (password_input == "java") and (username_input2 == "Colin"):
                        x = True
                    if (password_input == "penspinner") and (username_input2 == "David"):
                        x = True
    if y:
        password_input = input("Please enter password: \nType GUEST to use guest account: ")
        x = False
        if (password_input == "kyleiscool") and (username_input2 == "Kyle"):
            x = True
        if (password_input == "thegoat") and (username_input2 == "Shekar"):
            x = True
        if (password_input == "GUEST") and (username_input2 == "GUEST"):
            x = True
        if (password_input == "scrummaster") and (username_input2 == "Devam"):
            x = True
        if (password_input == "java") and (username_input2 == "Colin"):
            x = True
        if (password_input == "penspinner") and (username_input2 == "David"):
            x = True
        while not x:
            print(bcolors.FAIL + bcolors.BOLD + "invalid" + bcolors.ENDC)
            password_input = input("Please enter password: \nType GUEST to use guest account: ")
            if (password_input == "kyleiscool") and (username_input2 == "Kyle"):
                x = True
            if (password_input == "thegoat") and (username_input2 == "Shekar"):
                x = True
            if (password_input == "GUEST") and (username_input2 == "GUEST"):
                x = True
            if (password_input == "scrummaster") and (username_input2 == "Devam"):
                x = True
            if (password_input == "java") and (username_input2 == "Colin"):
                x = True
            if (password_input == "penspinner") and (username_input2 == "David"):
                x = True

    print(bcolors.OKGREEN + bcolors.BOLD + "PLAYER " + str(OOGABOOGA) + " SUCCESSFULLY LOGGED IN" + bcolors.ENDC)
    if password_input == "GUEST":
        print(bcolors.OKGREEN + "You are using temporary guest account" + bcolors.ENDC)
        w = True
    if not w:
        print(bcolors.OKGREEN + "Hello " + username_input2 + bcolors.ENDC)


""""
def neworexisting():
  print("login with existing account or new account"+"\nenter NEW for new account and EXISTING for existing account")
  first_input=input("")
  if(first_input == "NEW"):
    account_state = False
  elif(first_input=="EXISTING"):
    account_state = True
  else:
    neworexisting()
  return(account_state)
account_state = neworexisting()
"""

#delete
skip = input("Skip?\n")
if skip != "y":
    #delete

    account_state = True
    if account_state:
        final_username = password_code()
        username_credentials.remove(final_username)
        OOGABOOGA = 2
        password_code2()
        print(bcolors.OKBLUE + bcolors.BOLD + "\nBOTH PLAYERS HAVE SUCCESSFULLY LOGGED IN" + bcolors.ENDC)
        time.sleep(2.5)
        os.system("clear")
    if not account_state:
        print("hi")
        time.sleep(5)