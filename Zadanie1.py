from math import *
from random import *
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

def line_equation(line):
    x1 = line.tail.x
    y1 = line.tail.y
    x2 = line.head.x
    y2 = line.head.y

    a = (y2 - y1) / (x2 - x1)
    b = y2 - (a * x2)
    stra = str(a)
    strb = str(b)

    return "Szukana prosta to: y = " + stra + "x + " + strb

def checkPoint(check, line):
    x1 = line.tail.x
    y1 = line.tail.y
    x2 = line.head.x
    y2 = line.head.y
    list_X = [x1, x2]
    list_Y = [y1, y2]

    new_a = (y2 - y1) / (x2 - x1)
    new_b = y2 - (new_a * x2)
    strnew_a = str(new_a)
    strnew_b = str(new_b)
    print("Prosta to: y = " + strnew_a + "x + " + strnew_b)

    angle_in_degree = float(input("Wprowadz kat w stopniach:"))
    angle_in_radian = (3.14 * angle_in_degree) / 180

    print("Head/Tail")
    choice = input()

    if choice == "Tail":
        new_x1 = x1 * cos(angle_in_radian) - y1 * sin(angle_in_radian)
        new_y1 = y1 * cos(angle_in_radian) + x1 * sin(angle_in_radian)

        new_a = (y2 - new_y1) / (x2 - new_x1)
        new_b = y2 - (new_a * x2)
        strnew_a = str(new_a)
        strnew_b = str(new_b)
        print("Nowa prosta to: y = " + strnew_a + "x + " + strnew_b)

        if check.y > check.x * new_a + new_b:
            print("Punkt jest nad prosta o wspolrzednych (" + str(check.x) + ", " + str(check.y) + " )")
        elif check.y < check.x * new_a + new_b:
            print("Punkt jest pod prosta o wspolrzednych (" + str(check.x) + ", " + str(check.y) + " )")
        elif check.y == check.x * new_a + new_b:
            print("Punkt nalezy do prostej o wspolrzednych (" + str(check.x) + ", " + str(check.y) + " )")
        else:
            print("XD")
    elif choice == "Head":
        new_x2 = x2 * cos(angle_in_radian) - y2 * sin(angle_in_radian)
        new_y2 = y2 * cos(angle_in_radian) + x2 * sin(angle_in_radian)

        new_a = (new_y2 - y1) / (new_x2 - x1)
        new_b = new_y2 - (new_a * new_x2)
        strnew_a = str(new_a)
        strnew_b = str(new_b)
        print("Nowa prosta to: y = " + strnew_a + "x + " + strnew_b)

        if check.y > check.x * new_a + new_b:
            print("punkt jest nad prosta o wspolrzednych (" + str(check.x) + ", " + str(check.y) + " )")
        elif check.y < check.x * new_a + new_b:
            print("punkt jest pod prosta o wspolrzednych (" + str(check.x) + ", " + str(check.y) + " )")
        elif check.y == check.x * new_a + new_b:
            print("punkt nalezy do prostej o wspolrzednych (" + str(check.x) + ", " + str(check.y) + " )")
        else:
            print("XD")
    else:
        print("DX")

    plt.title("Zadanie 1")
    plt.plot(list_X, list_Y)
    plt.scatter(check.x, check.y, s=10)
    plt.show()


if __name__ == "__main__":
    x1 = randint(1, 10)
    y1 = randint(1, 10)
    x2 = randint(1, 10)
    y2 = randint(1, 10)
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    line_1st = Line(point1, point2)
    check_x = randint(x1, x2)
    check_y = randint(1, 10)
    check_point = Point(check_x, check_y)
    checkPoint(check_point, line_1st)