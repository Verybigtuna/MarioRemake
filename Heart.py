from Components import Component

import pygame

class Heart(Component):


        
    def awake(self,game_world):
        self._game_world = game_world   

        self.sr = self.gameObject.get_component("SpriteRenderer")
        #sr.sprite_image("shield")

     
        collider = self._gameObject.get_component("Collider")


    
    def start(self):
        pass
    
    def update(self, delta_time):

        if self.gameObject.health == 2:
            self.gameObject.destroy()

        if self.gameObject.health == 1:
            self.gameObject.destroy()
        
    


