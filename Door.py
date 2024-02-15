import pygame
from Components  import Component
from GameStates import GameStateManager
from GameStates import GameStates





class Lvl_Door(Component):

    def __init__(self,pos_x,pos_y, game_state_enum) -> None:
        self._pos_x=pos_x
        self._pos_y=pos_y
        self._game_state_enum = game_state_enum
    

    def awake(self, game_world):
        sr = self.gameObject.get_component("SpriteRenderer")


        self._screen_size = pygame.math.Vector2(game_world._screen.get_width(), game_world._screen.get_height())

        self.gameObject.transform.position =pygame.math.Vector2(self._pos_x,self._pos_y)
        
        self._spawnPosition_x=self._pos_x
        collider = self._gameObject.get_component("Collider")
        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)



    def start(self):
        pass

    def update(self, delta_time):
       pass



    def simple_move_pattern(self,delta_time):
        pass

    def on_collision_enter(self, other):
      GameStateManager.currentState = self._game_state_enum

    def on_collision_exit(self,other):
      pass


    def on_collision_enter_top(self, other):
        pass


    def on_collision_exit_top(self,other):
     pass
        