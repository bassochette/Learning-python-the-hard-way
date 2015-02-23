#!/usr/bin/python

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54
weight = 180 # lbs
weight_k = (weight * 453.592) / 1000
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." %weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % ( eyes, hair)
print "His teeth are usually  %s depending on the coffe." % teeth

print "He is %5.2f kilograms and %3.0f" % (weight_k, height_cm)
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)
