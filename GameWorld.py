import pygame
from Builder import PlayerBuilder
from Builder import Goomba_EnemyBuilder
from GameStates import GameStateManager

class GameWorld:

    

    def __init__(self) -> None:
        pygame.init()
        self._stateManager = GameStateManager(self)
        self._gameObjects = []
        self._mainMenu_Objects = []
        self._lvl1_Objects = []
        self._lvl2_Objects = []
        self._bossLvl_Objects = []
        self._options_Objects = []
        self._win_Objects = []
        self._colliders = []
        self._key_is_pressed = False

        builder = PlayerBuilder(self)
        builder.build()
        self._lvl1_Objects.append(builder.get_gameObject())
        self._lvl2_Objects.append(builder.get_gameObject())

        builder = Goomba_EnemyBuilder(self)
        builder.build(200, 400)
        self._lvl1_Objects.append(builder.get_gameObject())

        builder.build(500, 600)
        self._lvl1_Objects.append(builder.get_gameObject())

        
       # GameStateManager.currentState = GameStates.MAINMENU

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
        self._stateManager.awake(self)

        # for gameObject in self._gameObjects[:]:
        #     gameObject.awake(self)


    def start(self):
        self._stateManager.start()

        # for gameObject in self._gameObjects[:]:
        #     gameObject.start()

    def update(self):

    
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self._screen.fill("cornflowerblue")

            

            delta_time = self._clock.tick(60) / 1000.0

            #Draw game here
            

            self._stateManager.update(delta_time)
            


            # for gameObject in self._gameObjects[:]:

            #     if(gameObject.follows_camera==False):
                 
            #      gameObject.transform.offset+=Camera.camera_offset

                 

            #      gameObject.update(delta_time)
            #     else:
                  

                  
            #       gameObject.update(delta_time)
                  
                  
         

            for i, collider1 in enumerate(self._colliders):
                for j in range(i+1, len(self._colliders)):
                    collider2 = self._colliders[j]
                    collider1.collision_check(collider2)

            #self._gameObjects = [obj for obj in self._gameObjects if not obj.is_destroyed]
            
            #self._colliders=[obj for obj in self._colliders if not obj.gameObject.is_destroyed]
           
            # if GameStateManager.currentState == GameStates.LVL1:
            #     self._colliders = []
            #     for obj in self._lvl1_Objects:
            #         if not obj.is_destroyed:
            #             self._colliders.append(obj.get_component("Collider"))
          

            pygame.display.flip()
            self._clock.tick(60)

        pygame.quit()


gw = GameWorld()
gw.awake()
gw.start()
gw.update()