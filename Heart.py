from Components import Component

import pygame

class Mushroom_PowerUp(Component):

    def awake(self,game_world):

        self.sr = self.gameObject.get_component("SpriteRenderer")
        #sr.sprite_image("shield")
        self.gameObject.transform.position = pygame.math.Vector2(50,50)
        
        collider = self._gameObject.get_component("Collider")


    
    def start(self):
        return super().start()
    
    def update(self, delta_time):
        return super().update(delta_time)
    


