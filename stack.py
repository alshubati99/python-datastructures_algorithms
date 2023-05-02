
class Stack:
    def __init__(self): # constructor 
        self.items = [] # specific item of the class

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] # returns the last item

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items) # prints statement to inspect results


if __name__ == "__main__": # when importing this code into another file
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop()) # returns the value, and remove it
    print(s)
    print(s.peek()) # returns the last time of the stack
    print(s.size())

