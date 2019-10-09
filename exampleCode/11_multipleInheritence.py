# Multiple inheritence example
class MyFatherClass(object):
    def __init__(self):
        super().__init__()
        print('Father')

class MyMotherClass(object):
    def __init__(self):
        super().__init__()
        print('Mother')

class ChildClass(MyFatherClass, MyMotherClass):
    def __init__(self):
        print('Child')
        super().__init__()

def main():
    d1 = ChildClass()

if __name__ == '__main__':
    main()

# Output will be in following order Child/Mother/Father 
# The reason we use super in init, is so that child classes that may
# be using cooperative multiple inheritance will call the correct next
# parent class function in the Method Resolution Order (MRO).
