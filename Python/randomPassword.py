#!usr/bin/env python3
#This is a random password generator

import random
import string

def random_password(length, allowLetters, allowNumbers, allowGrammer):
    letters = string.ascii_letters
    numbers = string.digits
    grammer = string.punctuation
    password = ""
    allowedCharacters = ""
    #Check to see what characters will be allowed in the password
    if allowLetters == 1 and allowNumbers == 1 and allowGrammer == 1:
        allowedCharacters = letters + numbers + grammer
    elif allowLetters == 1 and allowNumbers == 1 and allowGrammer != 1:
        allowedCharacters = letters + numbers
    elif allowLetters == 1 and allowNumbers != 1 and allowGrammer != 1:
        allowedCharacters = letters
    elif allowLetters == 1 and allowNumbers != 1 and allowGrammer == 1:
        allowedCharacters = letters + grammer
    elif allowLetters != 1 and allowNumbers == 1 and allowGrammer == 1:    
        allowedCharacters = numbers + grammer
    elif allowLetters != 1 and allowNumbers != 1 and allowGrammer == 1:
        allowedCharacters = grammer
    elif allowLetters != 1 and allowNumbers == 1 and allowGrammer != 1:
        allowedCharacters = numbers
    else:
        print("Sorry, can't make a password from nothing!")
    for x in range(length):
        password += "".join(random.choice(allowedCharacters))
    print("The random password of length", length, "is:", password)

    
length = int(input("Enter the length of your password: "))
allowLetters = int(input("Enter 1 if you want to allow lowercase and uppercase letters in the password: "))
allowNumbers = int(input("Enter 1 if you want to allow numbers in the password: "))
allowGrammer = int(input("Enter 1 if you want to allow grammer symbols in the password: "))
random_password(length, allowLetters, allowNumbers, allowGrammer)
