import pygame
from GameObject import GameObject
from Components import SpriteRenderer
from Components import Animator
from Player import Player
from Builder import PlayerBuilder
from Builder import EnemyBuilder
from Builder import MapBuilder
class GameWorld:

    def __init__(self) -> None:
        pygame.init()
        self._gameObjects = []
        self._colliders = []

        self._screen = pygame.display.set_mode((1280,720))

        builder = PlayerBuilder()
        builder.build()
        self._gameObjects.append(builder.get_gameObject())
        
        builder = EnemyBuilder()
        builder.build()
        self._gameObjects.append(builder.get_gameObject())

        builder = MapBuilder()
        builder.build()
        self._gameObjects.append(builder.get_gameObject())


        self._running = True
        self._clock = pygame.time.Clock()

    @property
    def screen(self):
        return self._screen

    @property
    def colliders(self):
        return self._colliders

    def instantiate(self, gameobject):
        gameobject.awake(self)
        gameobject.start()
        self._gameObjects.append(gameobject)

    def awake(self):
        for gameObject in self._gameObjects[:]:
            gameObject.awake(self)


    def start(self):
        for gameObject in self._gameObjects[:]:
            gameObject.start()

    def update(self):


        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self._screen.fill("cornflowerblue")

            delta_time = self._clock.tick(60) / 1000.0

            #Draw game here
            for gameObject in self._gameObjects[:]:
                gameObject.update(delta_time)

            for i, collider1 in enumerate(self._colliders):
                for j in range(i+1, len(self._colliders)):
                    collider2 = self._colliders[j]
                    collider1.collision_check(collider2)

            self._gameObjects = [obj for obj in self._gameObjects if not obj.is_destroyed]

            pygame.display.flip()
            print(self._clock.get_fps())

        pygame.quit()


gw = GameWorld()
gw.awake()
gw.start()
gw.update()