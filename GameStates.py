from enum import Enum
from GameWorld import GameWorld
from Camera import Camera


class GameStates(Enum):
    MAINMENU = 1
    OPTIONS = 2
    LVL1 = 3
    LVL2 = 4
    BOSSLVL = 5
    WIN = 6


class GameStateManager():

    

    currentState = GameStates.MAINMENU


    def __init__(self, gameWorld):
        type(self).currentState = GameStates.LVL1
        self._gameWorld = gameWorld

    def awake(self, gameWorld):

        


         if GameStateManager.currentState == GameStates.MAINMENU: # _gameObjects skal udskiftes senere til De lister af gameobjects der er MAINMENU
            for game_object in self._gameWorld._gameObjects[:]:
                    game_object.awake(gameWorld)

         elif GameStateManager.currentState == GameStates.LVL1:
            for game_object in self._gameWorld._gameObjects[:]: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL1 state
                game_object.awake(gameWorld)

         elif GameStateManager.currentState == GameStates.LVL2: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL2 state
                for game_object in self._gameWorld._gameObjects[:]:
                    game_object.awake(gameWorld)
            
         elif GameStateManager.currentState == GameStates.BOSSLVL: # _gameObjects skal udskiftes senere til De lister af gameobjects der er BOSSLVL state
                for game_object in self._gameWorld._gameObjects[:]:
                    game_object.awake(gameWorld)

         elif GameStateManager.currentState == GameStates.OPTIONS: # _gameObjects skal udskiftes senere til De lister af gameobjects der er OPTIONS state
                for game_object in self._gameWorld._gameObjects[:]:
                    game_object.awake(gameWorld)

         elif GameStateManager.currentState == GameStates.WIN: # _gameObjects skal udskiftes senere til De lister af gameobjects der er WIN state
                for game_object in self._gameWorld._gameObjects[:]:
                    game_object.awake(gameWorld)




    def start(self):

       


        if GameStateManager.currentState == GameStates.MAINMENU: # _gameObjects skal udskiftes senere til De lister af gameobjects der er MAINMENU
            for game_object in self._gameWorld._gameObjects[:]:
                 game_object.start()

        elif GameStateManager.currentState == GameStates.LVL1:
            for game_object in self._gameWorld._gameObjects[:]: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL1 state
                 game_object.start()

        elif GameStateManager.currentState == GameStates.LVL2: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL2 state
            for game_object in self._gameWorld._gameObjects[:]:
                game_object.start()
            
        elif GameStateManager.currentState == GameStates.BOSSLVL: # _gameObjects skal udskiftes senere til De lister af gameobjects der er BOSSLVL state
            for game_object in self._gameWorld._gameObjects[:]:
                game_object.start()

        elif GameStateManager.currentState == GameStates.OPTIONS: # _gameObjects skal udskiftes senere til De lister af gameobjects der er OPTIONS state
            for game_object in self._gameWorld._gameObjects[:]:
                game_object.start()

        elif GameStateManager.currentState == GameStates.WIN: # _gameObjects skal udskiftes senere til De lister af gameobjects der er WIN state
            for game_object in self._gameWorld._gameObjects[:]:
                game_object.start()
    

    





    def update(self, delta_time):

        delta_time = self._gameWorld._clock.tick(60) / 1000.0


        if GameStateManager.currentState == GameStates.MAINMENU: # _gameObjects skal udskiftes senere til De lister af gameobjects der er MAINMENU
            for gameObject in self._gameWorld._mainMenu_Objects[:]:

                if(gameObject.follows_camera==False):
                 
                    gameObject.transform.offset+=Camera.camera_offset

                    gameObject.update(delta_time)
                else:
                    gameObject.update(delta_time)
                  
                  


            self._gameWorld._mainMenu_Objects = [obj for obj in self._gameWorld._mainMenu_Objects if not obj.is_destroyed]


            self._gameWorld._colliders = []
            for obj in self._gameWorld._mainMenu_Objects:
                if not obj.is_destroyed:
                    self._gameWorld._colliders.append(obj.get_component("Collider"))


        elif GameStateManager.currentState == GameStates.LVL1:
            for gameObject in self._gameWorld._lvl1_Objects[:]:

                if(gameObject.follows_camera==False):
                 
                    gameObject.transform.offset+=Camera.camera_offset

                    gameObject.update(delta_time)
                else:
                    gameObject.update(delta_time)
            
            
            self._gameWorld._lvl1_Objects = [obj for obj in self._gameWorld._lvl1_Objects if not obj.is_destroyed]

            
            self._gameWorld._colliders = []
            for obj in self._gameWorld._lvl1_Objects:
                if not obj.is_destroyed:
                    self._gameWorld._colliders.append(obj.get_component("Collider"))


        elif GameStateManager.currentState == GameStates.LVL2: # _gameObjects skal udskiftes senere til De lister af gameobjects der er LVL2 state
            for gameObject in self._gameWorld._lvl2_Objects[:]:

                if(gameObject.follows_camera==False):
                 
                    gameObject.transform.offset+=Camera.camera_offset

                    gameObject.update(delta_time)
                else:
                    gameObject.update(delta_time)
            

            self._gameWorld._lvl2_Objects = [obj for obj in self._gameWorld._lvl2_Objects if not obj.is_destroyed]

            self._gameWorld._colliders = []
            for obj in self._gameWorld._lvl2_Objects:
                if not obj.is_destroyed:
                    self._gameWorld._colliders.append(obj.get_component("Collider"))
            

        elif GameStateManager.currentState == GameStates.BOSSLVL: # _gameObjects skal udskiftes senere til De lister af gameobjects der er BOSSLVL state
            for gameObject in self._gameWorld._bossLvl_Objects[:]:

                if(gameObject.follows_camera==False):
                 
                    gameObject.transform.offset+=Camera.camera_offset

                    gameObject.update(delta_time)
                else:
                    gameObject.update(delta_time)
            

            self._gameWorld._bossLvl_Objects = [obj for obj in self._gameWorld._bossLvl_Objects if not obj.is_destroyed]

            self._gameWorld._colliders = []
            for obj in self._gameWorld._bossLvl_Objects:
                if not obj.is_destroyed:
                    self._gameWorld._colliders.append(obj.get_component("Collider"))


        elif GameStateManager.currentState == GameStates.OPTIONS: # _gameObjects skal udskiftes senere til De lister af gameobjects der er OPTIONS state
            for gameObject in self._gameWorld._options_Objects[:]:

                if(gameObject.follows_camera==False):
                 
                    gameObject.transform.offset+=Camera.camera_offset

                    gameObject.update(delta_time)
                else:
                    gameObject.update(delta_time)
            

            self._gameWorld._options_Objects = [obj for obj in self._gameWorld._options_Objects if not obj.is_destroyed]

            self._gameWorld._colliders = []
            for obj in self._gameWorld._options_Objects:
                if not obj.is_destroyed:
                    self._gameWorld._colliders.append(obj.get_component("Collider"))


        elif GameStateManager.currentState == GameStates.WIN: # _gameObjects skal udskiftes senere til De lister af gameobjects der er WIN state
            for gameObject in self._gameWorld._win_Objects[:]:

                if(gameObject.follows_camera==False):
                 
                    gameObject.transform.offset+=Camera.camera_offset

                    gameObject.update(delta_time)
                else:
                    gameObject.update(delta_time)
            

            self._gameWorld._win_Objects = [obj for obj in self._gameWorld._win_Objects if not obj.is_destroyed]
            
            self._gameWorld._colliders = []
            for obj in self._gameWorld._win_Objects:
                if not obj.is_destroyed:
                    self._gameWorld._colliders.append(obj.get_component("Collider"))



    def LoadContent():
        pass

       
        





    

    