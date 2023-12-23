#!/usr/bin/python
import sys
def print_array():
    print(sys.argv)
    a = input("What is the array?")
    print("the first parameter is ", a[0])
    print("the second parameter is ", a[1])
    print("the third parameter is ", a[2])
    print("we have",len(sys.argv)-1,"parameters")

print_array()
