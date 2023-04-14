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

    # Player1 = Player("Player1")
    # Player1.hand = decks["random_hand"]

    # # Player1.show()
    # print()
    # print("You have ", Player1.check(), " credits")
    play(10)

    # credits = play(credits)

# pygame

pygame.init()
width = 1440
height = 810
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Video Poker Dueces Wild")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

# fonts
font = pygame.font.SysFont("didot", 24)

# draw buttons
def draw_button(screen, color, x, y, width, height, text):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text = font.render(text, True, black)
    screen.blit(text, (x + (width/2 - text.get_width()/2), y + (height/2 - text.get_height()/2)))


def draw_cards(screen, hand):
    # draw cards

    # dont touch the width values this shit took forever
    pygame.Surface.blit(screen, hand[0].image, (248- 140, 100))
    pygame.Surface.blit(screen, hand[1].image, (248 * 2- 140, 100))
    pygame.Surface.blit(screen, hand[2].image, (248 * 3- 140, 100))
    pygame.Surface.blit(screen, hand[3].image, (248 * 4- 140, 100))
    pygame.Surface.blit(screen, hand[4].image, (248 * 5- 140, 100))

def draw_buttons(screen, hand):
    draw_button(screen, green if hand[0].hold else white, 280 - 140 + 30, 500, 100, 50, "HOLD")
    draw_button(screen, green if hand[1].hold else white, 280 * 2 - 140, 500, 100, 50, "HOLD")
    draw_button(screen, green if hand[2].hold else white, 280 * 3 - 140 - 30, 500, 100, 50, "HOLD")
    draw_button(screen, green if hand[3].hold else white, 280 * 4 - 140 - 60, 500, 100, 50, "HOLD")
    draw_button(screen, green if hand[4].hold else white, 280 * 5 - 140 - 90, 500, 100, 50, "HOLD")


def play(num_creds):



    deck = Deck()
    player1 = Player("Player1")
    player1.build(deck)

    playing = True

    # setup screen

        
    while True:

        curDeck = player1.getDeck()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # check button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # check if mouse position is over the button
                if 280 - 140 + 30 < mouse_pos[0] < 280 - 140 + 30 + 100 and 500 < mouse_pos[1] < 500 + 50:
                    print("button 1 clicked")
                    curDeck[0].toggle_hold()
                if 280 * 2 - 140 < mouse_pos[0] < 280 * 2 - 140 + 100 and 500 < mouse_pos[1] < 500 + 50:
                    print("button 2 clicked")
                    curDeck[1].toggle_hold()

                if 280 * 3 - 140 - 30 < mouse_pos[0] < 280 * 3 - 140 - 30 + 100 and 500 < mouse_pos[1] < 500 + 50:
                    print("button 3 clicked")
                    curDeck[2].toggle_hold()
                if 280 * 4 - 140 - 60 < mouse_pos[0] < 280 * 4 - 140 - 60 + 100 and 500 < mouse_pos[1] < 500 + 50:
                    print("button 4 clicked")
                    curDeck[3].toggle_hold()
                if 280 * 5 - 140 - 90 < mouse_pos[0] < 280 * 5 - 140 - 90 + 100 and 500 < mouse_pos[1] < 500 + 50:
                    print("button 5 clicked")
                    curDeck[4].toggle_hold()

        screen.fill(black)

        # test card drawings
        draw_cards(screen, player1.hand)
        draw_buttons(screen, player1.hand)
        pygame.display.update()

        pygame.display.update()

    


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



