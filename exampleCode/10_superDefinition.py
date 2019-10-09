# The super() builtin returns a proxy object that
# allows you to refer parent class by 'super'.
# super().__init__() = MyParentClass.__init__(self)
class MyParentClass(object):
    def __init__(self):
        print('Parent')

class SubClass(MyParentClass):
    def __init__(self):
        print('Child')
        super().__init__()
        #MyParentClass.__init__(self)

def main():
    d1 = SubClass()

if __name__ == '__main__':
    main()
