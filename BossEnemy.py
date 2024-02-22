from Components import Component
import pygame
from GameObject import GameObject
from Components import Laser
from Components import SpriteRenderer
from Components import Collider
from Components import EnemyLaser
from Components import SoundPlayer

class BossEnemy(Component):
    def __init__(self,pos_x,pos_y)-> None:

        self._pos_x=pos_x
        self._pos_y=pos_y
        
        

    def awake(self, game_world):
        self._time_since_last_shot = 1

        self._shoot_delay = 2
        self._can_shoot=False
        self.gameObject.Tag = "BossProjectile"
        self._game_world = game_world
        sr = self.gameObject.get_component("SpriteRenderer")
        self._animator=self._gameObject.get_component("Animator")


        self._boss_enemyPosition_y = self._gameObject.transform.position.y
        



        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(),sr.sprite_image.get_height())
        self._screen_size = pygame.math.Vector2(game_world._screen.get_width(), game_world._screen.get_height())

        self.gameObject.transform.position =pygame.math.Vector2(self._pos_x,self._pos_y)
        
        self._spawnPosition_x=self._pos_x
        self._spawnPosition_y=self._pos_y
        collider = self._gameObject.get_component("Collider")

        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)      

        self._speed=250

        self._speed_y = 250


 
    def start(self):
        pass
    
    def update(self, delta_time):
        self.simple_move_pattern(delta_time)

        self.shoot()

    

        self._movement = pygame.math.Vector2(0,0)
        self._delta_time=delta_time

        self._time_since_last_shot += delta_time



        bottom_limit = self._screen_size.y
        if self._gameObject.transform.position.y > bottom_limit:
            self._gameObject.destroy()


       
    
    
    def simple_move_pattern(self,delta_time):

       
       
        
        if(self.gameObject.transform.position.x>self._spawnPosition_x+80):
         self._speed=-250
         self._animator.play_animation == "Bowser_left"
         
         
        elif(self.gameObject.transform.position.x<self._spawnPosition_x-80):
            self._speed=250
            self._animator.play_animation == "Bowser_right"


        if(self.gameObject.transform.position.y>self._spawnPosition_y):
         self._speed_y=-250
         self._animator.play_animation == "Bowser_left"
         
         
        elif(self.gameObject.transform.position.y<self._spawnPosition_y-150):
            self._speed_y=250
            self._animator.play_animation == "Bowser_right"

        
            

      
        movement = pygame.math.Vector2(self._speed, self._speed_y)

       


        
        self.gameObject.transform.translate(movement*delta_time)

    def shoot(self):
        if self._time_since_last_shot >= self._shoot_delay:
            projectile = GameObject(pygame.math.Vector2(0,0),self._game_world)
            sr = projectile.add_component(SpriteRenderer("fireball_1.png",110, 90))
            if self._animator._current_animation == "Bowser_right":
                projectile.add_component(EnemyLaser(-200))
            elif self._animator._current_animation == "Bowser_left":
                projectile.add_component(EnemyLaser(-200))

            projectile.add_component(Collider())


        

            projectile_position = pygame.math.Vector2(self._gameObject.transform.position.x+(self._sprite_size.x/2)-sr.sprite_image.get_width()/2 -70
                                                    ,self._gameObject.transform.position.y +35)
        
            projectile.transform.position = projectile_position - self.gameObject.transform.offset

            self._game_world.instantiate(projectile)
            

            self._time_since_last_shot = 0


    def on_collision_enter(self,other):
      pass

    def on_collision_exit(self,other):
      pass

    