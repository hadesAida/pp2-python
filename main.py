from square import Square
from rectangle import Rectangle
from point import Point
from acc import Account

def main():
    square = Square(4)
    print(square.area())

    point1 = Point(0, 0)
    point2 = Point(3, 4)
    print(point1.dist(point2))

    account = Account("John Doe", 1000)
    account.deposit(500)
    account.withdraw(200)

if __name__ == "__main__":
    main()
