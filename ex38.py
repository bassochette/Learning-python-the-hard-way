#!/usr/bin/python

then_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wiat there not 10 things in that list. Let's fix that."

stuff = then_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10 :
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "Ther are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # What???? Coool!!!!
print '#'.join(stuff[3:5]) # super stellar!!!
