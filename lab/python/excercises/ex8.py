formatter = "%r %r %r %r"
#Formatter %r prints out the "Raw format" of the variables
#The reason why ' and " comes up in one of the sentences is that
#The word Didn't already contains the standard ' notation so it changes this
#to " 

print formatter %(1, 2, 3, 4)
print formatter %("one", "two", "three", "four")
print formatter %(True, False, False, True)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %("I had this thing.", "That you could type up right", "But it didn't sing", "So I said goodnight") 
