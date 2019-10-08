# Defining a method
# Method = Function + associated Object
class Car(object):
    """docstring for Car."""

    def __init__(self, make, model):
        self.make = make
        self.model = model

    # instance method defined
    def insurancePerAunnum(self):
        print(self.model * 10)

def main():
    commute = Car("Camry", 2011) # Object instatiation
    commute.insurancePerAunnum() # Method call

if __name__ == '__main__':
    main()
