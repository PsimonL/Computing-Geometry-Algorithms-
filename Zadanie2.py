from tkinter import *
from random import *

def area_of_triangle(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 -y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

def check_if_point_inside_triangle(x1, y1, x2, y2, x3, y3, check_x, check_y):
    area = area_of_triangle(x1, y1, x2, y2, x3, y3)
    area1 = area_of_triangle(check_x, check_y, x2, y2, x3, y3)
    area2 = area_of_triangle(x1, y1, check_x, check_y, x3, y3)
    area3 = area_of_triangle(x1, y1, x2, y2, check_x, check_y)

    print("Wspolrzedne sa informatyczne tzn uklad wspolrzednych zaczyna sie w lewym gornym rogu okna - obie wspolrzedne dodatnie.")
    if area == area1 + area2 + area3:
        print("Pkt o wspl (" + str(check_x) + ", " + str(check_y) + ") nalezy do trojkata")
    else:
        print("Pkt o wspl (" + str(check_x) + ", " + str(check_y) + ") NIE nalezy do trojkata")

def create_circle(x, y, r, c):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return c.create_oval(x0, y0, x1, y1)

if __name__ == "__main__":
    root = Tk()
    root.geometry('600x600')
    c = Canvas(root, height=600, width=600, bg="white")
    """
    #Przyklad kiedy nalezy
    x1 = 0
    y1 = 0 
    x2 = 200
    y2 = 0
    x3 = 0
    y3 = 200
    check_x = 50
    check_y = 50
    """
    x1 = randint(1, 600)
    y1 = randint(1, 600)
    x2 = randint(1, 600)
    y2 = randint(1, 600)
    x3 = randint(1, 600)
    y3 = randint(1, 600)
    check_x = randint(1, 600)
    check_y = randint(1, 600)

    line1 = c.create_line(x1, y1, x2, y2, width=5, fill="red")
    line2 = c.create_line(x2, y2, x3, y3, width=5, fill="red")
    line3 = c.create_line(x3, y3, x1, y1, width=5, fill="red")
    # create_circle(100, 100, 3, c)
    c.create_oval(check_x, check_y, check_x, check_y, width=10, fill="black")

    area_of_triangle(x1, y1, x2, y2, x3, y3)
    print("Pole trojkata wynosi: " + str(area_of_triangle(x1, y1, x2, y2, x3, y3)))
    check_if_point_inside_triangle(x1, y1, x2, y2, x3, y3, check_x, check_y)

    c.pack()
    root.mainloop()