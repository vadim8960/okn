
class Stack:

    def __init__(self, values=None):
        self.values = values
        pass

    def pop(self):
        if self.is_empty():
            return None
        retv = self.values[0]
        self.values = self.values[1:]
        return retv

    def push(self, elem):
        self.values.insert(0, elem)
        pass

    def is_empty(self):
        return not (len(self.values) > 0)

    def __str__(self):
        return str(self.values)

    def __eq__(self, other):
        return self.values == other.values

    def __ne__(self, other):
        return not Stack.__eq__(self, other)

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        return Stack(other.values + self.values)

    def __iadd__(self, other):
        return Stack(other.values + self.values)


def main():
    stack = Stack([1, 2, 3])
    stack2 = Stack([5, 6, 7])
    stack3 = Stack([8, 9, 10])

    print(stack)
    print(stack2)
    print(stack3)
    print()
    print(stack.pop())
    print(stack)
    stack.push(123)
    print(stack)
    print()
    print(stack + stack2)
    stack3 += stack
    print(stack3)
    print()
    print(stack != stack2)
    print()
    print(len(stack))
    print()

if __name__ == '__main__':
    main()

