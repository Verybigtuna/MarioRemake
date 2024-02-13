import pygame
from GameObject import GameObject
from Components import SpriteRenderer
from Components import Animator
from Player import Player
from Builder import PlayerBuilder
from Builder import Goomba_EnemyBuilder
from Camera import Camera
class GameWorld:

    

    def __init__(self) -> None:
        pygame.init()
        self._gameObjects = []
        self._colliders = []
        self._key_is_pressed = False

        builder = PlayerBuilder(self)
        builder.build()
        self._gameObjects.append(builder.get_gameObject())
        
        builder = Goomba_EnemyBuilder(self)
        builder.build(200, 400)
        self._gameObjects.append(builder.get_gameObject())

        builder.build(500, 600)
        self._gameObjects.append(builder.get_gameObject())

        


        self._screen = pygame.display.set_mode((1280,720))
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
            key_state = pygame.key.get_pressed()
            


            for gameObject in self._gameObjects[:]:

                if(gameObject.follows_camera==False):
                 
                 gameObject.transform.offset+=Camera.camera_offset

                 

                 gameObject.update(delta_time)
                else:
                  

                  
                  gameObject.update(delta_time)
                  
                  
         

            for i, collider1 in enumerate(self._colliders):
                for j in range(i+1, len(self._colliders)):
                    collider2 = self._colliders[j]
                    collider1.collision_check(collider2)

            self._gameObjects = [obj for obj in self._gameObjects if not obj.is_destroyed]
            
            self._colliders=[obj for obj in self._colliders if not obj.gameObject.is_destroyed]
           
                 
          

            pygame.display.flip()
            self._clock.tick(60)

        pygame.quit()


gw = GameWorld()
gw.awake()
gw.start()
gw.update()