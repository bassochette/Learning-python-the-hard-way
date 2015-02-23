#!/usr/bin/python
import random

# Varaibles
colors = ['Coeur', 'Pique', 'Trefle', 'Carreau']
cards = ['1', '2', '3', '4', '5', '6', '7', '8', '10', 'V', 'D', 'R']
listOfCards = []
deckSize = 52
deck = {}

# init lists
for c in colors:
    for ca in cards:
        listOfCards.append("%s%s" % (ca, c))
print "List des cartes prete: ", listOfCards
for i in range(0, deckSize):
    #print "initialisation de l'adresse %d" % i
    deck[i] = "None"

def setCard(d):
    r = random.randint(0, deckSize - 1)
    print "Setting up card to address %r" % r
    if d[r] == "None" :
        newCard = listOfCards.pop()
        print "address %d has card %s" % (r, newCard)
        d[r] = newCard
    elif len(listOfCards) == 0:
        return 0
    else:
        print "Addresse deja attribue"
        setCard(d)
def asNone(d):
    for key in d.keys():
        if d[key] == "None":
            return True

    return False


inited = False
while inited == False :
    print "Calling set card"
    if asNone(deck):
        setCard(deck)
    else:
        print "No none in deck"
        inited = True

print deck


