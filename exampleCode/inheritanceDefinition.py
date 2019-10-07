class Mamal(object):
    """docstring for Mamal."""

    def feed(self, animalName):
        print(animalName, 'is a Mamal.')

class Whale(Mamal):
    """docstring for Whale."""

    def swim(self):
        print('Whale lives in sea.')
        super().feed('whale')

def main():
    w = Whale()
    w.feed()

if __name__ == '__main__':
    main()
