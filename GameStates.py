from enum import Enum
from Camera import Camera



class GameStates(Enum):
    MAINMENU = 1
    OPTIONS = 2
    LVL1 = 3
    LVL2 = 4
    BOSSLVL = 5
    WIN = 6
    RESTART = 7



class GameStateManager():

    

    currentState = GameStates.MAINMENU
   


    def __init__(self, gameWorld):
        
        self._gameWorld = gameWorld

        self._empty_colliders=True
  
   
    def awake(self, gameWorld):

        


        #  if GameStateManager.currentState == GameStates.MAINMENU: # _gameObjects skal udskiftes senere til De lister af gameobjects der er MAINMENU
            for game_object in self._gameWorld._mainMenu_Objects[:]:
                    game_object.awake(gameWorld)

        #  elif GameStateManager.currentState == GameStates.LVL1:
            for game_object in self._gameWorld._lvl1_Objects[:]: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL1 state
                game_object.awake(gameWorld)

        #  elif GameStateManager.currentState == GameStates.LVL2: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL2 state
                for game_object in self._gameWorld._lvl2_Objects[:]:
                    game_object.awake(gameWorld)
            
        #  elif GameStateManager.currentState == GameStates.BOSSLVL: # _gameObjects skal udskiftes senere til De lister af gameobjects der er BOSSLVL state
                for game_object in self._gameWorld._bossLvl_Objects[:]:
                    game_object.awake(gameWorld)

        #  elif GameStateManager.currentState == GameStates.OPTIONS: # _gameObjects skal udskiftes senere til De lister af gameobjects der er OPTIONS state
                for game_object in self._gameWorld._options_Objects[:]:
                    game_object.awake(gameWorld)

        #  elif GameStateManager.currentState == GameStates.WIN: # _gameObjects skal udskiftes senere til De lister af gameobjects der er WIN state
                for game_object in self._gameWorld._win_Objects[:]:
                    game_object.awake(gameWorld)

                for game_object in self._gameWorld._restart_Objects[:]:
                    game_object.awake(gameWorld)




    def start(self):

       


        # if GameStateManager.currentState == GameStates.MAINMENU: # _gameObjects skal udskiftes senere til De lister af gameobjects der er MAINMENU
            for game_object in self._gameWorld._mainMenu_Objects[:]:
                 game_object.start()

        # elif GameStateManager.currentState == GameStates.LVL1:
            for game_object in self._gameWorld._lvl1_Objects[:]: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL1 state
                 game_object.start()

        # elif GameStateManager.currentState == GameStates.LVL2: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL2 state
            for game_object in self._gameWorld._lvl2_Objects[:]:
                game_object.start()
            
        # elif GameStateManager.currentState == GameStates.BOSSLVL: # _gameObjects skal udskiftes senere til De lister af gameobjects der er BOSSLVL state
            for game_object in self._gameWorld._bossLvl_Objects[:]:
                game_object.start()

        # elif GameStateManager.currentState == GameStates.OPTIONS: # _gameObjects skal udskiftes senere til De lister af gameobjects der er OPTIONS state
            for game_object in self._gameWorld._options_Objects[:]:
                game_object.start()

        # elif GameStateManager.currentState == GameStates.WIN: # _gameObjects skal udskiftes senere til De lister af gameobjects der er WIN state
            for game_object in self._gameWorld._win_Objects[:]:
                game_object.start()

            for game_object in self._gameWorld._restart_Objects[:]:
                game_object.start()
    

    





    def update(self, delta_time):

        delta_time = self._gameWorld._clock.tick(60) / 1000.0

        


        if GameStateManager.currentState == GameStates.MAINMENU: # _gameObjects skal udskiftes senere til De lister af gameobjects der er MAINMENU
            for gameObject in self._gameWorld._mainMenu_Objects[:]:

                
                gameObject.update(delta_time)
                  
                  


            self._gameWorld._mainMenu_Objects = [obj for obj in self._gameWorld._mainMenu_Objects if not obj.is_destroyed]

            
            self._gameWorld._colliders = []
            for obj in self._gameWorld._mainMenu_Objects:
                collider = obj.get_component("Collider")
                if not obj.is_destroyed and collider != None:
                    self._gameWorld._colliders.append(collider)


        elif GameStateManager.currentState == GameStates.LVL1:
            for gameObject in self._gameWorld._lvl1_Objects[:]:

                if(gameObject.follows_camera==False):
                 
                    gameObject.transform.offset+=Camera.camera_offset

                    gameObject.update(delta_time)
                else:
                    gameObject.update(delta_time)
            
            
            self._gameWorld._lvl1_Objects = [obj for obj in self._gameWorld._lvl1_Objects if not obj.is_destroyed]

            if self._empty_colliders==True:
             self._gameWorld._colliders = []
             self._empty_colliders=False
            
             for obj in self._gameWorld._lvl1_Objects:
                collider = obj.get_component("Collider")
                if not obj.is_destroyed and collider != None:
                    self._gameWorld._colliders.append(collider)
            
            self._gameWorld._colliders=[obj for obj in self._gameWorld._colliders if not obj.gameObject.is_destroyed]


        elif GameStateManager.currentState == GameStates.LVL2: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL2 state
            self._gameWorld._screen.fill("darkgrey")
            for gameObject in self._gameWorld._lvl2_Objects[:]:

                if(gameObject.follows_camera==False):
                 
                    gameObject.transform.offset+=Camera.camera_offset

                    gameObject.update(delta_time)
                else:
                    gameObject.update(delta_time)
            

            self._gameWorld._lvl2_Objects = [obj for obj in self._gameWorld._lvl2_Objects if not obj.is_destroyed]

            self._gameWorld._colliders = []
            for obj in self._gameWorld._lvl2_Objects:
                collider = obj.get_component("Collider")
                if not obj.is_destroyed and collider != None:
                    self._gameWorld._colliders.append(collider)
            

        elif GameStateManager.currentState == GameStates.BOSSLVL: # _gameObjects skal udskiftes senere til De lister af gameobjects der er BOSSLVL state
            self._gameWorld._screen.fill("black")
            for gameObject in self._gameWorld._bossLvl_Objects[:]:
            
                if(gameObject.follows_camera==False):
                 
                    gameObject.transform.offset+=Camera.camera_offset

                    gameObject.update(delta_time)
                else:
                    gameObject.update(delta_time)
            

            self._gameWorld._bossLvl_Objects = [obj for obj in self._gameWorld._bossLvl_Objects if not obj.is_destroyed]

            self._gameWorld._colliders = []
            for obj in self._gameWorld._bossLvl_Objects:
                collider = obj.get_component("Collider")
                if not obj.is_destroyed and collider != None:
                    self._gameWorld._colliders.append(collider)


        elif GameStateManager.currentState == GameStates.OPTIONS: # _gameObjects skal udskiftes senere til De lister af gameobjects der er OPTIONS state
            self._gameWorld._screen.fill("brown")
            for gameObject in self._gameWorld._options_Objects[:]:

                
                gameObject.update(delta_time)
            

            self._gameWorld._options_Objects = [obj for obj in self._gameWorld._options_Objects if not obj.is_destroyed]

            self._gameWorld._colliders = []
            for obj in self._gameWorld._options_Objects:
                collider = obj.get_component("Collider")
                if not obj.is_destroyed and collider != None:
                    self._gameWorld._colliders.append(collider)


        elif GameStateManager.currentState == GameStates.WIN: # _gameObjects skal udskiftes senere til De lister af gameobjects der er WIN state


            
            for gameObject in self._gameWorld._win_Objects[:]:

                
                gameObject.update(delta_time)
            

            self._gameWorld._win_Objects = [obj for obj in self._gameWorld._win_Objects if not obj.is_destroyed]
            
            self._gameWorld._colliders = []
            for obj in self._gameWorld._win_Objects:
                collider = obj.get_component("Collider")
                if not obj.is_destroyed and collider != None:
                    self._gameWorld._colliders.append(collider)

        
        if GameStateManager.currentState == GameStates.RESTART: # _gameObjects skal udskiftes senere til De lister af gameobjects der er MAINMENU
            self._gameWorld._screen.fill("darkred")
            for gameObject in self._gameWorld._restart_Objects[:]:

                gameObject.update(delta_time)
                  
                  


            self._gameWorld._restart_Objects = [obj for obj in self._gameWorld._restart_Objects if not obj.is_destroyed]


            self._gameWorld._colliders = []
            for obj in self._gameWorld._restart_Objects:
                collider = obj.get_component("Collider")
                if not obj.is_destroyed and collider != None:
                    self._gameWorld._colliders.append(collider)



    def LoadContent():
        pass


    
    def init2(self):
        from Button import ButtonTypes
        from Text import TextTypes  
        from Builder import MapBuilder
        from Builder import Gun_PowerUpBuilder
        from Builder import SolidObject_Builder
        from LvLMaker import LevelMaker
        from Components import MusicPlayer

        from Builder import ButtonBuilder

        from Builder import TextBoxBuilder



        self._gameWorld._mainMenu_Objects = []
        self._gameWorld._lvl1_Objects = []
        self._gameWorld._lvl2_Objects = []
        self._gameWorld._bossLvl_Objects = []
        self._gameWorld._options_Objects = []
        self._gameWorld._win_Objects = []
        self._gameWorld._restart_Objects = []
        self._gameWorld._colliders = []

        builder = ButtonBuilder(self._gameWorld)
        builder.build(480, 500, "button_start.png", ButtonTypes.START)
        self._gameWorld._mainMenu_Objects.append(builder.get_gameObject())


        builder.build(620, 500, "button_quit.png", ButtonTypes.QUIT)
        self._gameWorld._mainMenu_Objects.append(builder.get_gameObject())

        builder.build(550, 600, "button_options.png", ButtonTypes.OPTIONS)
        self._gameWorld._mainMenu_Objects.append(builder.get_gameObject())

        

        builder.build(550, 400, "button_restart.png", ButtonTypes.RESTART)
        self._gameWorld._restart_Objects.append(builder.get_gameObject())


        builder.build(550, 360, "button_mute_sound.png", ButtonTypes.MUTESOUND)
        self._gameWorld._options_Objects.append(builder.get_gameObject())

        builder.build(550, 560, "button_go_back.png", ButtonTypes.GOBACK)
        self._gameWorld._options_Objects.append(builder.get_gameObject())

        builder.build(550, 560, "button_go_back.png", ButtonTypes.GOBACK)
        self._gameWorld._win_Objects.append(builder.get_gameObject())


        builder = TextBoxBuilder(self._gameWorld)
        builder.build(380, 150, "TitleText.png", TextTypes.WELCOME)
        self._gameWorld._mainMenu_Objects.append(builder.get_gameObject())

        builder.build(380, 150, "you_are_dead.png", TextTypes.YOURDEAD)
        self._gameWorld._restart_Objects.append(builder.get_gameObject())

        builder.build(380, 150, "you_win.png", TextTypes.YOUWIN)
        self._gameWorld._win_Objects.append(builder.get_gameObject())

        

        levelOne = LevelMaker(self._gameWorld)
        levelOne.Level_One_map()

        levelTwo = LevelMaker(self._gameWorld)
        levelTwo.Level_Two_map()

        levelTwo = LevelMaker(self._gameWorld)
        levelTwo.Level_Boss_map()


    
        # GameStateManager.currentState = GameStates.MAINMENU
        self.music_player = MusicPlayer("mariotrap.mp3")  # Replace with your music file path
        #self.music_player.play_music()


       

       
        





    

    