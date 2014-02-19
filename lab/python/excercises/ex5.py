name ='Steffen U. Vetrhus'
age = 25 #Its true
height = 193 #Centimeters
weight = 95 #Kilograms
# Converts weight from KG to Pounds
weight_in_pounds = weight * 2

# Converts height from CM to Inches
height_in_inches = height * 0.4
eyes = 'Blue'
teeth = 'White'
hair = 'I dont have hair duh!'

print "Lets talk about %s." % name
print "Hes %d cm tall." % height
print "Hes %d kg heavy." % weight
print "Hes %d pounds heavy." % weight_in_pounds
print "He is %d inches tall." % height_in_inches
print "Actually that is about the normal weight for him."

#%R prints out the variable in its raw format, exactly or close to exactly as it was written
print "His got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


#This line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (age, weight, height, age + height + weight)


