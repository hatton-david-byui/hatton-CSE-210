import random
    


def card():
    """Card will choose a random number from 1-13. The numbers
    represent a card."""
    return random.randint(1, 13)
card_number1 = card()
print(card_number1)
