import direct.directbase.DirectStart
base.cam.setPos(0, -100, 0)
base.cam.lookAt(0, 0, 0)
base.camLens.setNearFar(1, 10000)
base.set_background_color(0, 0, 0, 1)  # цвет фона окна
class MyApp:   
    def __init__(self):     
        self.model = loader.loadModel("/home/filaret/proba1/textures/космолёт/боевой_корабль/X fighter.obj")   
        self.texture = loader.loadTexture("/home/filaret/proba1/textures/космолёт/двиг вкл.jpg")
        self.model.setTexture(self.texture)
        self.model.reparentTo(render)   
        self.model.setScale(1, 1, 1)   
        self.model.setPos(0, 0, 0)   
      
      
app = MyApp()   
base.run() 