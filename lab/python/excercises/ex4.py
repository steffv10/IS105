#Sets how many cars there are
cars = 100

#It shouldt matter if you put space_in_a_car as a floating point or an integer
#Since there cannot be a .XX spot in a car
#The car got integer value spots in it.

#Defines the spaces in one car
# space_in_a_car = 4.0
space_in_a_car = 4

#Sets how many drivers there will be
drivers = 30

#Sets how many passengers it is
passengers = 90

#Tells you how many empty cars there are
cars_not_driven = cars - drivers

#Tells us how many cars that are driven
cars_driven = drivers

#Tells us how many people that can be transported that day
carpool_capacity = cars_driven * space_in_a_car

#Tells us how many people we have to fit in each car 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars aviable."
print "There are only", drivers, "drivers aviable."
print "There will be", cars_not_driven, "empty cars today."
print "We  can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#The reason why he got the error was because he did not define the variable car_pool_capacity
#On my line 7 you can see the variable has been defined

i = 5
j = 5
print "J + I equals ",j + i
