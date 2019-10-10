# Abstraction example
# It becomes blue print for implementation
# can't instantiate abstract class
from abc import ABC, abstractmethod # ABC = Abstract Base Classes
class abstarctLandAnimal(ABC):
    """docstring for abstarctLandAnimal."""
    def __init__(self):
        super().__init__()    

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def talk(self):
        pass

class Duck(abstarctLandAnimal):
    """docstring for Duck."""

    def __init__(self):
        super().__init__()
        self.name = 'duck'

    def walk(self):
        print('duck walks')
    def talk(self):
        print('duck quaks')

def main():
    d1 = Duck()
    d1.walk()
    d1.talk()

if __name__ == '__main__':
    main()
