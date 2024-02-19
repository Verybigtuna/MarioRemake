from abc import ABC, abstractclassmethod
from GameObject import GameObject
from Components import Animator
from Components import SpriteRenderer
from Components import MapRenderer
from Player import Player
from Enemy import Enemy
from Goomba_Enemy import Goomba_Enemy
from Mushroom_PowerUp import Mushroom_PowerUp
import pygame
import random
from Components import Collider
from Door import Lvl_Door
from Button import MarioButton
from Text import TextBox
from SolidObject import SolidObject



from Gun_PowerUp import Gun_PowerUp
class Builder(ABC):

    @abstractclassmethod
    def build(self,game_world):
        pass
    @abstractclassmethod
    def get_gameObject(self) -> GameObject:
        pass


class PlayerBuilder(Builder):

    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

    def build(self,game_world):
        self._gameObject = GameObject(pygame.math.Vector2(0,0),self._game_world)
        #Make sure to add 

        sprite_height=40
        sprite_width=40

        sprite_height_upgrade =70
        sprite_width_upgrade = 70

        self._gameObject.add_component(SpriteRenderer("player.png",sprite_width,sprite_height))
        self._gameObject.add_component(Player(game_world))
        self._gameObject.add_component(Collider())

        animator = self._gameObject.add_component(Animator())
        animator.add_animation("Idleright",sprite_height,sprite_width, "mario_move_right2.png",
                               "mario_move_right3.png",
                               "mario_move_right4.png",
                               "mario_move_right3.png")
        
        animator.add_animation("Upgraderight",sprite_height_upgrade,sprite_width_upgrade, "mario_move_right2.png",
                               "mario_move_right3.png",
                               "mario_move_right4.png",
                               "mario_move_right3.png")
        
        animator.add_animation("Idleleft",sprite_height,sprite_height,"mario_move_left2.png",
                               "mario_move_left3.png",
                               "mario_move_left4.png",
                               "mario_move_left3.png")
        
        animator.add_animation("Upgradeleft",sprite_height_upgrade,sprite_width_upgrade, "mario_move_left2.png",
                               "mario_move_left3.png",
                               "mario_move_left4.png",
                               "mario_move_left3.png")    

        animator.play_animation("Idleright")

    def get_gameObject(self) -> GameObject:
        return self._gameObject
    

class EnemyBuilder(Builder):

    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(0,0),self._game_world)
        
        sprites = ["enemy_01.png", "enemy_02.png", "enemy_03.png"]
        selected_sprite = random.choice(sprites)
        self._gameObject.add_component(SpriteRenderer(selected_sprite))
        self._gameObject.add_component(Enemy())
        self._gameObject.add_component(Collider())

    def get_gameObject(self) -> GameObject:
        return self._gameObject
    
class Goomba_EnemyBuilder(Builder):
    
    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

        

    def build(self,pos_x,pos_y):
        self._gameObject = GameObject(pygame.math.Vector2(0,0),self._game_world)
        
        sprite_height=50
        sprite_width=50

        self._gameObject.add_component(SpriteRenderer("Goompa_move1.png",sprite_width,sprite_height))
        self._gameObject.add_component(Goomba_Enemy(pos_x,pos_y))
        self._gameObject.add_component(Collider())

        
        

      


    def get_gameObject(self) -> GameObject:
        return self._gameObject
        

class Mushroom_PowerUpBuilder(Builder):
    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world


    def build(self):

        sprite_height=100
        sprite_width=100
        self._gameObject = GameObject(pygame.math.Vector2(0,0), self._game_world)
        sprite = "shield.png"

        self._gameObject.add_component(SpriteRenderer(sprite,sprite_width,sprite_height))
        self._gameObject.add_component(Mushroom_PowerUp())
        self._gameObject.add_component(Collider())



    def get_gameObject(self) -> GameObject:
        return self._gameObject
    

class Gun_PowerUpBuilder(Builder):
    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

     
    def build(self,position):

        sprite_height=20
        sprite_width=20
        self._gameObject = GameObject(position, self._game_world)
        sprite = "laser.png"
        
        self._gameObject.add_component(SpriteRenderer(sprite,sprite_width,sprite_height))
        self._gameObject.add_component(Gun_PowerUp())
        self._gameObject.add_component(Collider())

        

    def get_gameObject(self) -> GameObject:
        return self._gameObject
    

class Door_Builder(Builder):
    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

        

    def build(self,pos_x,pos_y, enum):
        self._gameObject = GameObject(pygame.math.Vector2(0,0),self._game_world)
        
        sprite_height=50
        sprite_width=50

        self._gameObject.add_component(SpriteRenderer("supply-crate.png",sprite_width,sprite_height))
        self._gameObject.add_component(Lvl_Door(pos_x, pos_y, enum))
        self._gameObject.add_component(Collider())

        
        

      


    def get_gameObject(self) -> GameObject:
        return self._gameObject


class MapBuilder(Builder):
    def __init__(self, game_world) -> None:
        super().__init__()
        self._gameObjects=[]
        self._game_world=game_world

    def build(self):

        background1=GameObject(pygame.math.Vector2(0,0),self._game_world)
        sprite_height= self._game_world._screen.get_height()
        sprite_width=self._game_world._screen.get_width()

        self._mapRen=background1.add_component(MapRenderer("World1.png",sprite_width,sprite_height))
        

        self._mapRen.add_map("World1", sprite_width, sprite_height, "World1.png",)
        self._mapRen.add_map("shield", sprite_width, sprite_height, "shield.png",)


        self._mapRen.setMap("World1")

        







        self._gameObjects.append(background1)

        pass

    def get_gameObject(self) -> GameObject:
        return self._gameObjects
    

    def set_map(self,name):
        self._mapRen.setMap(f"{name}")
        
    


    def set_map(self,name):
        self._mapRen.setMap(f"{name}")


class SolidObject_Builder(Builder):
    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

        

    def build(self,pos_x,pos_y, sprite_name,height,width):
        self._gameObject = GameObject(pygame.math.Vector2(0,0),self._game_world)
        
        sprite_height=height
        sprite_width=width

        self._gameObject.add_component(SpriteRenderer(sprite_name,sprite_width,sprite_height))
        self._gameObject.add_component(SolidObject(pos_x, pos_y))
        self._gameObject.add_component(Collider())

        
        

      


    def get_gameObject(self) -> GameObject:
        return self._gameObject



class ButtonBuilder(Builder):
    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

        

    def build(self,pos_x,pos_y, buttontype, enum):
        self._gameObject = GameObject(pygame.math.Vector2(0,0),self._game_world)
        
        sprite_height= 64
        sprite_width= 138




        self._gameObject.add_component(SpriteRenderer(buttontype, sprite_width, sprite_height))
        self._gameObject.add_component(MarioButton(pos_x, pos_y, enum))
        self._gameObject.add_component(Collider())



    def get_gameObject(self) -> GameObject:
        return self._gameObject
    



class TextBoxBuilder(Builder):
    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

        

    def build(self,pos_x,pos_y, textType, enum):
        self._gameObject = GameObject(pygame.math.Vector2(0,0),self._game_world)
        
        text_sprite_height= 200
        text_sprite_width= 500




        self._gameObject.add_component(SpriteRenderer(textType, text_sprite_width, text_sprite_height))
        self._gameObject.add_component(TextBox(pos_x, pos_y, enum))
        self._gameObject.add_component(Collider())



    def get_gameObject(self) -> GameObject:
        return self._gameObject
    