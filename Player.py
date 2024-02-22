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
from Heart import Heart



class Player(Component):

    




    def __init__(self,game_world) -> None:
        self._game_world = game_world


    
        
    
    def awake(self, game_world):
        self._time_since_last_shot = 1
        self._shoot_delay = 1
        self._can_shoot=False
        self._player_position_x = self._gameObject.transform.position.x
        self._is_jumping = False
        self._is_falling = True
        self._can_jump = False
        self._start_jump_position = 0
        
        self.gameObject.follows_camera=True
        self.gameObject.Tag = "Player"
        self.gameObject.health = 3
        self.death = False
        self.keyinactive = False

        

        sr = self._gameObject.get_component("SpriteRenderer")
        
        self._animator=self._gameObject.get_component("Animator")

        self._movement = pygame.math.Vector2(0,0)

        self._right_blocked=False
        self._left_blocked=False
        self._up_blocked=False
        self._down_blocked=False

        self._collision_Happened=False

        self._right_collision_Happened=False
        self._left_collision_Happened=False

        self._stop_gravity=False



     
      



        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(), game_world.screen.get_height())
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(),sr.sprite_image.get_height())
        self._gameObject.transform.position.x = 100
        self._gameObject.transform.position.y = (self._screen_size.y) - (self._sprite_size.y)-200        
        collider = self._gameObject.get_component("Collider")
        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit",self.on_collision_exit)
        collider.subscribe("collision_enter_top",self.on_collision_enter_top)
        collider.subscribe("pixel_collision_enter",self.on_pixel_collision_enter)
        collider.subscribe("pixel_collision_exit",self.on_pixel_collision_exit)
        collider.subscribe("collision_enter_powerUp",self.on_collision_enter_powerUp)
        
        collider.subscribe("collision_enter_gun_powerup",self.on_collision_enter_gun_powerup)

       # collider.subscribe("collision_enter_solid_object",self.on_collision_enter_solid_object)
        #collider.subscribe("collision_exit_solid_object",self.on_collision_exit_solid_object)
        
        
       
        
       




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
        

        
            

        bottom_limit = self._screen_size.y+100 -self._sprite_size.y
      

        if keys[pygame.K_a] and not self._left_blocked and self.keyinactive == False:
            self._movement.x -= speed
            self._animator.play_animation(f"{self._animator._currentstate}left")
          
           

        if keys[pygame.K_d] and not self._right_blocked and self.keyinactive == False:
            self._movement.x += speed
            self._animator.play_animation(f"{self._animator._currentstate}right")
           
           

        if keys[pygame.K_SPACE] and self.can_jump is True and self.keyinactive == False:
            self.is_falling = False
            self.can_jump = False
            self.is_jumping = True
            self._start_jump_position = player_position_y
            self._down_blocked=False
            self.sound_player = SoundPlayer("jump-small.wav")
            self.sound_player.play_sound()  
            self.sound_player.set_volume(0.05)        

        if keys[pygame.K_f] and self._can_shoot==True:

            self.shoot()
            

        #Gravity
        if self.is_falling and not self._down_blocked:
            self._movement.y += self._gravity
            


            

        #Jumping
        if self.is_jumping:
            self._movement.y -= self._gravity
            if player_position_y < (self._start_jump_position - jump_height) or self._up_blocked==True:
                self.is_jumping = False
                self.is_falling = True
                
                
        
      

   
        self.gameObject.transform.offset+=self._movement*delta_time
       
        self._gameObject.transform.translate(self._movement*delta_time)
       

        Camera.camera_offset+=self._movement*delta_time

       # if self._gameObject.transform.position.x < -self._sprite_size.x:
        #    self._gameObject.transform.position.x = self._screen_size.x
        #elif self._gameObject.transform.position.x > self._screen_size.x:
        #    self._gameObject.transform.position.x = -self._sprite_size.x

        
       # if self._gameObject.transform.position.y > bottom_limit:
       #     self._gameObject.transform.position.y = bottom_limit
           


            
        # elif self._gameObject.transform.position.y < 0:
        #    self._gameObject.transform.position.y = 0
        
        if self._gameObject.transform.position.y == bottom_limit:
            self.gameObject.destroy()
            GameStateManager.currentState = GameStates.RESTART


     
        

    def shoot(self):
        if self._time_since_last_shot >= self._shoot_delay:
            projectile = GameObject(pygame.math.Vector2(0,0),self._game_world)
            sr = projectile.add_component(SpriteRenderer("laser.png",20,20))
            if self._animator._current_animation == f"{self._animator._currentstate}right":
                projectile.add_component(Laser(500))
            elif self._animator._current_animation == f"{self._animator._currentstate}left":
                projectile.add_component(Laser(-500))

            projectile.add_component(Collider())



            shoot_offset=pygame.math.Vector2(20,0)

        

            projectile_position =self.gameObject.transform.position-self.gameObject.transform.offset+shoot_offset
        
            projectile.transform.position = projectile_position

            self._game_world.instantiate(projectile)
            

            self._time_since_last_shot = 0
        
    def on_collision_enter(self, other):

        self.gameObject.health -= 1
        

        if self.gameObject.health == 0:
            self._animator.play_animation("Deathanimright")
            self.death = True
            self.sound_player = SoundPlayer("mariodie.wav")
            self.sound_player.play_sound()  
            self.sound_player.set_volume(0.05)

            self.keyinactive = True
            
        elif self.death == True:

            GameStateManager.currentState = GameStates.RESTART

        




        
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
        self.sound_player = SoundPlayer("powerup.wav")
        self.sound_player.play_sound()  
        self.sound_player.set_volume(0.05)

        self._animator=self._gameObject.get_component("Animator")
        self._animator._currentstate ="Upgrade"
        self._animator.play_animation(f"{self._animator._currentstate}right")
        sr=self.gameObject.get_component("SpriteRenderer")
        
        sprite_height_upgrade =50
        sprite_width_upgrade = 50
       
        sr._sprite_image=pygame.transform.scale(sr._sprite_image,(sprite_height_upgrade,sprite_width_upgrade))
        sr._sprite.rect = sr._sprite_image.get_rect()
        sr._sprite_mask = pygame.mask.from_surface(sr.sprite_image)
        
        

        print("collision enter powerup")

    
    def on_collision_enter_gun_powerup(self,other):
       
       print("collision gun PowerUp")
       self._can_shoot=True
       self.sound_player = SoundPlayer("1-up.wav")
       self.sound_player.play_sound()  
       self.sound_player.set_volume(0.05)       

    def on_collision_solid_object(self,other):
        self._sr = self.gameObject.get_component("SpriteRenderer")

        self._col = self.gameObject.get_component("Collider")


        other._col=other.gameObject.get_component("Collider")
        
        sr_enemy=other.gameObject.get_component("SpriteRenderer")
        enemyCol = sr_enemy.sprite.rect

        sr_player=self.gameObject.get_component("SpriteRenderer")
        playerCol = sr_player.sprite.rect

        is_rect_colliding =pygame.Rect.colliderect(sr_player._sprite.rect,sr_enemy._sprite.rect)
     
        
        player=self.gameObject.get_component("Player")
        
        collision_Happened=False
        

        colliding_with_top=False

       # if self.check_pixel_collision(self._col._collision_box, other._col._collision_box, self._col._sprite_mask, other._col.sprite_mask):

        if is_rect_colliding==True:
          collision_Happened=True

          

          player.can_jump = True
         

          keys = pygame.key.get_pressed()

          print("SolidObject collision")

    
          if enemyCol.bottom > playerCol.top and playerCol.bottom>enemyCol.bottom:
             self._up_blocked=True
             self.is_falling=True
             self.is_jumping=False
             self.gameObject.transform.position= pygame.math.Vector2(self.gameObject.transform.position.x,sr_enemy._sprite.rect.bottom+39+other.gameObject.transform.offset.y)
          elif enemyCol.top < playerCol.bottom and playerCol.top<enemyCol.top:
             player._down_blocked=True
             colliding_with_top=True
             self.is_falling=False
             if not keys[pygame.K_SPACE] and self.is_jumping==False:
              self.gameObject.transform.position= pygame.math.Vector2(self.gameObject.transform.position.x,sr_enemy._sprite.rect.top-39+other.gameObject.transform.offset.y)
         
        
       
          if enemyCol.left < playerCol.right and playerCol.left < enemyCol.left and colliding_with_top==False:
                    
             self._right_blocked=True
             
             self._right_collision_Happened=True
             old_pos=self.gameObject.transform.position
             
             new_pos =pygame.math.Vector2(sr_enemy._sprite.rect.left-sr_player._sprite_image.get_width(),self.gameObject.transform.position.y)

            
             #self.gameObject.transform.offset+=new_pos-old_pos
             #Camera.camera_offset+=new_pos-old_pos
             self.gameObject.transform.position+= new_pos-old_pos
              
       
       
       

      
       
             
       

      
                    


          if enemyCol.right > playerCol.left and playerCol.right > enemyCol.right:
            
             

             self._left_collision_Happened=True


             old_pos2=self.gameObject.transform.position

             new_pos2=pygame.math.Vector2(sr_enemy._sprite.rect.left+sr_enemy._sprite_image.get_width(),self.gameObject.transform.position.y)

             self.gameObject.transform.position+= new_pos2-old_pos2

             Camera.camera_offset+=(new_pos2-old_pos2)*self._delta_time
             self.gameObject.transform.offset+=(new_pos2-old_pos2)*self._delta_time

           
        elif collision_Happened==True:
            
            if self._right_collision_Happened==True:
              self._right_blocked=False
              self.on_collision_solid_object_exit(other)
            
            if self._left_collision_Happened==True:
                self._left_blocked=False
                self.on_collision_solid_object_exit(other)
            collision_Happened=False

        
           

    
            
    def check_pixel_collision(self, collision_box1, collision_box2, mask1, mask2):
        offset_x = collision_box2.x - collision_box1.x
        offset_y = collision_box2.y - collision_box1.y

        return mask1.overlap(mask2,(offset_x,offset_y)) is not None

    
    def on_collision_MysteryBox(self,other):
        self._sr = self.gameObject.get_component("SpriteRenderer")

        self._col = self.gameObject.get_component("Collider")


        other._col=other.gameObject.get_component("Collider")
        
        sr_enemy=other.gameObject.get_component("SpriteRenderer")
        enemyCol = sr_enemy.sprite.rect

        sr_player=self.gameObject.get_component("SpriteRenderer")
        playerCol = sr_player.sprite.rect

        is_rect_colliding =pygame.Rect.colliderect(sr_player._sprite.rect,sr_enemy._sprite.rect)
     
        
        player=self.gameObject.get_component("Player")
        
        

       # if self.check_pixel_collision(self._col._collision_box, other._col._collision_box, self._col._sprite_mask, other._col.sprite_mask):

        if is_rect_colliding==True:
          self._collision_Happened=True

         

          player.can_jump = True
         

          keys = pygame.key.get_pressed()

          print("MysteryBox collision")

    
          if enemyCol.bottom > playerCol.top and playerCol.bottom>enemyCol.bottom:
             self._up_blocked=True
             self.is_falling=True
             self.is_jumping=False
             self.gameObject.transform.position= pygame.math.Vector2(self.gameObject.transform.position.x,sr_enemy._sprite.rect.bottom+39)
          elif enemyCol.top < playerCol.bottom and playerCol.top<enemyCol.top:
             player._down_blocked=True
             if not keys[pygame.K_SPACE] and self.is_jumping==False:
              self.gameObject.transform.position= pygame.math.Vector2(self.gameObject.transform.position.x,sr_enemy._sprite.rect.top-39)
         
        
       
          if enemyCol.left < playerCol.right and playerCol.left < enemyCol.left:
                    
             player._right_blocked=True
             
             
             self.gameObject.transform.position= pygame.math.Vector2(sr_enemy._sprite.rect.left-sr_player._sprite_image.get_width(),self.gameObject.transform.position.y)
                    


          if enemyCol.right > playerCol.left and playerCol.right > enemyCol.right:
            
             #player._left_blocked=True
             self.gameObject.transform.position= pygame.math.Vector2(sr_enemy._sprite.rect.left+sr_enemy._sprite_image.get_width(),self.gameObject.transform.position.y)

        elif self._collision_Happened==True:
            self.on_collision_exit_MysteryBox(other)
            
            self._collision_Happened=False
           



    def on_collision_solid_object_exit(self,other):
       
       # player._right_blocked=False
        self._left_blocked=False
        self._up_blocked=False
        self._down_blocked=False

    def on_collision_exit_MysteryBox(self,other):
        player=self.gameObject.get_component("Player")
        player._right_blocked=False
        player._left_blocked=False
        player._up_blocked=False
        player._down_blocked=False

        
                    
        