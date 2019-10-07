# Confusion around constuctor in python
# __new__ runs before __init__
# object is already present.
class OurClassContructor(object):
    """docstring for OurClassContructor."""

    def __new__(cls,*args,**kwargs):
        print("==============")
        print("Inside __new__")
        print(cls)
        print(args)
        print(kwargs)

        obj = super().__new__(cls)
        return obj

    def __init__(self, name = "Chandran"):
        print("==============")
        print("Inside __init__")
        self.name = name

def main():
    OurObject = OurClassContructor("Manoj")

if __name__ == '__main__':
    main()
