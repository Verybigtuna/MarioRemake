import pygame
from Components  import Component
from GameStates import GameStateManager
from GameStates import GameStates
from enum import Enum




class TextTypes(Enum):
    WELCOME = 1
    YOURDEAD = 2
    YOUWIN = 3
    GUIDE = 4
    WALLGUIDE = 5
    

class TextBox(Component):

    
    def __init__(self,pos_x,pos_y, textType) -> None:
        self._pos_x=pos_x
        self._pos_y=pos_y
        self._textType = textType
       
    def awake(self, game_world):
        

        self.gameObject.Tag = "text"

        
        self._screen_size = pygame.math.Vector2(game_world._screen.get_width(), game_world._screen.get_height())

        self.gameObject.transform.position =pygame.math.Vector2(self._pos_x,self._pos_y)
        
        self._spawnPosition_x=self._pos_x
        self._rect = self.gameObject.get_component("SpriteRenderer").sprite.rect
        collider = self._gameObject.get_component("Collider")


        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)



    def start(self):
        pass

    def update(self, delta_time):
        pass

    
    def on_collision_enter(self, other):
      pass

    def on_collision_exit(self,other):
      pass


    def on_collision_enter_top(self, other):
        pass


    def on_collision_exit_top(self,other):
     pass
        
