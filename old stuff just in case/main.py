import pygame
from check import Player
from check import Deck
from check import Card










# write a program that plays a game of 5 card draw and checks
# for the best hand
#
def main():
    decks = {
        "wild_royal_flush": [Card("Hearts", 2), Card("Spades", 10), Card("Spades", 11), Card("Spades", 12), Card("Spades", 13)],
        "four_deuces": [Card("Hearts", 2), Card("Spades", 2), Card("Diamonds", 2), Card("Clubs", 2), Card("Spades", 10)],
        "natural_royal_flush": [Card("Hearts", 10), Card("Hearts", 11), Card("Hearts", 12), Card("Hearts", 13), Card("Hearts", 1)],
        "five_of_a_kind": [Card("Hearts", 4), Card("Spades", 4), Card("Diamonds", 4), Card("Clubs", 4), Card("Hearts", 2)],
        "straight_flush": [Card("Hearts", 4), Card("Hearts", 5), Card("Hearts", 6), Card("Hearts", 7), Card("Hearts", 8)],
        "four_of_a_kind": [Card("Hearts", 4), Card("Spades", 4), Card("Diamonds", 4), Card("Clubs", 4), Card("Hearts", 3)],
        "full_house": [Card("Hearts", 4), Card("Spades", 4), Card("Diamonds", 3), Card("Clubs", 3), Card("Hearts", 3)],
        "flush": [Card("Hearts", 4), Card("Hearts", 5), Card("Hearts", 13), Card("Hearts", 7), Card("Hearts", 8)],
        "straight": [Card("Hearts", 4), Card("Spades", 5), Card("Diamonds", 6), Card("Clubs", 7), Card("Hearts", 8)],
    }
    deck = Deck()
    player1 = Player("Nick")

    player1.hand = decks["natural_royal_flush"]

    player1.show()
    player1.check()
    print('')

    player1.hand = decks["four_deuces"]
    player1.show()
    player1.check()
    print("")
    player1.hand = decks["wild_royal_flush"]
    player1.show()
    player1.check()
    print("")
    player1.hand = decks["five_of_a_kind"]
    player1.show()
    player1.check()
    print("")
    player1.hand = decks["straight_flush"]
    player1.show()
    player1.check()
    print("")
    player1.hand = decks["four_of_a_kind"]
    player1.show()
    player1.check()
    print("")
    player1.hand = decks["full_house"]
    player1.show()
    player1.check()
    print("")
    player1.hand = decks["flush"]
    player1.show()
    player1.check()
    print("")
    player1.hand = decks["straight"]
    player1.show()
    player1.check()




    # write a bunch of decks
    

main()



# game loop
# get our 5 cards
# allow the player to hold and roll again
#       case where they don't hold
# check the 5 cards after the second roll
# update balances
# replay



