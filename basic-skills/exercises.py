#Annia
#22/08/22

'''
# Task 1

giftcard = float(input("What value does your gift card have? "))
book = input("What is the name of the book you bought? ")
cost = int(input("How much is the book? "))

summary = giftcard-cost

print("You have ${} left in your giftcard.".format(summary))



# Task 2

weight = float(input("How many grams of flour do you have? "))
cups = weight/125

print("You have {} cups of flour.".format(cups))



# Task 3

height = float(input("What is your height in metres and centimetres? "))
inches = height * 39.37

feet = inches / 12

print("Your height in inches is {} inches.".format(inches))
print("Your height in feet and inches is {} feet.".format(feet))

print("Your height in inches is" %inches" inches.")
print("Your height in feet and inches is" %feet" feet.")

# Task 3B

print("Your height in feet and inches is {} feet.".format(round(feet, 2)))



# Task 4

purchases = float(input("Wha is the dollar value of your purchase? "))
gst = purchases * .15
gstincl = purchases + gst

print("Your purchase price is ${}".format(purchases))
print("Your gst to be added is ${}".format(gst))
print("The amount to pay including gst is ${}".format(gstincl))

print()

purchase = float(input("What is the dollar value of your purchase? "))
gst = purchase * 15
gstincl = purchase * gst

print("Your purchase price is $" "%.2f" %purchase)

'''
seats = 3000
taxi = 95
taxi_full = 4
bus = 45
bus_full = 40
    
remaining = seats - (taxi_full + bus_full)
print("The number of people left at the stadium after transport has left is", remaining)

extra_bus = remaining//40
print("You will need to request", extra_bus + 1, " extra buses for a second trip.")

















