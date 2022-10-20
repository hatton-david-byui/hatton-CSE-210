import random as rd
from game.jumper import Jumper

class Puzzle:  

    def __init__(self, jumper):
        self._word_list = ["Earth", "Mars", "Jupiter"]
        self._word_selected = ""
        self.hidden_word = []
        self.current_letter = ""
        self._word_guess = ["_"]
        self.length = 0
        self.errors = 0
        self.jumper = jumper

    def _select_word(self):
        self._word_selected = rd.choice(self._word_list)
        self.length = len(self._word_selected)
        self._word_guess = [char for char in self._word_selected]
        return(self._word_selected)

    def draw_word_guess(self):
        self.hidden_word = ["_"] * self.length
        return(self.hidden_word)

    def process_guess(self, guess_letter):
        self.current_letter = guess_letter
        if self.current_letter in self._word_selected:
            self.hidden_word = self.can_keep_guessing(self.current_letter)
            return self.hidden_word
        else:
            self.errors += 1
            self.jumper.set_num_incorrect(self.errors)
            return self.hidden_word        
        
    def can_keep_guessing(self, guess_letter):
        self.current_letter = guess_letter
        for x in range(self.length):
            if self.current_letter == self._word_guess[x]:
                self.hidden_word[x] = self.current_letter
        return(self.hidden_word)
        
        