class Stack:
    def __init__(self):
        self.__container = []

    def push(self, item):
        if item % 2 == 0:
            self.__container.append(item)
        else:
            self.__container = [item] + self.__container
        print(self.__container)

    def pop(self):
        return self.__container.pop()

    def is_empty(self):
        return len(self.__container) == 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.pop()
        except IndexError:
            raise StopIteration
