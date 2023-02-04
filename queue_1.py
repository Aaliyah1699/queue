'''Queue Data Structure to learn FIFO scenarios, OOP'''

# Using a new class to implement a queue with functions


class Queue:
    def __init__(self):  # initialize attributes of object(self)
        self.items = []

    def __repr__(self):  # return a string as rep of the object
        return f'Queue object: data={self.items}'

    def is_empty(self):  # return inverse boolean value
        return not self.items

    def enqueue(self, item):  # add item to self.items
        self.items.append(item)

    def dequeue(self):  # remove items from beginning
        return self.items.pop(0)

    def size(self):  # return the length of items
        return len(self.items)

    def peek(self):  # return top element in self.items
        return self.items[0]


# execute code as script
if __name__ == '__main__':
    q = Queue()  # store queue class in this variable
    print(q.is_empty())
    q.enqueue('First')
    q.enqueue('Second')
    print(q)
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())
