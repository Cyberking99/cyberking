#Program to find the area of a circle
#Formular used A=πr²

#import maths module
import math

#Accept input for the value of the radius (r)
radius = float(input("What is the radius of the circle?\n"))

#Declare the formular for finding the area
area = math.pi * radius**2

#Show the answer (area of the circle)
print("The area of the circle with radius ",radius," is ",area)