num1 = int(input("First num: "))
num2 = int(input("Second num: "))

sum = num1 + num2

print("{} + {} = {}".format(num1, num2, sum))

# We need to convert the input value into an integer
# because it was a string by defualt.

# Another way to add numbers by using a function
def add(num1, num2) -> int:
    return num1 + num2

print (add(70, 90))

















