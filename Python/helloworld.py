#!/usr/bin/env python3

#This is a hello world script to
#demonstrate python
#Created by Mat Neyers on 01/10/22
name = input("Enter your name:")
currentYear = input("Enter the current year: ")
yearBorn = input("Enter the year you were born: ")
age = int(currentYear) - int(yearBorn)
print("Hello " + name + ", you are " + str(age) + " years old.")
