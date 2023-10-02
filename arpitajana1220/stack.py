#You can implement a basic stack in Python using a list. Here's a simple example of a stack:

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()

    # Push elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Print the stack
    print("Stack:", stack.items)

    # Pop elements from the stack
    popped_item = stack.pop()
    print("Popped item:", popped_item)

    # Peek at the top element
    top_item = stack.peek()
    print("Top item:", top_item)

    # Check the size of the stack
    stack_size = stack.size()
    print("Stack size:", stack_size)

#In this code, we define a Stack class that uses a list (self.items) to implement the stack operations:

#push(item): Adds an item to the top of the stack.
#pop(): Removes and returns the top item from the stack.
#peek(): Returns the top item from the stack without removing it.
#is_empty(): Checks if the stack is empty.
#size(): Returns the number of items in the stack.
#You can use this Stack class to create and manipulate stacks in your Python programs.
