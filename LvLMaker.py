import pygame
from Builder import MapBuilder
from Builder import Gun_PowerUpBuilder
from Builder import SolidObject_Builder
from Builder import PlayerBuilder
from Builder import Goomba_EnemyBuilder
from Builder import ButtonBuilder
from Builder import Mushroom_PowerUpBuilder
from Builder import TextBoxBuilder
from GameStates import GameStateManager
from Builder import Door_Builder
from GameStates import GameStates
from Text import TextTypes



class LevelMaker():
    def __init__(self, gameWorld):
        
        self._gameWorld = gameWorld
        self._mapbuilder=MapBuilder(self._gameWorld)
        

    def Level_One_map(self):

        
        self._mapbuilder.build()
        for mapitem in self._mapbuilder.get_gameObject():
            self._gameWorld._lvl1_Objects.append(mapitem)
#PLAYER
        builder = PlayerBuilder(self._gameWorld)
        builder.build(self._gameWorld)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())
#PLAYER

#ENEMIES
        builder = Goomba_EnemyBuilder(self._gameWorld)
        builder.build(200, 100)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(600, 560)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(600,200)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

#ENEMIES

#POWER UPS
        builder = Mushroom_PowerUpBuilder(self._gameWorld)
        builder.build()
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder=Gun_PowerUpBuilder(self._gameWorld)
        builder.build(pygame.math.Vector2(300,560))
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

#POWER UPS

# DOORS
        builder = Door_Builder(self)
        builder.build(4600, 500, GameStates.LVL2)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())
#DOORS
        
# BLOCKS
        builder=SolidObject_Builder(self)

        for i in range(5):
            builder.build(400+i*50,400,"mario_block.png")
            self._gameWorld._lvl1_Objects.append(builder.get_gameObject())


#GROUND
        for i in range(30):
            builder.build(0 + i*50,600,"ground.png")
            self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        for i in range(30):
            builder.build(1700 + i*50,600,"ground.png")
            self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        for i in range(30):
            builder.build(3500 + i*50,600,"ground.png")
            self._gameWorld._lvl1_Objects.append(builder.get_gameObject())
#GROUND
        

#BLOCKS
        

     


    
  
   
