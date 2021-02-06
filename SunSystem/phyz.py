import numpy as np

global G
G = 6.6743015 * 10**(-11)

len_vector_points = lambda x, y: np.sqrt(np.sum((y - x)**2))
len_vector = lambda x: np.sqrt(np.sum((x)**2))
F_Gravity = lambda m1, m2, r: (G * m1 * m2 * r)/(len_vector(r)**3)  # эти 3 функции точно работают правильно.

class point:
    def __init__(self, m, coord, V, name):
        self.m = m
        self.V = np.array(V)
        self.coord = np.array(coord)
        self.point_name = name
    def infa_point(self):
        print("точка", self.point_name + ":")
        print("    m =", self.m)
        print("    coord =", self.coord)
        print("    V =", self.V)
        print("-----------------------------")

class sphere(point):
    def __init__(self, R, m, coord, V, name):
        super().__init__(m, coord, V, "point_" + name)
        self.R = R
        self.sphere_name = name
    def infa_sphere(self):
        print("сфера", self.sphere_name + ":")
        print("  R =", self.R)
        self.infa_point()
        print("---------------------------------")
    def point_in_sphere(self, Point):
        r = len_vector_points(Point.coord, self.coord)
        print(r)
        return r <= self.R

def delta_V(V, F, m, FPStime):
    a = F/m
    V = V + a * FPStime
    return V

def delta_coord(coord, V, FPStime):
    coord = coord + V*FPStime
    return coord
