# Number of cars
cars = 100

# Amount of space in a car (we could use an integer here in this case)
space_in_a_car = 4.0

# Total number of drivers
drivers = 30

# Total number of passengers
passengers = 90

# Number of cars not driven
cars_not_driven = cars - drivers

# Number of cars driven
cars_driven = drivers

# Total capacity in the car pool
carpool_capacity = cars_driven * space_in_a_car

# The average number of passengers in a car.
average_passengers_in_a_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passengers_in_a_car, "in each car."
