class Array:

    def __init__(self):
        self.array = []

    def is_empty(self):
        return self.get_size() == 0

    def get_size(self):
        return len(self.array)

    def insert(self, data):
        self.array.append(data)

    def get_min(self):
        return [i for i in self.array if all(i <= j for j in self.array)][0]

    def get_max(self):
        return [i for i in self.array if all(i >= j for j in self.array)][0]

    def display(self):
        return self.array

    def delete(self, index):
        pass

    def bubble_sort(self):

        for i in range(self.get_size() - 1):
            swapped = False
            for j in range(self.get_size() - i - 1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    swapped = True
            if not swapped:
                break
        return self.array

    def linear_search(self, target):
        search = [self.array[i] for i in range(self.get_size()) if self.array[i] == target]
        return 'Not Found' if len(search) == 0 else search[0]

    def binary_search(self, target):
        left, right = 0, self.get_size() -1

        while left <= right:
            middle = (left + right) // 2

            if self.array[middle] == target:
                return self.array[middle]

            if self.array[middle] < target:
                left = middle + 1

            else:
                right = middle - 1

        return 'Not Found'



