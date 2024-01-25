# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
""" Write a program that would allow to enter and store in variables of the appropriate data types:
-- Name
-- Email
-- Address of the origin
-- Address of the destination
-- Whether you need a car seat
(Taxi app)
Our goal is to get the input
track them into correct data types

Primitive data types: 
    strings (text, words, letters, numbers)
    integer (2, 16, 17, 534. 1000000023), float (12, 12.34, 324.567323)
    boolean(0 or 1, True or False)
    Null


Other data types:
    list = ["a","b", "c", "d"]
    dictionary
    tuples = ["a","b", "c", "d"]
    sets
"""


name = input("Enter your name: ") #string
email = input("Enter your email: ") #string
origin = input("where do you want to be picked up from? ") #string
destination = input("What is your destination address? ") #string
carseat = input("Do you need a car seat (y/n)? ") #boolean data type y = 1 and n = 0
if carseat == "n":
    require_carseat = False
else:
    require_carseat = True
user_info = [name, email, origin, destination, require_carseat]
print(user_info)


data_store = []

updated = data_store.append(user_info)
print("Here is the update", updated)




"""
print(type(user_info))
print(user_info)
print(name, email, origin, destination, require_carseat)
print(type(name), type(email), type(origin), type(destination), type(require_carseat))
"""