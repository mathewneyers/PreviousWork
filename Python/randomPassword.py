#!usr/bin/env python3
#This is a random password generator

import random
import string

def random_password(length, allowLower, allowUpper, allowNumbers, allowGrammer):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    grammer = string.punctuation
    password = ""
    allowedCharacters = ""
    if allowLower == 1 and allowUpper == 1 and allowNumbers == 1 and allowGrammer == 1:
        allowedCharacters = lower + upper + numbers + grammer
    
    for x in range(length):
        password += "".join(random.choice(allowedCharacters))
    print("The random password of length", length, "is:", password)

    
length = int(input("Enter the length of your password: "))
allowLower = int(input("Enter 1 if you want to allow lowercase letters in the password: "))
allowUpper = int(input("Enter 1 if you want to allow uppercase letters in the password: "))
allowNumbers = int(input("Enter 1 if you want to allow numbers in the password: "))
allowGrammer = int(input("Enter 1 if you want to allow grammer symbols in the password: "))
random_password(length, allowLower, allowUpper, allowNumbers, allowGrammer)
