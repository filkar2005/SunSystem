import sys
from panda3d.core import *
import direct.directbase.DirectStart
from direct.task import Task
import time
from direct.gui.DirectGui import *
from phyz import*

global bliz
bliz = 10

base.set_background_color(0, 0, 0, 1)  # цвет фона окна
base.accept('escape', sys.exit)
room = render.attachNewNode("room")
room.setPos(0, 0, 0)
room.reparentTo(render)
base.setFrameRateMeter(True) 

global all_objects
all_objects = []

global FPStime
FPStime = 0

class star(sphere):
    def __init__(self, R, m, coord, name, texture):
        print("инициализация звезды начата")
        super().__init__(R, m, coord, [0, 0, 0], "sphere" + name)
        self.star_name = name
        self.texture = loader.loadTexture(texture)
        self.model = loader.loadModel("textures/планеты/планета.obj")
        self.model.setTexture(self.texture)
        self.model.setScale(R/bliz)
        self.model.setPos(self.coord[0]/bliz, self.coord[1]/bliz, self.coord[2]/bliz)
        self.model.reparentTo(render)
        self.lightpivot = render.attachNewNode("lightpivot")
        self.lightpivot.setPos(self.coord[0]/bliz, self.coord[1]/bliz, self.coord[2]/bliz)
        self.plight = PointLight('plight')
        self.plight.setColor((30, 30, 20, 1))
        self.plnp = self.lightpivot.attachNewNode(self.plight)
        self.plnp.setPos(self.coord[0]/bliz, self.coord[1]/bliz, self.coord[2]/bliz)
        room.setLight(self.plnp)
        self.model.reparentTo(self.plnp)
        room.setShaderAuto()
        self.shaderenable = 1
        print("инициализация звезды закончена")

class planet(sphere):
    def __init__(self, R, m, coord, V, name, texture):
        print("инициализация планеты начата")
        super().__init__(R, m, coord, V, "sphere" + name)
        self.texture = loader.loadTexture(texture)
        self.model = loader.loadModel("textures/планеты/планета.obj")
        self.model.setTexture(self.texture)
        self.model.setScale(R/bliz)
        self.model.setPos(self.coord[0]/bliz, self.coord[1]/bliz, self.coord[2]/bliz)
        self.model.reparentTo(room)
        print("инициализация планеты закончена")
    def update_position(self):
        F = F_Gravity(self.m, all_objects[0].m, len_vector_points(self.coord, all_objects[0]))
        self.V = delta_V(self.V, F, selfm, FPStime)
        self.coord = delta_coord(self.coord, self.V, FPStime)
        self.model.setPos(self.coord[0]/bliz, self.coord[1]/bliz, self.coord[2]/bliz)
    
sun = star(5, 10, [0, 0, 0], "sun", 'textures/планеты/текстуры планет/солнце/13913_Sun_diff.jpg')
all_objects.append(sun)

base.run()
