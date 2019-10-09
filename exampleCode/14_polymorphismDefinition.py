# Polymorphism is the capacity to take on different forms
# Polymorphism with Class Methods
class Add(object):
    """docstring for Add."""

    def operation(self, x, y):
        self.x = x
        self.y = y
        return (self.x + self.y)

class Sub(object):
    """docstring for Sub."""

    def operation(self, x, y):
        self.x = x
        self.y = y
        return (self.x - self.y)

def main():
    A = Add()
    S = Sub()

    for resultof in (A, S):
        print(resultof.operation(5,3))

if __name__ == '__main__':
    main()
