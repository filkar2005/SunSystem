import math
G = 6.67 * (10**(-17))
class vector3D:
    vect = [0, 0, 0]
    def __init__(self, vect):
        if list == type(vect):
            self.vect = vect
        else:
            print("!!!WARNING!!!", vect, "isn't a vector (it must be list). The default null vector is taken as the value")
    def __add__(self, vect2):
        vector_rezult = [None, None, None]
        vector_rezult[0] = self.vect[0] + vect2.vect[0]
        vector_rezult[1] = self.vect[1] + vect2.vect[1]
        vector_rezult[2] = self.vect[2] + vect2.vect[2]
        return vector3D(vector_rezult)
    def __sub__(self, vect2):
        vector_rezult = [None, None, None]
        vector_rezult[0] = self.vect[0] - vect2.vect[0]
        vector_rezult[1] = self.vect[1] - vect2.vect[1]
        vector_rezult[2] = self.vect[2] - vect2.vect[2]
        return vector3D(vector_rezult)
    def __mul__(self, chislo):
        vector_rezult = [None, None, None]
        vector_rezult[0] = self.vect[0] * chislo
        vector_rezult[1] = self.vect[1] * chislo
        vector_rezult[2] = self.vect[2] * chislo
        return vector3D(vector_rezult)
    def __truediv__(self, chislo):
        vector_rezult = [None, None, None]
        vector_rezult[0] = self.vect[0] / chislo
        vector_rezult[1] = self.vect[1] / chislo
        vector_rezult[2] = self.vect[2] / chislo
        return vector3D(vector_rezult)
    
    def leng(self):
        rezult = math.sqrt(self.vect[0]**2 + self.vect[1]**2 + self.vect[2]**2)
        return rezult
    
def gravity(m1, m2, coord1, coord2):
    R = coord2 - coord1
    r = R.leng()
    F = (m1 * m2 * G)/(r**3)
    F = R*F
    return F
def delta_V(m, V, F, timeFPS):
    a = F / m
    V = V + a * timeFPS
    return V
def delta_coord(coord, V, timeFPS):
    new_coord = coord + V * timeFPS
    return new_coord