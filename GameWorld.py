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
from LvLMaker import LevelMaker
from Components import MusicPlayer
from Builder import Shooter_EnemyBuilder
from Score import GameScore

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
        

        self.music_player = MusicPlayer("mariotrap.mp3")
        self.music_player.play_music()
        self.music_player.set_volume(0.03)
        

        self.WHITE = (255, 255, 255) 

        self.font = pygame.font.SysFont(None, 36)

        builder = ButtonBuilder(self)
        builder.build(480, 500, "button_start.png", ButtonTypes.START)
        self._mainMenu_Objects.append(builder.get_gameObject())


        builder.build(620, 500, "button_quit.png", ButtonTypes.QUIT)
        self._mainMenu_Objects.append(builder.get_gameObject())

        builder.build(550, 600, "button_options.png", ButtonTypes.OPTIONS)
        self._mainMenu_Objects.append(builder.get_gameObject())

        

        builder.build(550, 400, "button_restart.png", ButtonTypes.RESTART)
        self._restart_Objects.append(builder.get_gameObject())


        builder.build(350, 360, "button_mute_sound.png", ButtonTypes.MUTESOUND)
        self._options_Objects.append(builder.get_gameObject())

        builder.build(850, 360, "button_mute_sound.png", ButtonTypes.UNMUTESOUND)
        self._options_Objects.append(builder.get_gameObject())

        builder.build(550, 660, "button_go_back.png", ButtonTypes.GOBACK)
        self._options_Objects.append(builder.get_gameObject())

        builder.build(550, 560, "button_go_back.png", ButtonTypes.GOBACK)
        self._win_Objects.append(builder.get_gameObject())



        builder = TextBoxBuilder(self)
        builder.build(380, 150, "TitleText.png", TextTypes.WELCOME)
        self._mainMenu_Objects.append(builder.get_gameObject())

        builder.build(380, 150, "you_are_dead.png", TextTypes.YOURDEAD)
        self._restart_Objects.append(builder.get_gameObject())

        builder.build(380, 150, "you_win.png", TextTypes.YOUWIN)
        self._win_Objects.append(builder.get_gameObject())
#turtorial
        


#turtorial
        
        
        

        levelOne = LevelMaker(self)
        levelOne.Level_One_map()

        levelTwo = LevelMaker(self)
        levelTwo.Level_Two_map()

        levelTwo = LevelMaker(self)
        levelTwo.Level_Boss_map()



       # GameStateManager.currentState = GameStates.MAINMENU



       
        
        self._running = True
        self._clock = pygame.time.Clock()

    @property
    def screen(self):
        return self._screen

    @property
    def colliders(self):
        return self._colliders
    
    def display_score(self, score):
       score_text = self.font.render("Score: " + str(score), True, self.WHITE)
       score_rect = score_text.get_rect()
       score_rect.topright = (self._screen.get_width() - 10, 10)  # Adjust the position as needed
       self._screen.blit(score_text, score_rect)

    def display_final_score(self, score):
       score_text = self.font.render("Final Score: " + str(score), True, self.WHITE)
       score_rect = score_text.get_rect()
       score_rect.topright = (self._screen.get_width() - 580, 360)  # Adjust the position as needed
       self._screen.blit(score_text, score_rect)



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
            
            

            if GameStateManager.currentState == GameStates.RESTART or GameStateManager.currentState == GameStates.WIN:
                self.display_final_score(GameScore.score)
            else:
                self.display_score(GameScore.score)

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