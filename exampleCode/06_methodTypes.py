# three types of methods in Python:
    # class methods.
    # static methods.
    # instance methods.
class MyClass(object):

    def method(self):
        retrun ('instance method called', self)

    @classmethod
    def classmethod(cls):
        return ('class method called', cls)

    @staticmethod
    def staticmethod():
        return 'static method called'

def main():
    obj = MyClass()
    print(obj.method)
    print(obj.classmethod)
    print(obj.staticmethod)
    # Method Resolution Order (MRO) is the order in which Python
    # looks for a method in a hierarchy of classes.
    print(MyClass.mro())

if __name__ == '__main__':
    main()
