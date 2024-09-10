class ArrayQueue:
    def __init__(self):
        self.queue = []

    def get_size(self):
        return len(self.queue)

    def is_empty(self):
        return self.get_size() == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return 'Empty' if  self.is_empty() else self.queue.pop(0)

    def peek(self):
        return 'Empty' if self.is_empty() else self.queue[0]

