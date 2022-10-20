# TODO: Implement the Seeker class as follows...

# 1) Add the class declaration. Use the following class comment.
class Seeker:  

# 2) Create the class constructor. Use the following method comment.

    def __init__(self):
       self._location = 0

# 3) Create the get_location(self) method. Use the following method comment.
    def get_location(self):
        return self._location       
        
# 4) Create the move_location(self, location) method. Use the following method comment.
    def move_location(self, location):
        self._location = location