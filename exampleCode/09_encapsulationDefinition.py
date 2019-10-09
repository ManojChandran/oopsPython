# defining Encapsulation
class ProductEncapsulation(object):
    """docstring ProdEncapsulation."""

    def __init__(self):
        self.__productName = 't-shirt'
        self.__brandCode = '871628736777'

    def getProductname(self):
        return self.__productName

    def getbradCode(self):
        return self.__brandCode

def main():
    Item = ProductEncapsulation()
    print(Item.getProductname())
    print(Item.getbradCode())

if __name__ == '__main__':
    main()
