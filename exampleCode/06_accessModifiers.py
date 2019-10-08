class Car(object):
    """docstring for Car."""

    def __init__(self):
        print('my car')
        self.name = 'Camry'     # Public
        self.__make = 'Toyota'  # Private
        self._model = 2011      # protected

def main():
    obj = Car()
    print(obj.name)
    print(obj._model)
    # print(obj._make) # will give error


if __name__ == '__main__':
    main()
