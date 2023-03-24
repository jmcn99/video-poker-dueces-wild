import random

class Card:
    def __init__(self,suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")


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


    def show(self):
        for card in self.hand:
            card.show()

    def check(self):
        if(self.natural_royal_flush()):
            print("Natural Royal Flush")
        elif(self.four_deuces()):
            print("Four Deuces")
        elif(self.wild_royal_flush()):
            print("Wild Royal Flush")
        elif(self.five_of_a_kind()):
            print("Five of a Kind")
        elif(self.straight_flush()):
            print("Straight Flush")
        elif(self.four_of_a_kind()):
            print("Four of a Kind")
        elif(self.full_house()):
            print("Full House")
        elif(self.flush()):
            print("Flush")  
        elif(self.straight()):
            print("Straight")   
        elif(self.three_of_a_kind()):
            print("Three of a Kind")
        else:
            print("No Win")

        



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

        
        #specifically check hands with aces
        if(hand_copy[0] == 1 and hand_copy[1] == 2 and (hand_copy[2] == 3  or hand_copy[2] == 2) and (hand_copy[3] == 4 or hand_copy[3] == 2) and (hand_copy[4] == 5 or hand_copy[4] == 2)):
           return True

        if(hand_copy[0] == 1 and (hand_copy[1] == 10 or hand_copy[1] == 2) and (hand_copy[2] == 11 or hand_copy[2] == 2) and (hand_copy[3] == 12 or hand_copy[3] == 2) and (hand_copy[4] == 13 or hand_copy[4] == 2)):
            return True
        
        
        for i in range(0, len(hand_copy)-1):
            if hand_copy[i].value != 2 and hand_copy[i+1].value-1 != hand_copy[i].value:
                return False
            

        return True
        
    def four_of_a_kind(self):
        num_2s = 0
        # check if there is a 2 in the hand
        # count number of 2s in the hand
        
        for card in self.hand:
            if card.value == 2:
                num_2s += 1

        #check if four of a kind
        for i in range(1, 14):
            # count amount of cards with value i
            count = 0
            for card in self.hand:
                if card.value == i:
                    count += 1
            if count + num_2s >= 4:
                return True
        return False


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
            if card.value == 2:
                num2s += 1
            else:
                cards[card.value] += 1

        three_of_a_kind = False
        pair = False
        for i in range(1,14):
            if cards[i] + num2s >= 3:
                three_of_a_kind = True
                num2s -= 3 - cards[i]
                cards[i] = 0
                break
        
        if(three_of_a_kind):
            for i in range(1,14):
                if cards[i] + num2s >= 2:
                    pair = True
                    break

        return (pair and three_of_a_kind)
