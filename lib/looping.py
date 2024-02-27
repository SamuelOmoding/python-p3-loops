#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")
happy_new_year()
pass

def square_integers(int_list):
    int_list = [nums ** 2 for nums in int_list]
    return int_list
print(square_integers([4, 10, 30, 13, 500]))
pass

def fizzbuzz():
    for nums in range(1, 101):
        if(nums % 3 == 0 and nums % 5 == 0 ):
            print("FizzBuzz")
        elif nums % 3 == 0:
            print("Fizz")
        elif nums % 5 == 0:
            print ("Buzz")
        else:
            print (nums)

fizzbuzz()  
