import pygame
from Components  import Component
from GameStates import GameStateManager
from GameStates import GameStates
from enum import Enum
from Score import GameScore
from Components import MusicPlayer




class ButtonTypes(Enum):
    START = 1
    OPTIONS = 2
    QUIT = 3
    RESTART = 4
    MUTESOUND = 5
    WIN = 6
    GOBACK = 7
    UNMUTESOUND = 8


class MarioButton(Component):

    down = True
    


    def __init__(self,pos_x,pos_y, buttonType) -> None:
        self._pos_x=pos_x
        self._pos_y=pos_y
        self._buttonType = buttonType
        self._clicked = False
        self.music_player = MusicPlayer


    

    def awake(self, game_world):
        

        self.gameObject.Tag = "button"

        self._gameWorld = game_world

        
        self._screen_size = pygame.math.Vector2(game_world._screen.get_width(), game_world._screen.get_height())

        self.gameObject.transform.position =pygame.math.Vector2(self._pos_x,self._pos_y)
        
        self._spawnPosition_x=self._pos_x
        self._rect = self.gameObject.get_component("SpriteRenderer").sprite.rect
        collider = self._gameObject.get_component("Collider")


        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)



    def start(self):
        pass

    def update(self, delta_time):
        
    
        pos = pygame.mouse.get_pos()
       
        # print("bruh")
        if self._rect.collidepoint(pos):
            self.On_Button_Click()
               
             
        return super().update(delta_time)

   

    def On_Button_Click(self):
        if pygame.mouse.get_pressed()[0] == 1 and self._clicked == False:
            if self._buttonType == ButtonTypes.START:
                self._clicked = True
                GameStateManager.currentState = GameStates.LVL1

            if self._buttonType == ButtonTypes.QUIT:
                self._clicked = True
                pygame.quit()

            if self._buttonType == ButtonTypes.OPTIONS:
                self._clicked = True
                GameStateManager.currentState = GameStates.OPTIONS


            if self._buttonType == ButtonTypes.MUTESOUND:

                self.music_player = MusicPlayer("mariotrap.mp3")
                self.music_player.play_music()

                self._clicked = True
                
                self.music_player.set_volume(0.0)

                

            if self._buttonType == ButtonTypes.UNMUTESOUND:
                
                self._clicked = True
                

                self.music_player = MusicPlayer("mariotrap.mp3")

                self.music_player.play_music()

                self.music_player.set_volume(0.10)

                pass

            if self._buttonType == ButtonTypes.RESTART:
                self._clicked = True
                self._gameWorld._stateManager.init2()
                self._gameWorld._stateManager.awake(self._gameWorld)
                self._gameWorld._stateManager.start()

                GameStateManager.currentState = GameStates.MAINMENU

                GameScore.score = 0
                

            if self._buttonType == ButtonTypes.GOBACK:
                self._clicked = True
                GameStateManager.currentState = GameStates.MAINMENU
                
        if pygame.mouse.get_pressed()[0] == 0:
            self._clicked = False


    
    def on_collision_enter(self, other):
      pass

    def on_collision_exit(self,other):
      pass


    def on_collision_enter_top(self, other):
        pass


    def on_collision_exit_top(self,other):
     pass
        
