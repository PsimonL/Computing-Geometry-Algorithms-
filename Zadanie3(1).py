import numpy as np
from random import randint
import cv2

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
#WAŻNE! __str__
    def __str__(self):
        return f"({self.x}, {self.y})"


class Polygon:
    def __init__(self, points: list[Point]):
        self.points = [point for point in points]
        self.contour = [[point.x, point.y] for point in self.points]
        self.contour = np.array(self.contour)
        for point in self.points: print(point)

    def is_object_in_field(self, obj_coordinates):
        if cv2.pointPolygonTest(self.contour, (obj_coordinates.x, obj_coordinates.y), measureDist=False) >= 0:
            print("Punkt nalezy")
        else:
            print("Punkt NIE nalezy")


if __name__ == "__main__":
    points = [Point(randint(1, 10), randint(1, 10)) for _ in range(randint(4, 6))]
    p1 = Polygon(points)
    check_x = randint(1, 10)
    check_y = randint(1, 10 )
    print("Check Point: (" + str(check_x) + ", " + str(check_y) + ") ")
    p1.is_object_in_field(Point(check_x, check_y))