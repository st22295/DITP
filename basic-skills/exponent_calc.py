# x and y should be integers
# You cannot calculate exponents
# with non-integer bases or exponents

print("Hi, I would like to calculate x to the power of y for you.")

x = int(input("What is x: "))
y = int(input("What is y: "))

answer = x**y

print("{} to the power of {} is {}".format(x, y, answer))
