

class Jumper:

    def __init__(self):
        self.num_incorrect = 0
        self.end_game = False

    def create_jumper(self):
        if self.num_incorrect == 0:
            jumper = """
             ___  
            /___\ 
            \   / 
             \ /  
              0   
             /|\  
             / \  
            """
        elif self.num_incorrect == 1:
            jumper = """
            /___\ 
            \   / 
             \ /  
              0   
             /|\  
             / \  
            """
        elif self.num_incorrect == 2:
            jumper = """
            \   / 
             \ /  
              0   
             /|\  
             / \  
            """
        elif self.num_incorrect == 3:
            jumper = """
             \ /  
              0   
             /|\  
             / \  
            """
        elif self.num_incorrect == 4:
            jumper = """
              X   
             /|\  
             / \  
            """
            self.end_game = True
        return jumper

    def get_jumper(self):
        return self.create_jumper()

    def get_end_game(self):
        return self.end_game
        
    def set_num_incorrect(self, incorrect):
        self.num_incorrect = incorrect