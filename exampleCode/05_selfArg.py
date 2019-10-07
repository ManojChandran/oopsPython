# defining self in the class
# self is Explicit representation of instance of class (Object)
class A(object): #
    """docstring for A."""
    def __init__(self, value = 0):
        self.value = value

    def set_method(self):
        print(self.value)


def main():
    a = A() # instantiating an Object
    a.set_method() # prints 0, as it runs as method with object "self".
    A().set_method # prints nothing as it runs as simple function.

if __name__ == '__main__':
    main()
