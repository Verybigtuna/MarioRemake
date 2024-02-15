from Components import Component
import pygame
from GameObject import GameObject
from Components import Laser
from Components import SpriteRenderer
from Camera import Camera
class Player(Component):

    #def __init__(self) -> None:

    
        
    
    def awake(self, game_world):
        self._time_since_last_shot = 1
        self._shoot_delay = 1
        self._game_world = game_world
        self._is_jumping = False
        self._is_falling = True
        self._can_jump = False
        self._start_jump_position = 0
        
        self.gameObject.follows_camera=True
        self.gameObject.Tag = "Player"
        
        sr = self._gameObject.get_component("SpriteRenderer")
        
        self._animator=self._gameObject.get_component("Animator")

     

      



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
        movement = pygame.math.Vector2(0,0)
        Camera.camera_offset=pygame.math.Vector2(0,0)

        self._time_since_last_shot += delta_time
        gravity = 700
        jump_height = 300
        
        player_position_y = self._gameObject.transform.position.y

        bottom_limit = self._screen_size.y-100 -self._sprite_size.y
        if keys[pygame.K_w]:
            movement.y -= speed
            

        if keys[pygame.K_s] and self.gameObject.transform.position.y<bottom_limit:
            movement.y += speed

        if keys[pygame.K_a]:
            movement.x -= speed
            self._animator.play_animation(f"{self._animator._currentstate}left")
           

        if keys[pygame.K_d]:
            movement.x += speed
            self._animator.play_animation(f"{self._animator._currentstate}right")
           

        if keys[pygame.K_SPACE] and self.can_jump is True:
            self.is_falling = False
            self.can_jump = False
            self.is_jumping = True
            self._start_jump_position = player_position_y
            

        #Gravity
        if self.is_falling:
            movement.y += gravity

        #Jumping
        if self.is_jumping:
            movement.y -= gravity
            if player_position_y < (self._start_jump_position - jump_height):
                self.is_jumping = False
                self.is_falling = True

        self._gameObject.transform.translate(movement*delta_time)
        self.gameObject.transform.offset+=movement*delta_time


        



        Camera.camera_offset+=movement*delta_time

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


     
        

    def shoot(self):
        if self._time_since_last_shot >= self._shoot_delay:
            projectile = GameObject(None)
            sr = projectile.add_component(SpriteRenderer("laser.png"))
            projectile.add_component(Laser())

            projectile_position = pygame.math.Vector2(self._gameObject.transform.position.x+(self._sprite_size.x/2)-sr.sprite_image.get_width()/2
                                                    ,self._gameObject.transform.position.y-40)
        
            projectile.transform.position = projectile_position

            self._game_world.instantiate(projectile)

            self._time_since_last_shot = 0
        
    def on_collision_enter(self, other):
        
        if self._animator._current_animation !="Upgraderight" and self._animator._current_animation !="Upgradeleft":

            self.gameObject.destroy()
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