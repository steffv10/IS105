
#Defines variables
x ="There are %d types of people." %10
binary = "binary"
do_not = "Dont"
y = "Those who know %s and those who %s." % (binary, do_not)
#Prints variable X and Y 
print x
#Got string inside string *1/4*
print y

#Got string inside string *2/4*
print "I said: %r." % x
#Got string inside a string *3/4*
print "I also said: '%s'." %y

#Creates a variable False
hilarious = False
#Variable for evaluating the joke
joke_evaluation = "Isnt that joke so funny?! %r"

#One might think this got string inside string but False is boolean and not a string
#prints the evaluation
print joke_evaluation %hilarious

#Defines two String variables
w = "This is the left side of..."
e = "a string with a right side."

#Prints two variables added together
#String inside a string *4/4*
print w + e
#There are two strings, ofc adding them together would make it a longer string...
