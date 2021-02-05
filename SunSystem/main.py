 #Не забудь! все вектора vector3D  
import sys
from panda3d.core import *
import direct.directbase.DirectStart
import numpy as np
import phyz as p
from direct.task import Task
import time
from direct.gui.DirectGui import *
import infa

global bliz
bliz = 1000
base.set_background_color(0, 0, 0, 1)  # цвет фона окна
base.accept('escape', sys.exit)
room = render.attachNewNode("room")
room.setPos(0, 0, 0)
room.reparentTo(render)
base.setFrameRateMeter(True) 
global all_objects
all_objects = []
class planet:
    def __init__(self, m, R, V, coord, texture):
        print("инициализация планеты начата")
        global bliz
        self.m = m
        self.R = R
        self.V = V
        self.coord = coord
        self.texture = loader.loadTexture(texture)
        self.model = loader.loadModel("textures/планеты/планета.obj")
        self.model.setTexture(self.texture)
        self.model.setScale(R/bliz)
        self.model.setPos(self.coord.vect[0], self.coord.vect[1], self.coord.vect[2])
        self.model.reparentTo(room)
        print("инициализация планеты закончена")
    def dvij(self):
        global bliz
        F = p.gravity(self.m, sun.m, self.coord, sun.coord)
        self.V = p.delta_V(self.m, self.V, F, timeFPS)
        self.coord = p.delta_coord(self.coord, self.V, timeFPS)
        self.model.setPos(self.coord.vect[0]/bliz, self.coord.vect[1]/bliz, self.coord.vect[2]/bliz)
class sputnik:
    def __init__(self, m, R, V, coord, texture, planet):
        print("инициализация спутника начата")
        global bliz
        self.planet = planet
        self.m = m
        self.R = R
        self.V = V
        self.coord = coord
        self.texture = loader.loadTexture(texture)
        self.model = loader.loadModel("textures/планеты/планета.obj")
        self.model.setTexture(self.texture)
        self.model.setScale(R/bliz)
        self.model.setPos(self.coord.vect[0], self.coord.vect[1], self.coord.vect[2])
        self.model.reparentTo(room)
        print("инициализация спутника закончена")
    def dvij(self):
        F1 = p.gravity(self.m, self.planet.m, self.coord, self.planet.coord)
        F2 = p.gravity(self.m, sun.m, self.coord, sun.coord)
        F = F1 + F2
        self.V = p.delta_V(self.m, self.V, F, timeFPS)
        self.coord = p.delta_coord(self.coord, self.V, timeFPS)
        self.model.setPos(self.coord.vect[0]/bliz, self.coord.vect[1]/bliz, self.coord.vect[2]/bliz)

class sunclass:
    def __init__(self, m, R, coord, texture):
        print("инициализация звезды начата")
        global bliz
        self.m = m
        self.R = R
        self.coord = coord
        self.texture = loader.loadTexture(texture)
        self.model = loader.loadModel("textures/планеты/планета.obj")
        self.model.setTexture(self.texture)
        self.model.setScale(R/bliz)
        self.model.setPos(self.coord.vect[0], self.coord.vect[1], self.coord.vect[2])
        self.model.reparentTo(render)
        self.lightpivot = render.attachNewNode("lightpivot")
        self.lightpivot.setPos(0, 0, 0)
        self.plight = PointLight('plight')
        self.plight.setColor((30, 30, 20, 1))
        self.plnp = self.lightpivot.attachNewNode(self.plight)
        self.plnp.setPos(0, 0, 0)
        room.setLight(self.plnp)
        self.model.reparentTo(self.plnp)
        
        room.setShaderAuto()

        self.shaderenable = 1
        print("инициализация звезды закончена")

# point2 - координаты относительно point1.
#coord1 + point2 = [3, 3, 3] + [1, 1, 0]
#coord2 = [4, 4, 3]
class rocket:
    def __init__(self, m, coord1, point2, V_all):
        print("инициализация ракеты начата") 
        self.m = m
        self.coord1 = coord1
        self.point2 = point2
        self.R = point2.leng()
        self.V_all = V_all
        self.V1 = V_all
        self.V2 = V_all
        self.F = p.vector3D([0, 0, 0])
        self.coord2 = self.coord1 + self.point2
        base.cam.setPos(self.coord1.vect[0]/bliz, self.coord1.vect[1]/bliz, self.coord1.vect[2]/bliz)
        base.cam.lookAt(self.coord2.vect[0]/bliz, self.coord2.vect[1]/bliz, self.coord2.vect[2]/bliz)
        base.camLens.setNearFar(1, 1000000)
        base.disableMouse()
        self.Fplus = p.vector3D([0, 1000, 0])
        print("инициализация ракеты законченна")
    def pravka_point2(self):
        self.point2 = (self.point2 / self.point2.leng()) * self.R
    def gravity_rocket(self):
        F = p.vector3D([0, 0, 0])
        for i in all_objects:
            F = F + p.gravity(self.m, i.m, self.coord1, i.coord)
        return F
    def cam_pos(self):
        base.cam.setPos(self.coord1.vect[0]/bliz, self.coord1.vect[1]/bliz, self.coord1.vect[2]/bliz)
        base.cam.lookAt(self.coord2.vect[0]/bliz, self.coord2.vect[1]/bliz, self.coord2.vect[2]/bliz)
    def dvij(self):
        F = self.gravity_rocket() + self.F
        self.V_all = p.delta_V(self.m, self.V_all, F, timeFPS)
        self.coord1 = p.delta_coord(self.coord1, self.V_all, timeFPS)
        self.coord2 = p.delta_coord(self.coord2, self.V_all, timeFPS)
        self.cam_pos()
        print(int(self.V_all.leng()))
        print(self.F.vect)
    def plus_F(self):
        self.F = self.F + self.Fplus
    def minus_F(self):
        self.F = self.F - self.Fplus
        
sun = sunclass(1.9891*(10 ** 30), 1392000, p.vector3D([0, 0, 0]), 'textures/планеты/текстуры планет/солнце/13913_Sun_diff.jpg')
zemla = planet(5.97 * (10 ** 24), 12770.6, p.vector3D([0, 0, 0]), p.vector3D([149600000, 0, 0]), 'textures/планеты/текстуры планет/земля/Diffuse_2K.png')
loon = sputnik(7.35 * (10 ** 15), 3547.4, p.vector3D([0, 0, 0]), p.vector3D([149984403, 0, 0]), 'textures/планеты/текстуры планет/луна/Bump_2K.png', zemla)
racketa = rocket(1000000, p.vector3D([149600000, -200000, 0]), p.vector3D([0, 5, 0]), p.vector3D([0, 500, 0]))

all_objects.append(sun)
all_objects.append(zemla)
all_objects.append(loon)

global time0, time1, timeFPS
time0 = time.time()
def update(task):
    global time0, time1, timeFPS
    time1 = time.time()
    timeFPS = time1 - time0
    zemla.dvij()
    loon.dvij()
    racketa.dvij()
    time0 = time1
    return task.cont
base.accept('arrow_up-repeat', racketa.plus_F)
base.accept('arrow_down-repeat', racketa.minus_F)
taskMgr.add(update, 'update')
base.run()
#луна - земля - солнце (соотношения радиусов)
#1 - 3,6 - 392,4  *1000000
#m - в килограммах