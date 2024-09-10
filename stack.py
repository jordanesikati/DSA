class ArrayStack:
    def __init__(self):
        self.stack = []

    def get_size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return "Empty" if self.is_empty() else self.stack.pop()

    def peek(self):
        return "Empty" if self.is_empty() else self.stack[-1]


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty(): return 'Empty'
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self):
        return 'Empty' if self.is_empty() else self.head.data

