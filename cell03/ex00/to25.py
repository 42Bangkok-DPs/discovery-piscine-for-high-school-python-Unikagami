#!/usr/bin/env python3

number = int(input("enter the number less than 25 : "))
if number > 25 :
    print("Error")
while number < 26 :
    print("Inside the loop, my variable is" + " " + str(number))
    number += 1
