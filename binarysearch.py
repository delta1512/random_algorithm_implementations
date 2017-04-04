from random import randint

class node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def hopin(self, value):
        if self.value == None:
            self.value = value
        else:
            if value <= self.value:
                if self.left == None:
                    self.left = node()
                self.left.hopin(value)
            else:
                if self.right == None:
                    self.right = node()
                self.right.hopin(value)

    def traverse(self):
        yield self.value
        if self.left != None:
            yield from self.left.traverse()
        if self.right != None:
            yield from self.right.traverse()

root = node()

a = 1
b = 100
root.hopin(round((b-a)/2))

for x in range(10):
    root.hopin(randint(a, b))

for x in root.traverse():
    print(x)
