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
        builder.build(3000, 550)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(600, 550)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(1400,550)
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

        builder.build(-50, -70,"mario_block.png", 720, 50)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        
        builder.build(700,400,"mario_block.png", 50, 200)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(1000,400,"mario_block.png", 50, 200)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(850,200,"mario_block.png", 50, 200)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())




        builder.build(2620,200,"mario_block.png", 50, 200)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(2260,200,"mario_block.png", 50, 200)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(2480,400,"mario_block.png", 50, 200)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())






        builder.build(4900, -70,"mario_block.png", 720, 50)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        


#GROUND
        
        builder.build(0 ,600,"ground.png", 50, 1400)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        
        builder.build(1400 ,600,"ground.png", 50, 1000)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())
        
        builder.build(2720 ,600,"ground.png", 50, 600)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        
        builder.build(3500 ,600,"ground.png", 50, 1400)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())
#GROUND
        

#BLOCKS
        

     


    
  
   
