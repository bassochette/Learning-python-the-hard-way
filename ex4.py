#!/usr/bin/python

# we assign an integer to the variable car
cars = 100
# here we assign a floating decimal number to the variable space_in_a_car
space_in_a_car = 4.0
# assigning the integer 30 to the variable drivers
drivers = 30
# assign the inteher 90 to the variable passengers
passengers = 90
# assign the result of the operation: value of cars minus value of drivers
cars_not_driven = cars - drivers
# assign the value of the variable drivers to the variable cars_driven
cars_driven = drivers
# assign the result of the cars driven value(30) multiplied by space_in_a_car value(4.0), the result is a floating decimal number because space_in_a_car is a float which suplent the integer in cars_driven
carpool_capacity = cars_driven * space_in_a_car
# assign the value of the division between the value of passengers and the value of cars_driven
average_passengers_per_cars = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_cars, "in each car."
