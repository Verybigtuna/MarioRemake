from abc import ABC, abstractclassmethod
from GameObject import GameObject
from Components import Animator
from Components import SpriteRenderer
from Player import Player
from Enemy import Enemy
from Goomba_Enemy import Goomba_Enemy
import pygame
import random
from Components import Collider
from Door import Lvl_Door



class Builder(ABC):

    @abstractclassmethod
    def build(self,game_world):
        pass

    def get_gameObject(self) -> GameObject:
        pass


class PlayerBuilder(Builder):

    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(0,0),self._game_world)
        #Make sure to add 

        sprite_height=70
        sprite_width=70


        self._gameObject.add_component(SpriteRenderer("player.png",sprite_width,sprite_height))
        self._gameObject.add_component(Player())
        self._gameObject.add_component(Collider())

        animator = self._gameObject.add_component(Animator())
        animator.add_animation("Idle",sprite_height,sprite_width, "player02.png",
                               "player03.png",
                               "player04.png",
                               "player05.png",
                               "player06.png",
                               "player07.png",
                               "player08.png",
                               "player07.png",
                               "player06.png",
                               "player05.png",
                               "player04.png",
                               "player03.png")
        
        

        animator.play_animation("Idle")

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


class Door_Builder(Builder):
    
    def __init__(self,game_world) -> None:

        super().__init__()

        self._game_world=game_world

        

    def build(self,pos_x,pos_y, enum):
        self._gameObject = GameObject(pygame.math.Vector2(0,0),self._game_world)
        
        sprite_height=50
        sprite_width=50

        self._gameObject.add_component(SpriteRenderer("shield.png",sprite_width,sprite_height))
        self._gameObject.add_component(Lvl_Door(pos_x, pos_y, enum))
        self._gameObject.add_component(Collider())

        
        

      


    def get_gameObject(self) -> GameObject:
        return self._gameObject