# Multiple inheritence example
class MyFatherClass(object):
    def __init__(self):
        print('Father')

class MyMotherClass(object):
    def __init__(self):
        print('Mother')

class ChildClass(MyFatherClass, MyMotherClass):
    def __init__(self):
        print('Child')
        # super().__init__()  # will refer the first class in parameter(MyFatherClass)
        MyFatherClass.__init__(self)
        MyMotherClass.__init__(self)

def main():
    d1 = ChildClass()

if __name__ == '__main__':
    main()
