# Created on July 26th
# Felix Guerrero
# Exercise 4 - Variables and Names  - Learn python the hard way.

#Defining Variables
cars = 100
space_in_a_car = 4 
drivers = 30
passengers = 90

# Variables Calculations
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#Output of variables
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."
