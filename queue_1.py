'''Queue Data Structure to learn FIFO scenarios, OOP'''

# Using a new class to implement a queue with functions
class Queue:
    def __init__(self): #initialize attributes of object(self)
        self.items = []
    
    def __repr__(self): #return a string as rep of the object
        return f'Queue object: data={self.items}'

    def is_empty(self): #return inverse boolean value
        return not self.items

    