"""
cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

def main():
  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  showDeck()
  showHand(PLAYER)
  showHand(COMP)

def assignCard(user):
    randomCard = randint(0,51)
    cardLoc[randomCard] = user

def CardName(num):
        return("{} of {}" .format(rankName[num % 13],suitName[num // 13]))

def clearDeck():
    for i in range(NUMCARDS):
        cardLoc[i] = 0

def showDeck():
    print("{:^20}{:^20}{:^20}\n".format("#", "Card", "Location"))
    for i in range(NUMCARDS):
        print("{:^20}{:^20}{:^20}\n".format(str(i), CardName(i), playerName[cardLoc[i]]))

def showHand(participant):
    print("\nDisplaying {} hand:\n" .format(playerName[participant]))
    for i in range(NUMCARDS):
        if cardLoc[i] == participant:
            print ("{}" .format(CardName(i)))



main()
