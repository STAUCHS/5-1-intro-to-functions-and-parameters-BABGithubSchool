#-------------------------------------------------------------------------
# Name:		    Lesson 5.1 Intro to Functions & Parameters
# Purpose:		Example #2
# Author:		Bassias. B
# Created:		18/04/2024
#-------------------------------------------------------------------------

# Example #1:
## Part (a) Create a function that will check if a number is even or odd

def even_or_odd(num = int(input("Enter a number: "))):
    if num == 0:
        print("Zero is neither even nor odd.")
    elif (num % 2) == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

## Part (b) Use your function by calling it

even_or_odd()