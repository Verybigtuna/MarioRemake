from abc import ABC, abstractclassmethod
from GameObject import GameObject
from Components import Animator
from Components import SpriteRenderer
from Player import Player
from Enemy import Enemy
import pygame
import random
from Components import Collider
from Map import Map
from pathlib import Path
import os
class Builder(ABC):

    @abstractclassmethod
    def build(self):
        pass

    def get_gameObject(self) -> GameObject:
        pass


class PlayerBuilder(Builder):

    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(0,0))
        self._gameObject.add_component(SpriteRenderer("player.png"))
        self._gameObject.add_component(Player())
        self._gameObject.add_component(Collider())

        animator = self._gameObject.add_component(Animator())
        animator.add_animation("Idle", "player02.png",
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

    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(0,0))
        sprites = ["enemy_01.png", "enemy_02.png", "enemy_03.png"]
        selected_sprite = random.choice(sprites)
        self._gameObject.add_component(SpriteRenderer(selected_sprite))
        self._gameObject.add_component(Enemy())
        self._gameObject.add_component(Collider())

    def get_gameObject(self) -> GameObject:
        return self._gameObject
    

class MapBuilder(Builder):

    def build(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self._gameObject = GameObject(pygame.math.Vector2(0,0))
        sprite = pygame.image.load("map1.png")
        #HERE = Path(__file__).parent
        #sprite = pygame.image.load(HERE / "assets/map1.png")
        scale = (100, 100)
        sprite = pygame.transform.scale(sprite, scale)
        self._gameObject.add_component(SpriteRenderer(sprite))
        self._gameObject.add_component(Map())
        self._gameObject.add_component(Collider())

    def get_gameObject(self) -> GameObject:
        return self._gameObject