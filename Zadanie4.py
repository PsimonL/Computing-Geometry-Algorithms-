from random import *
import matplotlib.pyplot as plt
def circle_crossings(radius, x0, y0):
    figure, axes = plt.subplots()

    x1 = randint(0, 10)
    y1 = randint(0, 10)
    x2 = randint(0, 10)
    y2 = randint(0, 10)
    print("Wspolrzedne odcinka - tail: (" + str(x1) + ", " + str(y1) + ")")
    print("Wspolrzedne odcinka - head: (" + str(x2) + ", " + str(y2) + ")")

    plt.plot([x1, x2], [y1, y2])
    circle = plt.Circle((x0, y0), radius, color="red", fill=False)
    axes.add_patch(circle)

    a = x1 ** 2 + y1 ** 2 + x2 ** 2 + y2 ** 2 - 2 * (x1 * x2 + y1 * y2)
    b = 2 * ((x0 * (x2 - x1)) + (y0 * (y2 - y1)) + (x1 * x2) + (y1 * y2) - (x2 ** 2) - (y2 ** 2))
    c = -(radius ** 2) + x2 ** 2 + y2 ** 2 + x0 ** 2 + y0 ** 2 - 2 * (x0 * x2 + y0 * y2)

    delta = b ** 2 - (4 * a * c)

    if delta == 0:
        print("1 pkt wspolny")
    elif delta > 0:
        print("2 pkt wspolne")
    else: # delta < 0
        print("0 pkt wspolnych")
    plt.show()

#radius = int(input("Wprowadz dlugosc promienia: "))
radius = 3
x0 = 10
y0 = 10

circle_crossings(radius, x0, y0)