from game.card import Card

class Director:

    def __init__(self):
        self.card = Card()
        self.another = ""
        self.answer = ""
        self.Q = self.question(self)
        self.choice = ""
        self.score = 0
        self.keep_playing = True
        self.points = 0
        self.random_card1 = self.card_draw(self)
        self.random_card2 = self.card_draw(self)
        
    def start_playing(self):
        """Gets things going and will be cycled through every time they choose to play another round"""
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """Starts things out by getting assigning card_number1"""
        self.card.card_number1

    def do_updates(self):
        """Checks the guess of the player by reaching into Card.py and gives or takes poins accordingly."""
        if self.choice == "low":
            self.points = self.card.low()
            

        elif self.choice == "high":
            self.points = self.card.high()

    def do_outputs(self):
        """Outputs the important game information for each round of play. it shows the player
        their first card and shows them their score. it then asks them if they would like another card
        if yes, it gets their guess and startes everything over. 
        if no, it stopps the game. 
        """
        print(f"\nYour new card is: {self.card.card_number2}")
        print(f"Your score is: {self.score}")
        self.another = input("would you like another card (y/n):")
        if self.another == "y":
            self.choice = input("High or Low? [high/low]:")
            self.do_updates
            self.keep_playing = (self.choice == "y")
        else:
            self.keep_playing = False
    


    def question(self):
        self.choice = input("high or low:")
        self.answer = 


    def card_draw(self):
        return self.card.card(self)

    def in_or_out(self):
        self.choice = input("keep playing?")



