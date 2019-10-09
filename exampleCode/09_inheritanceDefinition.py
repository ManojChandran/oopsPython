# Inheritance example.
# Pass class value instead of object while defining.
class Mammal(object):
    """docstring for Mamal."""

    def is_a_mammal(self):
        print('yes, a mammal')

class Whale(Mammal): # Pass class and getting inheritted
    """docstring for Whale."""

    def who_is_this(self):
        print('Whale')

def main():
    w = Whale() # instantiating Object whale
    w.who_is_this()
    w.is_a_mammal() # inherited is a relationship

if __name__ == '__main__':
    main()
