# defining a class oan creating an Object.
# class Shark(object): == class Shark:
class Shark(object):
    """docstring for Shark."""

    def swim(self):
        print("Shark swim")

def main():
    fish = Shark()
    fish.swim()
    # Print the additional attributes associated with Object
    print(dir(fish))

if __name__ == '__main__':
    main()
