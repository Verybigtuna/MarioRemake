from Components import Component
import pygame
from GameObject import GameObject
from Components import Laser
from Components import SpriteRenderer
from Components import Collider
from Camera import Camera
from GameStates import GameStateManager
from GameStates import GameStates
from Components import SoundPlayer

import time
class Player(Component):

    def __init__(self,game_world) -> None:
        self._game_world = game_world

    
        
    
    def awake(self, game_world):
        self._time_since_last_shot = 1
        self._shoot_delay = 1
        self._can_shoot=False
        
        self._is_jumping = False
        self._is_falling = True
        self._can_jump = False
        self._start_jump_position = 0
        
        self.gameObject.follows_camera=True
        self.gameObject.Tag = "Player"



        sr = self._gameObject.get_component("SpriteRenderer")
        
        self._animator=self._gameObject.get_component("Animator")

        self._movement = pygame.math.Vector2(0,0)

        self._right_blocked=False
        self._left_blocked=False
        self._up_blocked=False
        self._down_blocked=False


     
     
      



        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(), game_world.screen.get_height())
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(),sr.sprite_image.get_height())
        self._gameObject.transform.position.x = 50
        self._gameObject.transform.position.y = (self._screen_size.y) - (self._sprite_size.y)
        
        collider = self._gameObject.get_component("Collider")
        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)
        collider.subscribe("collision_enter_top",self.on_collision_enter_top)
        collider.subscribe("pixel_collision_enter",self.on_pixel_collision_enter)
        collider.subscribe("pixel_collision_exit",self.on_pixel_collision_exit)
        collider.subscribe("collision_enter_powerUp",self.on_collision_enter_powerUp)
        
        collider.subscribe("collision_enter_gun_powerup",self.on_collision_enter_gun_powerup)

        collider.subscribe("collision_enter_solid_object",self.on_collision_enter_solid_object)
        collider.subscribe("collision_exit_solid_object",self.on_collision_exit_solid_object)


    @property
    def can_jump(self):
        return self._can_jump
    @can_jump.setter
    def can_jump(self, value):
        self._can_jump = value
    @property
    def is_jumping(self):
        return self._is_jumping
    @is_jumping.setter
    def is_jumping(self, value):
        self._is_jumping = value
    @property
    def is_falling(self):
        return self._is_falling
    @is_falling.setter
    def is_falling(self, value):
        self._is_falling = value

    def start(self):
        pass

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        speed = 1000
        self._movement = pygame.math.Vector2(0,0)
        Camera.camera_offset=pygame.math.Vector2(0,0)

        self._delta_time=delta_time

        self._time_since_last_shot += delta_time
        self._gravity = 1700
        
        jump_height = 300
        
        player_position_y = self._gameObject.transform.position.y

        bottom_limit = self._screen_size.y-100 -self._sprite_size.y
      

        if keys[pygame.K_a] and not self._left_blocked:
            self._movement.x -= speed
            self._animator.play_animation(f"{self._animator._currentstate}left")
          
           

        if keys[pygame.K_d] and not self._right_blocked:
            self._movement.x += speed
            self._animator.play_animation(f"{self._animator._currentstate}right")
           
           

        if keys[pygame.K_SPACE] and self.can_jump is True:
            self.is_falling = False
            self.can_jump = False
            self.is_jumping = True
            self._start_jump_position = player_position_y
            self._down_blocked=False

        if keys[pygame.K_f] and self._can_shoot==True:
            self.shoot()
            

        #Gravity
        if self.is_falling and self._down_blocked==False:
            self._movement.y += self._gravity

        #Jumping
        if self.is_jumping:
            self._movement.y -= self._gravity
            if player_position_y < (self._start_jump_position - jump_height) or self._up_blocked==True:
                self.is_jumping = False
                self.is_falling = True
               

        self._gameObject.transform.translate(self._movement*delta_time)
        self.gameObject.transform.offset+=self._movement*delta_time


        



        Camera.camera_offset+=self._movement*delta_time

       # if self._gameObject.transform.position.x < -self._sprite_size.x:
        #    self._gameObject.transform.position.x = self._screen_size.x
        #elif self._gameObject.transform.position.x > self._screen_size.x:
        #    self._gameObject.transform.position.x = -self._sprite_size.x

        
        if self._gameObject.transform.position.y > bottom_limit:
            self._gameObject.transform.position.y = bottom_limit
           


            
        # elif self._gameObject.transform.position.y < 0:
        #    self._gameObject.transform.position.y = 0
        
        if self._gameObject.transform.position.y == bottom_limit:
            self.can_jump = True
            self.is_falling = False
            self._down_blocked=True


     
        

    def shoot(self):
        if self._time_since_last_shot >= self._shoot_delay:
            projectile = GameObject(pygame.math.Vector2(0,0),self._game_world)
            sr = projectile.add_component(SpriteRenderer("laser.png",20,20))
            projectile.add_component(Laser())
            projectile.add_component(Collider())

        

            projectile_position = pygame.math.Vector2(self._gameObject.transform.position.x+(self._sprite_size.x/2)-sr.sprite_image.get_width()/2
                                                    ,self._gameObject.transform.position.y)
        
            projectile.transform.position = projectile_position

            self._game_world.instantiate(projectile)
            self.sound_player = SoundPlayer("laserbeam.mp3")

            self._time_since_last_shot = 0
        
    def on_collision_enter(self, other):
        
        self._animator.play_animation("Deathanimright")


        if self._animator._current_animation !="Upgraderight" and self._animator._current_animation !="Upgradeleft":

            
            self.gameObject.destroy()
            GameStateManager.currentState = GameStates.RESTART
        else:
            self._animator.play_animation(f"{self._animator._currentstate}right")
        
        print("collision enter")

    def on_collision_exit(self, other):
        print("collision exit")

    def on_pixel_collision_enter(self, other):
        print("pixel collision enter")

        

    def on_pixel_collision_exit(self, other):
        print("pixel collision exit")
    
    def on_collision_enter_top(self,other):
        
        print("collision enter top")

    def on_collision_enter_powerUp(self,other):
        self._animator=self._gameObject.get_component("Animator")
        self._animator._currentstate ="Upgrade"
        self._animator.play_animation(f"{self._animator._currentstate}right")
        print("collision enter powerup")

    
    def on_collision_enter_gun_powerup(self,other):
       print("collision gun PowerUp")
       self._can_shoot=True

    def on_collision_enter_solid_object(self,other):
        sr_enemy=other.gameObject.get_component("SpriteRenderer")
        enemyCol = sr_enemy.sprite.rect

        sr_player=self.gameObject.get_component("SpriteRenderer")
        playerCol = sr_player.sprite.rect

        player=self.gameObject.get_component("Player")

        player.can_jump = True


        print("Solid OBject collision")



        if enemyCol.bottom > playerCol.top and playerCol.centery>enemyCol.bottom:
           player._up_blocked=True
           
 

        if enemyCol.top <= playerCol.bottom:
                    
         player._down_blocked=True
        
       
                    


        if enemyCol.left < playerCol.right and playerCol.centerx < enemyCol.left:
                    
           player._right_blocked=True
                    


        if enemyCol.right > playerCol.left and playerCol.centerx > enemyCol.right:
            
            player._left_blocked=True


    def on_collision_exit_solid_object(self,other):
        player=self.gameObject.get_component("Player")
        player._right_blocked=False
        player._left_blocked=False
        player._up_blocked=False
        player._down_blocked=False

        
                    
        