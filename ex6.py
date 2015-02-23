#!/usr/bin/python

# assigning a formatted string to x
x = "There are %d types of people." % 10
# assign a string to binary
binary = "binary"
# assign a string to do_not
do_not = "don't"
# assign a formatted string to y
y = "Those who know %s and those who %s." % (binary , do_not)

# display the value of x
print x
# display the value of y
print y

# display a string that include the value x
print "I said : %r." % x
# display a string that include the value of y between single quotes
print "I also said: '%s'. " % y

# assign a boolean to hilarious
hilarious = False
# assign a string with a fomatting option in it
joke_evaluation = "Isn't that joke so funny?! %r"

# display joke_evaluation concatanate to the value of hilarious
print joke_evaluation % hilarious

# assign a string to w
w = "This is the left side of..."
# assign a string to e
e = "a string with a right side."

# display the concatanation of w and e
print w + e
