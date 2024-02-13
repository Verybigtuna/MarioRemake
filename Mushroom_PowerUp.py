from Components import Component

import pygame

class Mushroom_PowerUp(Component):

    def awake(self,game_world):

        sr = self.gameObject.get_component("SpriteRenderer")
        #sr.sprite_image("shield")
        self.gameObject.transform.position = pygame.math.Vector2(0,0)
        
        collider = self._gameObject.get_component("Collider")
        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)
        collider.subscribe("collision_enter_powerUp",self.on_collision_enter)
        collider.subscribe("collision_exit_powerUp",self.on_collision_exit)
        
    
    def start(self):
        return super().start()
    
    def update(self, delta_time):
        return super().update(delta_time)
    

    def on_collision_enter(self, other):
        print("collision enter my penis")
        self.gameObject.destroy()

    def on_collision_exit(self,other):
        print("collision exit")

    def on_collision_enter_powerUp(self,other):
        
        print("collision enter powered up")

    def on_collision_exter_powerUp(self,other):
        pass
        
