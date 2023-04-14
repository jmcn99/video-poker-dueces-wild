import os
import random
import pygame

payouts = {
    "Natural Royal Flush": 800,
    "Four Deuces": 200,
    "Wild Royal Flush": 25,
    "Five of a Kind": 15,
    "Straight Flush": 9,
    "Four of a Kind": 5,
    "Full House": 3,
    "Flush": 2,
    "Straight": 2,
    "Three of a Kind": 1,
    "No Win": 0

}

class Card:
    def __init__(self,suit, value):
        self.suit = suit
        self.value = value
        self.string = (str(value) + "_of_" + suit + ".svg").lower()
        self.image = pygame.image.load(os.path.join('card_images', self.string))
        self.hold = False

    def show(self):
        print(f"{self.value} of {self.suit}")

    def toggle_hold(self):
        self.hold = not self.hold
        print("hold: " + str(self.hold))
        
        


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            for v in range (1,14):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()



    def draw(self):
        return self.cards.pop(random.randint(0,len(self.cards)-1))


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
    
    def setDeck(self, deck):
        self.cards = deck

    def build(self, deck):
        for i in range(5):
            self.draw(deck)

    def getDeck(self):
        return self.hand
    
    def reroll(self, deck):
        for card in self.hand:
            if not card.hold:
                card = deck.draw()


    def show(self):
        for card in self.hand:
            card.show()

    def check(self):
        if(self.natural_royal_flush()):
            print("Natural Royal Flush")
            return payouts["Natural Royal Flush"]
        elif(self.four_deuces()):
            print("Four Deuces")
            return payouts["Four Deuces"]
        elif(self.wild_royal_flush()):
            print("Wild Royal Flush")
            return payouts["Wild Royal Flush"]
        elif(self.five_of_a_kind()):
            print("Five of a Kind")
            return payouts["Five of a Kind"]
        elif(self.straight_flush()):
            print("Straight Flush")
            return payouts["Straight Flush"]
        elif(self.four_of_a_kind()):
            print("Four of a Kind")
            return payouts["Four of a Kind"]
        elif(self.full_house()):
            print("Full House")
            return payouts["Full House"]
        elif(self.flush()):
            print("Flush")  
            return payouts["Flush"]
        elif(self.straight()):
            print("Straight")
            return payouts["Straight"]
        elif(self.three_of_a_kind()):
            print("Three of a Kind")
            return payouts["Three of a Kind"]
        else:
            print("No Win")
            return payouts["No Win"]

        



    def natural_royal_flush(self):
        # check for a royal flush without any 2s in hand
        # check if all cards are the same suit
        for i in range(0, len(self.hand)):
            if self.hand[i].suit != self.hand[0].suit:
                return False
        
        # copy hand
        hand_copy = []
        for card in self.hand:
            hand_copy.append(card)

            

        # sort hand
        hand_copy.sort(key=lambda x: x.value)
        if hand_copy[0].value != 1:
            return False
        
        for i in range(1, len(self.hand)):
            if hand_copy[i].value != 9 + i:
                return False
            
    
        return True
    
    def four_deuces(self):
        # check if there are 4 dueces
        num_2s = 0
        for card in self.hand:
            if card.value == 2:
                num_2s += 1
        
        if num_2s == 4:
            return True
        
        return False

    def wild_royal_flush(self):
        num_2s = 0
        # check if there is a 2 in the hand
        # count number of 2s in the hand
        
        for card in self.hand:
            if card.value == 2:
                num_2s += 1

        royal_flush_dict ={
            10: 0,
            11: 0,
            12: 0,
            13: 0,
            1: 0
        }

        
        for card in self.hand:
            if (card.value in royal_flush_dict):
                royal_flush_dict[card.value] += 1
            
        return (self.flush() and self.straight() and royal_flush_dict[10] + royal_flush_dict[11] + royal_flush_dict[12] + royal_flush_dict[13] + royal_flush_dict[1] + num_2s == 5)
        
        # # same suit
        # for i in range(0, len(self.hand)):
        #     if self.hand[i].value != 2 and self.hand[i].suit != self.hand[0].suit:
        #         return False
            
        # num_0s = 5
        # for i in range(0, len(self.hand)):
        #     if self.hand[i].value in royal_flush_dict:
        #         royal_flush_dict[self.hand[i].value] += 1
        #         num_0s -= 1
            
        
        # if num_0s <= num_2s:
        #     return True
        
        # return False



    def five_of_a_kind(self):
        # check if there are 5 of a kind
        num_2s = 0
        # check if there is a 2 in the hand
        # count number of 2s in the hand
        
        for card in self.hand:
            if card.value == 2:
                num_2s += 1

        hand_copy = []
        for card in self.hand:
            hand_copy.append(card)

        hand_copy.sort(key=lambda x: x.value)

                
        
        for i in range(1, 14):
            count = 0
            for card in self.hand:
                if card.value == i:
                    count += 1
            if count + num_2s >= 5:
                return True
            
        return False

    def three_of_a_kind(self):
        # check if there are 5 of a kind
        num_2s = 0
        # check if there is a 2 in the hand
        # count number of 2s in the hand
        
        for card in self.hand:
            if card.value == 2:
                num_2s += 1

        hand_copy = []
        for card in self.hand:
            hand_copy.append(card)
        
        hand_copy.sort(key=lambda x: x.value)

        for i in range(1, 14):
            count = 0
            for card in self.hand:
                if card.value == i:
                    count += 1
            if count + num_2s >= 3:
                return True
        
        return False

    def straight_flush(self):

        return (self.straight() and self.flush())

        #check if straight flush

    def flush(self):
        #check if flush

        num_2s = 0
        # check if there is a 2 in the hand
        # count number of 2s in the hand

        #deep copy sort
        
        index = 0 
        found = False
        index_of_non_2 = 0
        for card in self.hand:
            if card.value != 2 and not found:
                found = True
                index_of_non_2 = index
        
            elif card.value == 2:
                num_2s += 1

            index += 1
            
            
        for i in range(0, len(self.hand)):
            if self.hand[i].value != 2 and self.hand[i].suit != self.hand[index_of_non_2].suit:
                return False

        return True

    def straight(self):
        #check if straight
        
        # make a deep copy of the hand
        hand_copy = []
        for card in self.hand:
            hand_copy.append(card)
        # sort
        hand_copy.sort(key=lambda x: x.value)
        # count num 2s
        num_2s = 0
        for card in self.hand:
            if card.value == 2:
                num_2s += 1
        # check if there are only 1s in the array other than 2s
        cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        for card in hand_copy:
            cards[card.value-1] += 1

        print(cards)

        
        for i in range(0, len(cards)):
            if cards[i] > 1 and i != 1:
                return False
            

        

        # if there are 0 2s, check for 5 1s in a row
        if cards[1] == 0:
            for i in range(0, 9):
                if cards[i] == 1 and cards[i+1] == 1 and cards[i+2] == 1 and cards[i+3] == 1 and cards[i+4] == 1:
                
                    return True
            # check for 10 J Q K A
            if cards[0] == 1 and cards[9] == 1 and cards[10] == 1 and cards[11] == 1 and cards[12] == 1:
                return True
            
        
        # if there is one 2, check for 4 1s in a group of 5
        elif cards[1] == 1:
            print("going into 1 2")
            cards[1] = 0
            for i in range(0, 9):
                if cards[i] + cards[i+1] + cards[i+2] + cards[i+3] + cards[i+4] == 4:
                    return True
            # check for 10 J Q K A
            if cards[0] + cards[9] + cards[10] + cards[11] + cards[12] == 4:
                return True
        #if there is two 2s, check for 3 1s in a group of 5
        elif cards[1] == 2:
            cards[1] = 0
            for i in range(0, 9):
                if cards[i] + cards[i+1] + cards[i+2] + cards[i+3] + cards[i+4] == 3:
                    return True
            # check for 10 J Q K A
            if cards[0] + cards[9] + cards[10] + cards[11] + cards[12] == 3:
                return True

        return False
        
    def four_of_a_kind(self):
        num_2s = 0
        # check if there is a 2 in the hand
        # count number of 2s in the hand
        


        cards = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        for card in self.hand:
            cards[card.value-1] += 1

        num_2s = cards[1]
        cards[1] = 0
        for i in range(0, len(cards)):
            if cards[i] + num_2s == 4:
                return True    


    def full_house(self):
        cards = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 0
        }

        hand_copy = []
        for card in self.hand:
            hand_copy.append(card)

        hand_copy.sort(key=lambda x: x.value)
        num2s = 0
        for card in hand_copy:
            cards[card.value] += 1


        num2s = cards[2]
        three_of_a_kind = False
        pair = False

        if num2s == 0:
            for i in range(1,14):
                if cards[i] == 3:
                    three_of_a_kind = True
                if cards[i] == 2:
                    pair = True

            if three_of_a_kind and pair:
                return True

        elif num2s == 1:
            cards[2] = 0

            # look for 3 of a kind
            for i in range(1,14):
                if cards[i] == 3:
                    return True

            # look for 2 pairs
            num_pairs = 0
            for i in range(1,14):
                if cards[i] == 2:
                    num_pairs += 1
            if num_pairs == 2:
                return True

        elif num2s == 2:
            # look for 3 of a kind
            cards[2] = 0
            for i in range(1,14):
                if cards[i] == 3:
                    return True
            # look for a pair
            for i in range(1,14):
                if cards[i] == 2:
                    return True
        
                    
    

        return False
