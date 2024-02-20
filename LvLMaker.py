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
from SolidObject import SolidObjectType


class LevelMaker():
    
    

    def __init__(self, gameWorld):
        
        self._gameWorld = gameWorld
        self._mapbuilder=MapBuilder(self._gameWorld)
        self._clock = pygame.time.Clock()

        
        

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

        builder.build(1600,550)
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

        builder.build(-50, -70,"mario_block.png", 720, 50, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        
        builder.build(700,400,"mario_block.png", 50, 200, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(1000,400,"mario_block.png", 50, 200, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(850,200,"mario_block.png", 50, 200, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())




        builder.build(2420,200,"mario_block.png", 50, 200, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(2060,200,"mario_block.png", 50, 200, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(2280,400,"mario_block.png", 50, 200, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        builder.build(4000,400,"mario_block.png", 50, 200, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())


        builder.build(4400, 280,"mario_block.png", 320, 50, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())



        builder.build(4900, -70,"mario_block.png", 720, 50, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        


#GROUND
        
        builder.build(0 ,600,"ground.png", 50, 1400, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        
        builder.build(1500 ,600,"ground.png", 50, 700, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())
        
        builder.build(2720 ,600,"ground.png", 50, 600, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())

        
        builder.build(3500 ,600,"ground.png", 50, 1400, SolidObjectType.normal)
        self._gameWorld._lvl1_Objects.append(builder.get_gameObject())
#GROUND
        

#BLOCKS
        

    def Level_Two_map(self):

        
        
#PLAYER
        builder = PlayerBuilder(self._gameWorld)
        builder.build(self._gameWorld)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())
#PLAYER

#ENEMIES
        builder = Goomba_EnemyBuilder(self._gameWorld)
        builder.build(3000, 550)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        builder.build(600, 550)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        builder.build(1600,550)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

#ENEMIES

#POWER UPS
        builder = Mushroom_PowerUpBuilder(self._gameWorld)
        builder.build()
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        builder=Gun_PowerUpBuilder(self._gameWorld)
        builder.build(pygame.math.Vector2(300,560))
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        builder.build(pygame.math.Vector2(350,560))
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())


        builder.build(pygame.math.Vector2(2160,420))
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())

#POWER UPS

# DOORS
        builder = Door_Builder(self)
        builder.build(4600, 500, GameStates.BOSSLVL)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())
#DOORS
        
# BLOCKS
        builder=SolidObject_Builder(self)

        builder.build(-50, -70,"mario_block.png", 720, 50, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())


        builder.build(750, -70,"mario_block.png", 560, 50, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        builder.build(1000, -70,"mario_block.png", 720, 50, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        
        




        builder.build(2940,100,"mario_block.png", 50, 200, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        builder.build(2060,500,"mario_block.png", 50, 200, SolidObjectType.moveX)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        builder.build(2520,300,"mario_block.png", 50, 200, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())



        builder.build(4050,400,"mario_block.png", 50, 100, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())


       


        builder.build(4900, -70,"mario_block.png", 720, 50, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())






        builder.build(4050, -70,"mario_block.png", 560, 50, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        builder.build(4400, -70,"mario_block.png", 720, 50, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        


#GROUND
        
        builder.build(0 ,600,"ground2.png", 50, 1400, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        
        builder.build(1500 ,600,"ground2.png", 50, 500, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())
        
        builder.build(2720 ,600,"ground2.png", 50, 500, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())

        
        builder.build(3500 ,600,"ground2.png", 50, 1400, SolidObjectType.normal)
        self._gameWorld._lvl2_Objects.append(builder.get_gameObject())
#GROUND
        

#BLOCKS
        
    def Level_Boss_map(self):

#PLAYER
        builder = PlayerBuilder(self._gameWorld)
        builder.build(self._gameWorld)
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())
#PLAYER

#ENEMIES
        builder = Goomba_EnemyBuilder(self._gameWorld)
        builder.build(3000, 550)
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())

#ENEMIES

#POWER UPS
        builder = Mushroom_PowerUpBuilder(self._gameWorld)
        builder.build()
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())

        builder=Gun_PowerUpBuilder(self._gameWorld)
        builder.build(pygame.math.Vector2(300,560))
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())

        

#POWER UPS

# DOORS
        builder = Door_Builder(self)
        builder.build(4600, 500, GameStates.WIN)
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())
#DOORS
        
# BLOCKS
        builder=SolidObject_Builder(self)

        builder.build(-50, -70,"mario_block.png", 720, 50, SolidObjectType.normal)
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())

        
        
        builder.build(1800 ,140,"ground2.png", 100, 50, SolidObjectType.moveY2)
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())
        
        



        builder.build(2000 ,340,"ground2.png", 100, 50, SolidObjectType.moveY)
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())




        builder.build(4900, -70,"mario_block.png", 720, 50, SolidObjectType.normal)
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())


#GROUND
        
        builder.build(0 ,640,"ground2.png", 50, 2000, SolidObjectType.normal)
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())






        builder.build(2000 ,140,"ground2.png", 50, 500, SolidObjectType.normal)
        self._gameWorld._bossLvl_Objects.append(builder.get_gameObject())

        

        
#GROUND
        

#BLOCKS
        
     


    


    
  
   
