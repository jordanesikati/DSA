class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return "Empty" if self.is_empty() else self.stack.pop()

    def peek(self):
        return "Empty" if self.is_empty() else self.stack[-1]