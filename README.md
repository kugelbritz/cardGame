# cardGame
Francois
Card Game


Goals:
Create a program database that mimics a deck of cards and keeps track of their locations. Have all cards start in the deck and write a function to assign the cards to player, computer and deck. A secondary function should print the location of each card and the cards each player has.


Input: 
Create card objects and randomize the doling out of cards. Input the number of cards per hand as to make sure that each player does not hold more than five cards at any given time.


Output: 
Output a list of card locations including the suit, number and color. 
Output a list of the cards that each player is holding.


Steps:
Define all needed functions as called from the function main (assignCard, showDeck, clearDeck, CardName, showHand)
Assign each card to a participant
Name the cards using modulus 13 and integer division to go through the playerName and suitName and name the cards in order.
Print the deck as called (0 - 51) and translate the random locations from 0,1 and 2 to deck, player and computer respectively.
Clear the deck by resetting all the locations to zero (deck)
Show Hand by reading each cards location and printing the card name as it relates to each participant (player or computer).
Format so it looks pretty and call the main after all definitions
