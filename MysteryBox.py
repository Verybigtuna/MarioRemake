from Components import Component

import random
import pygame



class MysteryBox(Component):

    def __init__(self,pos_x,pos_y) -> None:
        self._pos_x=pos_x
        self._pos_y=pos_y
    

    def awake(self, game_world):
        sr = self.gameObject.get_component("SpriteRenderer")

        self._game_world=game_world

        self._mysteryBox_used=False


        self._screen_size = pygame.math.Vector2(game_world._screen.get_width(), game_world._screen.get_height())

        self.gameObject.transform.position =pygame.math.Vector2(self._pos_x,self._pos_y)
        
        self._spawnPosition_x=self._pos_x
        collider = self._gameObject.get_component("Collider")
        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)

        collider.subscribe("on_collision_enter_bottom",self.on_collision_enter_bottom)
        collider.subscribe("collision_exit_bottom",self.on_collision_exit_bottom)

        self._random=random.randint(1,3)

      

        self.gameObject.Tag = "MysteryBox"
       
        

    def start(self):
        pass

    def update(self, delta_time):
       
        pass


   
    def on_collision_enter(self,other):
      pass

    def on_collision_exit(self,other):
      pass


    def on_collision_enter_bottom(self, other):
       if self._mysteryBox_used==False:
         if self._random==1:
             from Builder import Mushroom_PowerUpBuilder
             builder= Mushroom_PowerUpBuilder(self._game_world)
         elif self._random==2:
              from Builder import Gun_PowerUpBuilder
              builder=Gun_PowerUpBuilder(self._game_world)
         elif self._random==3:
              from Builder import CoinBuilder
              builder=CoinBuilder(self._game_world)
         
       

         spawn_offset_y=-40


         camoffset=self.gameObject.transform.offset


         builder.build(self._pos_x-camoffset.x,self._pos_y+spawn_offset_y-camoffset.y)

         self._game_world.instantiate(builder.get_gameObject())


         sr=self.gameObject.get_component("SpriteRenderer")
         
         sprite_image = pygame.image.load(f"Assets\\{"Empty_Block.png"}").convert_alpha()

         sprite_height_upgrade =50
         sprite_width_upgrade = 50
       
         sr._sprite_image=pygame.transform.scale(sprite_image,(sprite_height_upgrade,sprite_width_upgrade))
         #sr._sprite.rect = sr._sprite_image.get_rect()
         #sr._sprite_mask = pygame.mask.from_surface(sr._sprite_image)

         

         self._mysteryBox_used=True


 

    def on_collision_exit_bottom(self,other):
     pass
        

