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
        "three_of_a_kind": [Card("Hearts", 4), Card("Spades", 4), Card("Diamonds", 4), Card("Clubs", 7), Card("Hearts", 8)],
        "random_hand": [Card("Diamonds", 7), Card("Clubs", 6), Card("Spades", 9), Card("Spades", 5), Card("Hearts", 2)]

    }
    # credits = 25

    Player1 = Player("Player1")
    Player1.hand = decks["random_hand"]

    # Player1.show()
    print()
    print("You have ", Player1.check(), " credits")

    # credits = play(credits)

    
def play(num_creds):


    deck = Deck()
    player1 = Player("Player1")

    playing = True

    while playing:
        print()
        print("You have ", num_creds, " credits")

        # get bet
        bet = get_bet(num_creds)
        print()

        num_creds -= int(bet)



        # get 5 cards
        for i in range(5):
            player1.draw(deck)


        print("Your hand is: ")
        player1.show()
        print()

        print("What cards would you like to hold? (1-5)")
        print("Enter 0 to hold none")
        print()
        
        num_cards = 0
        valid_input = False
        while not valid_input:
            hold = input("Enter your choice: ")
            # check number of spaces
            if hold != "0":
                num_cards = hold.count(" ")+1
                # strip the spaces
                hold = hold.replace(" ", "")
                if num_cards > 5:
                    print("You can only hold 5 cards")
                    break
                else:
                    # check if all numbers are between 1 and 5
                    for i in range(num_cards):
                        if hold[i] < "1" or hold[i] > "5":
                            print("You can only hold cards 1-5")
                            break
                        else:
                            valid_input = True
            else:
                num_cards = 0
                valid_input = True

            
        print("Hold is: ", hold)
        card_holds = [1,2,3,4,5]
        if hold != "0":
            for num in hold:
                card_holds.remove(int(num))

            for num in card_holds:
                player1.hand[num-1] = deck.draw()

        else:
            player1.hand = []
            for i in range(5):
                player1.draw(deck)


        print("Your hand is: ")
        player1.show()
        print()

        multi = player1.check()
        num_creds += int(bet) * multi

        print("You have ", num_creds, " credits")
        print()

        if num_creds == 0:
            print("You have no credits left")
            playing = False
        else:
            play_again = input("Would you like to play again? (y/n) ")
            if play_again == "n":
                playing = False
            else:
                player1.hand = []
                deck = Deck()

    return num_creds

            
def get_bet(credits):
    valid_input = False
    while not valid_input:
        bet = input("Enter your bet: ")
        if bet.isdigit():
            if int(bet) > credits:
                print("You don't have enough credits")
            else:
                valid_input = True
        else:
            print("You must enter a number")

    return bet
            


main()




# game loop
# get our 5 cards
# allow the player to hold and roll again
#       case where they don't hold
# check the 5 cards after the second roll
# update balances
# replay



