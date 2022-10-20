from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.terminal_service = TerminalService()
        self.jumper = Jumper()
        self.puzzle = Puzzle(self.jumper)
        self.run = True
        self.letter_input = ""
        self.person = ""
        self.hidden_word = []
        self.first_run = True
        
    def start_game(self):
        self.person = self.jumper.create_jumper()
        self.puzzle._select_word()
        self.hidden_word = self.puzzle.draw_word_guess()
        self.run_game()
    
    def _get_inputs(self):
    
        self.guess_letter = self.terminal_service.read_text("\nGuess a letter [a-z] ")
        
        
    def _do_updates(self):
 
        self.hidden_word = self.puzzle.process_guess(self.letter_input)
        self.jumper_guy = self.jumper.get_jumper()
        self.run = False
        for value in self.hidden_word:
            if value == "_":
                self.run = True
        if self.jumper.get_end_game() == True:
            self.run = False
        
    def _do_outputs(self):
        self.terminal_service.write_text(self.person)
        self.terminal_service.write_text(self.hidden_word)

    def run_game(self):
        while self.run:
            if self.first_run == False:
                self._get_inputs()
            self._do_updates()
            self._do_outputs()
            self.first_run = False
        