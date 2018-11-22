#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : format.py
# Date              : 21.11.2018
# Last Modified Date: 21.11.2018
#  format格式化函数

# Python3 program to demonstarte
# the str.format() method

# using format option in a simple string
print("{}, A computer science portal for geeks.".format("GeeksforGeeks"))

# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))

# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))

#  多个参数
#  Syntax : { } { } .format(value1, value2)
#  IndexError: list index out of range错误
my_string = "{}, is a {} {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))

# Python program using multiple place
# holders to demonstrate str.format() method
# Multiple placeholders in format() function
my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))

# different datatypes can be used in formatting
print("Hi ! My name is {} and I am {} years old".format("User", 19))
# The values passed as parameters
# are replaced in order of their entry
print("This is {} {} {} {}".format("one", "two", "three", "four"))
