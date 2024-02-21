import pygame
from Components import Component
from enum import Enum
from GameStates import GameStateManager
from GameStates import GameStates

class SolidObjectType(Enum):
   normal = 1
   moveX = 2
   moveY = 3
   moveY2 = 4
   death = 5


class SolidObject(Component):


    currentObjectType = SolidObjectType.normal

    
    def __init__(self,pos_x,pos_y, objectType) -> None:
        self._pos_x=pos_x
        self._pos_y=pos_y
        self._objectType = objectType
        
    

    def awake(self, game_world):
        sr = self.gameObject.get_component("SpriteRenderer")

        self.gameObject.Tag = "SolidObject"


        self._screen_size = pygame.math.Vector2(game_world._screen.get_width(), game_world._screen.get_height())

        self.gameObject.transform.position =pygame.math.Vector2(self._pos_x,self._pos_y)
        
        self._spawnPosition_x=self._pos_x
        self._spawnPosition_y=self._pos_y
        collider = self._gameObject.get_component("Collider")
        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)
        collider.subscribe("collision_enter_top",self.on_collision_enter_top)
        self._speed=150

        if self._objectType == SolidObjectType.moveY2:
           self._spawnPosition_y += 100



    def start(self):
        pass

    def update(self, delta_time):
       if self._objectType == SolidObjectType.moveX:
          self.simple_move_pattern_x(delta_time)
        
       if self._objectType == SolidObjectType.moveY:
          self.simple_move_pattern_y(delta_time)
        
       if self._objectType == SolidObjectType.moveY2:
          self.simple_move_pattern_y2(delta_time)


    def simple_move_pattern_x(self,delta_time):
        
        if(self.gameObject.transform.position.x>self._spawnPosition_x+100):
         self._speed=-150
         
        elif(self.gameObject.transform.position.x<self._spawnPosition_x-100):
            self._speed=150
            
        movement = pygame.math.Vector2(self._speed,0)

        self.gameObject.transform.translate(movement*delta_time)


    def simple_move_pattern_y(self,delta_time):
        
        if(self.gameObject.transform.position.y>self._spawnPosition_y+100):
         self._speed=-150
         
        elif(self.gameObject.transform.position.y<self._spawnPosition_y-100):
            self._speed=150
            
        movement = pygame.math.Vector2(0,self._speed)

        self.gameObject.transform.translate(movement*delta_time)


    def simple_move_pattern_y2(self,delta_time):

       
         
        if(self.gameObject.transform.position.y<self._spawnPosition_y-100):
            self._speed=150

        elif(self.gameObject.transform.position.y>self._spawnPosition_y+100):
            self._speed=-150
            
        movement = pygame.math.Vector2(0,self._speed)

        self.gameObject.transform.translate(movement*delta_time)

    def on_collision_enter(self, other):
      pass

    def on_collision_exit(self,other):
      pass


    def on_collision_enter_top(self, other):
      if self._objectType == SolidObjectType.death:
         other.gameObject.destroy()
         GameStateManager.currentState = GameStates.RESTART
       


    def on_collision_exit_top(self,other):
     pass

