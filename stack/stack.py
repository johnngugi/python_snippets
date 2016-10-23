class Stack:
    """An implementation of a stack in python."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        return self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
