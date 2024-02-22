from Components import Component
import random
import pygame
from Score import GameScore
from Components import SoundPlayer

class Goomba_Enemy(Component):

    def __init__(self,pos_x,pos_y) -> None:
        self._pos_x=pos_x
        self._pos_y=pos_y
    

    def awake(self, game_world):
        sr = self.gameObject.get_component("SpriteRenderer")


        self._screen_size = pygame.math.Vector2(game_world._screen.get_width(), game_world._screen.get_height())

        self.gameObject.transform.position =pygame.math.Vector2(self._pos_x,self._pos_y)
        
        self._spawnPosition_x=self._pos_x
        collider = self._gameObject.get_component("Collider")
        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)

        collider.subscribe("collision_enter_top",self.on_collision_enter_top)
        collider.subscribe("collision_exit_top",self.on_collision_exit_top)

        collider.subscribe("collision_projectile",self.on_collision_projectile)

        self.gameObject.Tag = "Enemy"
        self._speed=250
        

    def start(self):
        pass

    def update(self, delta_time):
       
        self.simple_move_pattern(delta_time)

        bottom_limit = self._screen_size.y
        if self._gameObject.transform.position.y > bottom_limit:
            self._gameObject.destroy()


    def simple_move_pattern(self,delta_time):

        if(self.gameObject.transform.position.x>self._spawnPosition_x+100):
         self._speed=-250
         
         
        elif(self.gameObject.transform.position.x<self._spawnPosition_x-100):
            self._speed=250
            
        movement = pygame.math.Vector2(self._speed,0)

        self.gameObject.transform.translate(movement*delta_time)

    def on_collision_enter(self,other):
      pass

    def on_collision_exit(self,other):
      pass


    def on_collision_enter_top(self, other):
        self.sound_player = SoundPlayer("stomp.wav")
        self.sound_player.play_sound()  
        self.sound_player.set_volume(0.05)

        
        self.gameObject.destroy()
        GameScore.score += 100

    def on_collision_projectile(self,other):
       
       self.gameObject.destroy()
       other.gameObject.destroy()


    def on_collision_exit_top(self,other):
     pass
        



        
