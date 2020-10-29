class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
import time
import os

"""
Kyle's password is kyleiscool
Shekar's password is thegoa
David's password is penspinner
colin's password is iamcolin
devam's password is mrscrummaster
GUEST's password is GUEST
"""

master_password="chessiscool"
username_credentials=["Kyle", "Shekar", "GUEST"]
def username_give():
  print("Please enter username: "+"\nType GUEST to use guest account")
def password_give():
  print("Please enter password: "+"\nType GUEST to use guest account")
z=1
y=True
x=False
w=False
username_give()
username_input=input("")
while(username_input not in username_credentials):
  if(z==1):
    print(bcolors.FAIL+bcolors.BOLD+"invalid"+bcolors.ENDC)
    username_give()
    username_input=input("")
    if(username_input in username_credentials):
      password_give()
      password_input=input("")
      if(password_input=="kyleiscool")and(username_input=="Kyle"):
        x=True
      if(password_input=="thegoat")and(username_input=="Shekar"):
        x=True
      if(password_input=="GUEST")and(username_input=="GUEST"):
        x=True
      y=False
      while(x==False):
        print(bcolors.FAIL+bcolors.BOLD+"invalid"+bcolors.ENDC)
        password_give()
        password_input=input("")
        y=False
        if(password_input=="kyleiscool")and(username_input=="Kyle"):
          x=True
        if(password_input=="thegoa")and(username_input=="Shekar"):
          x=True
        if(password_input=="GUEST")and(username_input=="GUEST"):
          x=True
if(y==True):  
  password_give()
  password_input=input("")
  x=False
  if(password_input=="kyleiscool")and(username_input=="Kyle"):
    x=True
  if(password_input=="thegoat")and(username_input=="Shekar"):
    x=True
  if(password_input=="GUEST")and(username_input=="GUEST"):
    x=True
  while(x==False):
    print(bcolors.FAIL+bcolors.BOLD+"invalid"+bcolors.ENDC)
    password_give()
    password_input=input("")
    if(password_input=="kyleiscool")and(username_input=="Kyle"):
      x=True
    if(password_input=="thegoat")and(username_input=="Shekar"):
      x=True
    if(password_input=="GUEST")and(username_input=="GUEST"):
      x=True

print(bcolors.OKGREEN+bcolors.BOLD+"SUCCESSFULLY LOGGED IN"+bcolors.ENDC)
if(password_input=="GUEST"):
  print(bcolors.OKGREEN+"You are using temporary guest account"+bcolors.ENDC)
  w=True
if(w==False):
  print(bcolors.OKGREEN+"Hello "+username_input+bcolors.ENDC)
time.sleep(2)
os.system("clear")
