import random

class Card:
    """This is everything we should need for the card decision.
    The random card that is chosen, the number of turns, and High/Low
    choice consequences."""
    def __init__(self):
        self.card_number1 = 0
        self.card_number2 = 0

    def card(self):
        """Card will choose a random number from 1-13. The numbers
        represent a card."""
        self.card_number1 = random.randint(1, 13)
        self.num_turns += 1
    
    def high(self):
        """If player chooses High and gets it right we add 100 points
        But if they get it wrong they lose 75 points"""
        if self.card_number2 > self.card_number1:
            return +100
        elif self.card_number2 < self.card_number1:
            return -75


    def low(self):
        """If player chooses Low and gets it right we add 100 points
        But if they get it wrong they lose 75 points"""
        if self.card_number2 < self.card_number1:
            return self.point_total + 100
        elif self.card_number2 > self.card_number1:
            return self.point_total - 75

    


