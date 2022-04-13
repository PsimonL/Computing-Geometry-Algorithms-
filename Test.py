from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import cv2

print(cv2.__version__)
#kontur jest ważny
point = Point(0.5, 5)
polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
if polygon.contains(point) == True:
    print("nalezy")
elif polygon.contains(point) == False:
    print("nie nalezy")