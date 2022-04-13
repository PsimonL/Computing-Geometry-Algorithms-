from random import *
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
def orientation(p, q, r):
    result = (q - p).cross(r - p)

def crossing_number ( polygon , point):
    cn = 0
    n = len(polygon.point_list)
    for i in range(n):
        a = polygon.point_list[i]
        b = polygon.point_list[(i+1)%n]
        if a.y <= point.y:
            if b.y > point.y and orientation

if __name__ == "__main__":
    #liczba wierzhcolkow weilokąta
    #n = randint(4, 6)
    n = 4
    print(n)
    a = 5
    """check_x = randint(1, a)
    check_y = randint(1, a)"""
    check_x = 1
    check_y = 1
    print("Check Point:" + str(check_x) + " " + str(check_y))
    check_point = Point(check_x, check_y)

    """set_x = set()
    set_y = set()
    start_a = 0
    finish_a = n
    start_b = start_a
    finish_b = finish_a

    while start_a < finish_a:
        r = randint(1, a)
        if r not in set_x:
            start_a += 1
            set_x.add(r)
    while start_b < finish_b:
        r = randint(1, a)
        if r not in set_y:
            start_b += 1
            set_y.add(r)

    list_x = list(set_x)
    list_y = list(set_y)
    shuffle(list_x)
    shuffle(list_y)"""
    list_x = [5, 0, 5, 0]
    list_y = [5, 5, 0, 0]
    print(list_x)
    print(list_y)
    final_list = list(zip(list_x, list_y))
    print(final_list)


    point = Point(check_x, check_y)
    polygon = Polygon(final_list)
    if polygon.contains(point) == True:
        print("nalezy")
    elif polygon.contains(point) == False:
        print("nie nalezy")