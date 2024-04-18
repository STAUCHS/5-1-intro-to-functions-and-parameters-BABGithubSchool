#-------------------------------------------------------------------------
# Name:		    Lesson 5.1 Intro to Functions & Parameters
# Purpose:		Example #1
# Author:		Bassias. B
# Created:		18/04/2024
#-------------------------------------------------------------------------

# Example #1:
## Part (a) Create a function that will calculate the area of a rectangle

def rectangle_area():
    length = float(input("Input the length: "))
    width = float(input("Input the width: "))

    area = length * width

    print(f"The area of your rectangle is {area} cm^2.")

## Part (b) Use your function by calling it

rectangle_area()
