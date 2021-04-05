class Line:
    def __init__(self, coor1, coor2):  # object creation accepting the coordinates of a line as arguments
        self.coor1 = coor1  # x1 , y1
        self.coor2 = coor2  # x2 , y2

    def distance(self):  # calculating distance of a line
        x1, y1 = self.coor1  # tuple unpacking to assign coordinates
        x2, y2 = self.coor2  # ||
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    def slope(self):  # calculating slope of a line
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


# Line Tests
coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())

print(li.slope())


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1): # object creation to accept height and radius of a cylinder
        self.height = height
        self.radius = radius

    def volume(self):
        # volume of a cylinder = pi(r)^2(h)
        return Cylinder.pi * self.radius**2 * self.height

    def surface_area(self):
        # surface area of a cylinder = 2 pi (r)(h) + 2 pi (r)^2
        return (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * self.radius**2)


# Cylinder Tests
c = Cylinder(2, 3)

print(c.volume())

print(c.surface_area())

