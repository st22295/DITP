# Rounding

'''

gst = 0.15
item = float(input("Enter item price: $"))
item_gst = item * gst
total_cost = item + item_gst
print("Total cost: {}".format(round(total_cost)))

gst = 0.15
item = float(input("Enter item price: $"))
item_gst = item * gst
total_cost = item + item_gst
print("Total cost: {}".format(round(total_cost, 2)))

print('\n')



# Square Root - sqrt()

from math import sqrt

print(sqrt(9))
print(sqrt(6+19))
print(sqrt(12*3))

square =  int(input("Which number should I calculate the square root of? "))
print("The square root of {} is {}".format(square, sqrt(square)))

square = int(input("Which number should I calculate the square root of? "))
print("The square root of {} is {}".format(square, round(sqrt(square), 2)))



# Pi

from math import pi

diameter = int(input("What is the diameter of the circle? "))
print("The circumference of the circle is {}".format(pi * diameter))

diameter = int(input("What is the diameter of the circle? "))
print("The circumference of the circle is {}".format(round(pi * diameter,2)))

'''

# Exercises

#7

side_a = int(input("What is the length of the first side, a? "))
side_b = int(input("What is the lengthog the second side, b? "))
# hypotenuse_length = 

# print("The length of the hypotenuse is {}".format(hypotenuse_length))























