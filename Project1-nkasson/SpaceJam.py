import sys, math
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from direct.gui.DirectGui import *


class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.accept('escape', self.quit)        
        self.universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.universe.setScale(10000)  
        self.universe.setColorScale(1.0,0.5,0.3,1.0)
        self.universe.reparentTo(self.render)
        #Breakdown of model loading: Self, Model file, Scale, X pos, Y pos, Z pos, Texture file, Yaw, Pitch, Rotation

        self.planet1 = SpaceJam.addAdditionalModel(
            self,   "./Assets/Planets/protoPlanet.x",   230,    2832,   -512,   0,    
            "./Assets/Planets/pluto.jpg",0,0,0)
        self.planet2 = SpaceJam.addAdditionalModel(
            self,   "./Assets/Planets/protoPlanet.x",   40,     767,    452,    0,       
            "./Assets/Planets/jupiter.jpg",0,0,0)      
        self.planet3 = SpaceJam.addAdditionalModel(
            self,   "./Assets/Planets/protoPlanet.x",   110,    3290,   -2172,  0,   
            "./Assets/Planets/moonLike.jpg",0,0,0)
        self.planet4 = SpaceJam.addAdditionalModel(
            self,   "./Assets/Planets/protoPlanet.x",   120,    -2864,  -3672,  0,  
            "./Assets/Planets/orangePlanet.jpg",0,0,0)    
        self.planet4 = SpaceJam.addAdditionalModel(
           self,   "./Assets/Planets/redPlanet.x",      80,     -800,   800,    0,          
            "./Assets/Planets/redPlanet.jpg",0,0,0) 
        self.planet5 = SpaceJam.addAdditionalModel(
           self,   "./Assets/Planets/protoPlanet.x",    65,     390,    -820,   0,
            "./Assets/Planets/yellowPlanet.png",0,0,0)
        self.planet6 = SpaceJam.addAdditionalModel( 
           self,   "./Assets/Planets/protoPlanet.x",    80,     1200,   -1850,  0,
            "./Assets/Planets/bluePlanet.jpg",0,0,0)
        self.planet7 = SpaceJam.addAdditionalModel(
           self,   "./Assets/Planets/protoPlanet.x",    58,     1890,  -2200,  0,     
        "./Assets/Planets/velvetPlanet.png",0,0,0)
        self.planet8 = SpaceJam.addAdditionalModel(
           self,   "./Assets/Planets/protoPlanet.x",    115,    -670,   -100,   0,
        "./Assets/Planets/healthyPlanet.png",0,0,0)
        self.station1 = SpaceJam.addAdditionalModel(
            self,   "./Assets/station/spaceStation.x", 5,-3064.0,-3472.0, 0.0, 
            "./Assets/station/SpaceStation1_Dif2.png",40,90,0)
        self.station2 = SpaceJam.addAdditionalModel(
            self,   "./Assets/station/spaceStation.x", 6, 610.0,472.0,40.0,      
            "./Assets/station/SpaceStation1_Dif2.png",0,90,0)
        # self.stationtest = SpaceJam.addAdditionalModel(
        #     self,   "./Assets/station/spaceStation.x", 0.2,0.0,20.0,0.0,       
        # "./Assets/station/SpaceStation1_Dif2.png",0,90,0)
        #was used to test yaw and rotation to get a "correct orientation station" 
        self.ship1 = SpaceJam.addAdditionalModel(
            self,   "./Assets/blorg/theBorg.x",     1,558,557,29,                 
            "./Assets/blorg/small_space_ship_2_color.jpg",10,90,20)
        self.ship2 = SpaceJam.addAdditionalModel(
            self,   "./Assets/blorg/theBorg.x",     1,631,532,2,                 
            "./Assets/blorg/small_space_ship_2_color.jpg",3,90,80)
        self.ship3 = SpaceJam.addAdditionalModel(
            self,   "./Assets/blorg/theBorg.x",     1,700,312,36,                 
            "./Assets/blorg/small_space_ship_2_color.jpg",4,90,120)
        self.ship4 = SpaceJam.addAdditionalModel(
            self,   "./Assets/blorg/theBorg.x",     1,692,42,8,                 
            "./Assets/blorg/small_space_ship_2_color.jpg",1,90,60)
        self.ship5 = SpaceJam.addAdditionalModel(
            self,   "./Assets/blorg/theBorg.x",     0.7,0,70,8,                 
            "./Assets/blorg/small_space_ship_2_color.jpg",0,90,30)
        #i wanted to add more spaceships to add a bit of a feel like it's lively
    def addAdditionalModel(self,ModelFile,scale,CoordX,CoordY,CoordZ,TextureFile,Yaw,Pitch,Rotation):
        new_obj = self.loader.loadModel(ModelFile) 
        new_obj.setScale(scale)
        new_obj.setColorScale(1.0,1.0,1.0,1.0)
        new_obj.reparentTo(self.render)
        new_obj.setPos(CoordX,CoordY,CoordZ)
        new_obj_tex = self.loader.loadTexture(TextureFile)
        new_obj.setTexture(new_obj_tex)
        new_obj.setHpr(Yaw,Pitch,Rotation)
        
    def quit(self):
        sys.exit()
app = SpaceJam()
app.run()
