import pygame
from Builder import PlayerBuilder
from Builder import Goomba_EnemyBuilder
from Builder import ButtonBuilder
from Builder import Mushroom_PowerUpBuilder
from Builder import TextBoxBuilder
from GameStates import GameStateManager
from Builder import Door_Builder
from GameStates import GameStates
from Button import ButtonTypes
from Text import TextTypes  
from Builder import MapBuilder
from Builder import Gun_PowerUpBuilder
from Builder import SolidObject_Builder
from Components import MusicPlayer


class GameWorld:

    

    def __init__(self) -> None:
        pygame.init()
        self._stateManager = GameStateManager(self)
        self._mainMenu_Objects = []
        self._lvl1_Objects = []
        self._lvl2_Objects = []
        self._bossLvl_Objects = []
        self._options_Objects = []
        self._win_Objects = []
        self._restart_Objects = []
        self._colliders = []

        self._screen = pygame.display.set_mode((1280,720))
        self._mapbuilder=MapBuilder(self)
        self._mapbuilder.build()
        
        for mapitem in self._mapbuilder.get_gameObject():
            self._lvl1_Objects.append(mapitem)

        builder = PlayerBuilder(self)
        builder.build(self)
        self._lvl1_Objects.append(builder.get_gameObject())
        self._lvl2_Objects.append(builder.get_gameObject())

        builder = Goomba_EnemyBuilder(self)
        builder.build(200, 100)
        self._lvl1_Objects.append(builder.get_gameObject())

        builder.build(600, 560)
        self._lvl1_Objects.append(builder.get_gameObject())

        builder.build(600,200)
        self._lvl1_Objects.append(builder.get_gameObject())


        builder = Mushroom_PowerUpBuilder(self)
        builder.build()
        self._lvl1_Objects.append(builder.get_gameObject())

        builder=Gun_PowerUpBuilder(self)
        builder.build(pygame.math.Vector2(300,560))
        self._lvl1_Objects.append(builder.get_gameObject())

        self.music_player = MusicPlayer("mariotrap.mp3")
        self.music_player.play_music()
        self.music_player.set_volume(0.03)

        builder = ButtonBuilder(self)
        builder.build(480, 500, "button_start.png", ButtonTypes.START)
        self._mainMenu_Objects.append(builder.get_gameObject())


        builder.build(620, 500, "button_quit.png", ButtonTypes.QUIT)
        self._mainMenu_Objects.append(builder.get_gameObject())

        builder.build(550, 600, "button_options.png", ButtonTypes.OPTIONS)
        self._mainMenu_Objects.append(builder.get_gameObject())

        

        builder.build(550, 600, "button_restart.png", ButtonTypes.RESTART)
        self._restart_Objects.append(builder.get_gameObject())


        builder.build(350, 360, "button_mute_sound.png", ButtonTypes.MUTESOUND)
        self._options_Objects.append(builder.get_gameObject())

        builder.build(850, 360, "button_mute_sound.png", ButtonTypes.UNMUTESOUND)
        self._options_Objects.append(builder.get_gameObject())

        builder.build(550, 660, "button_go_back.png", ButtonTypes.GOBACK)
        self._options_Objects.append(builder.get_gameObject())



        builder = TextBoxBuilder(self)
        builder.build(380, 150, "TitleText.png", TextTypes.WELCOME)
        self._mainMenu_Objects.append(builder.get_gameObject())

        builder.build(380, 150, "you_are_dead.png", TextTypes.YOURDEAD)
        self._restart_Objects.append(builder.get_gameObject())


       


        
        builder = Door_Builder(self)
        builder.build(900, 500, GameStates.LVL2)
        self._lvl1_Objects.append(builder.get_gameObject())

        builder=SolidObject_Builder(self)
        

       # for i in range():
           
        builder.build(300,400,"mario_block.png",50,200)
        self._lvl1_Objects.append(builder.get_gameObject())
        



    


       # GameStateManager.currentState = GameStates.MAINMENU



       
        
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
        if GameStateManager.currentState == GameStates.MAINMENU:
            self._mainMenu_Objects.append(gameobject)

        if GameStateManager.currentState == GameStates.LVL1:
            self._lvl1_Objects.append(gameobject)

        if GameStateManager.currentState == GameStates.LVL2:
            self._lvl2_Objects.append(gameobject)

        if GameStateManager.currentState == GameStates.BOSSLVL:
            self._bossLvl_Objects.append(gameobject)

        if GameStateManager.currentState == GameStates.OPTIONS:
            self._options_Objects.append(gameobject)

        if GameStateManager.currentState == GameStates.WIN:
            self._win_Objects.append(gameobject)

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