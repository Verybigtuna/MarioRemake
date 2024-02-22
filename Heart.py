from Components import Component
from Player import Player

import pygame

class Heart1(Component):
    


        
    def awake(self,game_world):
        self._game_world = game_world   

        self.sr = self.gameObject.get_component("SpriteRenderer")
        #sr.sprite_image("shield")

     
        collider = self._gameObject.get_component("Collider")


    
    def start(self):
        pass
    
    def update(self, delta_time):

        if Player.health == 2:
            self.gameObject.destroy()



class Heart2(Component):
    


        
    def awake(self,game_world):
        self._game_world = game_world   

        self.sr = self.gameObject.get_component("SpriteRenderer")
        #sr.sprite_image("shield")

     
        collider = self._gameObject.get_component("Collider")


    
    def start(self):
        pass
    
    def update(self, delta_time):

        if Player.health == 1:
            self.gameObject.destroy()
            
class Heart3(Component):
    


        
    def awake(self,game_world):
        self._game_world = game_world   

        self.sr = self.gameObject.get_component("SpriteRenderer")
        #sr.sprite_image("shield")

     
        collider = self._gameObject.get_component("Collider")


    
    def start(self):
        pass
    
    def update(self, delta_time):

        if Player.health == 0:
            self.gameObject.destroy()




        
    


