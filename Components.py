import pygame
from abc import ABC, abstractmethod

class Component(ABC):

    def __init__(self) -> None:
        super().__init__()
        self._gameObject =None
        


    @property
    def gameObject(self):
        return self._gameObject
    
    @gameObject.setter
    def gameObject(self,value):
        self._gameObject = value

    @abstractmethod
    def awake(self, game_world):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass


class Transform(Component):

    def __init__(self, position) -> None:
        super().__init__()

        self._position = position
        self._offset=pygame.math.Vector2(0,0)


    @property
    def position(self):
        return self._position
    
    
    @position.setter
    def position(self, value):
        self._position = value
    
    @property
    def offset(self):
        return self._offset
    
    
    @offset.setter
    def offset(self, value):
        self._offset = value



    def translate(self, direction):
        self._position += direction

    def awake(self, game_world):
        
        pass

    
    def start(self):
        pass

    
    def update(self, delta_time):
        pass


    
class MapRenderer(Component):
    def __init__(self,sprite_name,width, height)-> None:
        super().__init__()

        self._sprite_image = pygame.image.load(f"Assets\\{sprite_name}")
        self._sprite = pygame.sprite.Sprite()
        self._sprite_image=pygame.transform.scale(self._sprite_image,(width,height))
        self._sprite.rect = self._sprite_image.get_rect()
        self._sprite_mask = pygame.mask.from_surface(self.sprite_image)

      
        self._maps = {}
        self._current_map = None

    def add_map(self,name,width,height,sprite_Name):
      
        sprite_image = pygame.image.load(f"Assets\\{sprite_Name}")
        sprite_image=pygame.transform.scale(sprite_image,(width,height))
            
            
        self._maps[name] = sprite_image

    
    def setMap(self, map_Name):

        self._current_map = map_Name
    


    
        
        
    
    @property
    def sprite_image(self):
        return self._sprite_image
    


    
    @property
    def sprite_get_rect_bottom(self):
        return self._sprite_image.get_rect().bottom
    
    @property
    def sprite_get_rect_top(self):
        return self._sprite_image.get_rect().top
    

    @property
    def sprite_get_rect_right(self):
        return self._sprite_image.get_rect().right
    

    @property
    def sprite_get_rect_left(self):
        return self._sprite_image.get_rect().left


    @property
    def sprite(self):
        return self._sprite
    
    @property
    def sprite_mask(self):
        return self._sprite_mask

    @sprite_image.setter
    def sprite_image(self, value):
        self._sprite_image = value

    def awake(self, game_world):
        self._game_world = game_world
        self._sprite.rect.topleft = self.gameObject.transform.position

    
    def start(self):
        pass

    
    def update(self, delta_time):

       if len(self._maps)>0:
         self._sprite.rect.topleft = self.gameObject.transform.position-self.gameObject.transform.offset
         self._game_world.screen.blit(self._maps[self._current_map], self._sprite.rect)

    
    def scale(self,width,height):
        self.sprite_image=pygame.transform.scale(self.sprite_image,(width,height))



class SpriteRenderer(Component):

    def __init__(self, sprite_name,width,height) -> None:
        super().__init__()


        self._sprite_image = pygame.image.load(f"Assets\\{sprite_name}")
        self._sprite = pygame.sprite.Sprite()
        self._sprite_image=pygame.transform.scale(self._sprite_image,(width,height))
        self._sprite.rect = self._sprite_image.get_rect()
        self._sprite_mask = pygame.mask.from_surface(self.sprite_image)
      
        
        
    
    @property
    def sprite_image(self):
        return self._sprite_image
    
    @property
    def sprite_get_rect(self):
        return self._sprite_image.get_rect()

    
    @property
    def sprite_get_rect_bottom(self):
        return self._sprite_image.get_rect().bottom
    
    @property
    def sprite_get_rect_top(self):
        return self._sprite_image.get_rect().top
    

    @property
    def sprite_get_rect_right(self):
        return self._sprite_image.get_rect().right
    

    @property
    def sprite_get_rect_left(self):
        return self._sprite_image.get_rect().left


    @property
    def sprite(self):
        return self._sprite
    
    @property
    def sprite_mask(self):
        return self._sprite_mask

    @sprite_image.setter
    def sprite_image(self, value):
        self._sprite_image = value

    def awake(self, game_world):
        self._game_world = game_world
        self._sprite.rect.topleft = self.gameObject.transform.position

    
    def start(self):
        pass

    
    def update(self, delta_time):
        


       
        self._sprite.rect.topleft = self.gameObject.transform.position-self.gameObject.transform.offset
        self._game_world.screen.blit(self._sprite_image, self._sprite.rect)
        color = (255,0,0)
          
        # Drawing Rectangle
        pygame.draw.rect(self._game_world.screen, color, self._sprite.rect,2)
       

        

    
    def scale(self,width,height):
        self.sprite_image=pygame.transform.scale(self.sprite_image,(width,height))

    





class Animator(Component):

    def __init__(self) -> None:
        super().__init__()
        self._animation = {}
        self._current_animation = None
        self._animation_time = 0
        self._current_frame_index = 0
        self._currentstate = "Idle"
        self._thisstate = "Gunbrother_"

    def add_animation(self, name,width,height, *args,):
        frames = []
        for arg in args:
            sprite_image = pygame.image.load(f"Assets\\{arg}")
            sprite_image=pygame.transform.scale(sprite_image,(width,height))
            frames.append(sprite_image)
        
        self._animation[name] = frames

  

    def play_animation(self, animation):

        self._current_animation = animation

    def awake(self, game_world):
        self._sprite_renderer = self._gameObject.get_component("SpriteRenderer")

    def start(self):
        pass

    def update(self, delta_time):
        frame_duration = 0.1
        

        self._animation_time += delta_time
        # tjekker om den skal skifte frame
        if self._animation_time >= frame_duration:
            self._animation_time = 0
            self._current_frame_index += 1
            #får animation
            animation_sequence = self._animation[self._current_animation]

            if self._current_frame_index >= len(animation_sequence):
                self._current_frame_index = 0 # reset animation
            #skifter sprite
            self._sprite_renderer.sprite_image = animation_sequence[self._current_frame_index]


class Laser(Component):

    def __init__(self,speed) -> None:
        self._speed = speed
        

    def awake(self, game_world):
        self.gameObject.Tag = "Projectile"

    def start(self):
        pass

    def update(self, delta_time):
        
        movement = pygame.math.Vector2(self._speed,0)
        
        self._gameObject.transform.translate(movement*delta_time)

        if self._gameObject.transform.position.y < 0:
            self._gameObject.destroy()

class EnemyLaser(Component):
    def __init__(self,speed) -> None:
        self._speed = speed
        

    def awake(self, game_world):
        self.gameObject.Tag = "EnemyProjectile"
        self._bullet_time = 1

    def start(self):
        pass

    def update(self, delta_time):

        self._bullet_time += delta_time

        if self._bullet_time == 4:
            self.gameObject.destroy()
            self._bullet_time = 0       
        movement = pygame.math.Vector2(self._speed,0)
        
        self._gameObject.transform.translate(movement*delta_time)

        if self._gameObject.transform.position.y < 0:
            self._gameObject.destroy()

class Collider(Component):
    
    def __init__(self) -> None:
        self._other_colliders = []
        self._other_masks = []
        self._listeners = {}

    @property
    def collision_box(self):
        return self._collision_box
    

    
    @property
    def sprite_mask(self):
        return self._sprite_mask
    
    @property
    def sr(self):
        return self._sr

    def subscribe(self, service, method):
        self._listeners[service] = method

    def awake(self, game_world):
        self._sr = self.gameObject.get_component("SpriteRenderer")
        self._collision_box = self._sr.sprite.rect

        self._rect=self._sr.sprite.rect
        
        self._top_collision=False
        
    
        self._sprite_mask = self._sr.sprite_mask
        game_world.colliders.append(self)

      

    def start(self):
        pass

    def update(self, delta_time):
        pass

    def collision_check(self, other):
        
        self._sr = self.gameObject.get_component("SpriteRenderer")

        #is_rect_colliding = self._collision_box.colliderect(other._collision_box)
        
        is_rect_colliding =pygame.Rect.colliderect(self._sr.sprite.rect,other._sr.sprite.rect)
       
        if self.gameObject.Tag=="Player" and other.gameObject.Tag=="SolidObject" :
            p=self.gameObject.get_component("Player")
            p.on_collision_solid_object(other)

        if self.gameObject.Tag=="Player" and other.gameObject.Tag=="MysteryBox" :
            p=self.gameObject.get_component("Player")
            p.on_collision_MysteryBox(other)

      


        
        
        is_already_colliding = other in self._other_colliders

       



        if is_rect_colliding:


           



            if(self._rect.bottom>other._rect.top and other._rect.bottom>self._rect.bottom  and self.gameObject.Tag == "Player" and other.gameObject.Tag == "Enemy"):
                if not is_already_colliding:
                 other.collision_enter_top(self)
                
            
                #self._top_collision==True
            if self.gameObject.Tag=="Player":
                 
             match other.gameObject.Tag:
                case "Enemy":
                 if  not is_already_colliding:
                   self.collision_enter(other)

                 
                 #other.collision_enter(self)
             #if self.check_pixel_collision(self._collision_box, other.collision_box, self._sprite_mask, other.sprite_mask):
              #  if other not in self._other_masks:
              #      self.pixel_collision_enter(other)
               #     other.pixel_collision_enter(self)
                
             #else:
              #  if other in self._other_masks:
                #    self.pixel_collision_exit(other)
               #     other.pixel_collision_exit(self)
                case "PowerUp":
                
                 if  not is_already_colliding:
                   self.collision_enter_powerUp(other)
                   other.collision_enter_powerUp(self)
           
                case "gun_powerup":
       
                  if  not is_already_colliding:
                   self.collision_enter_gun_powerUp(other)
                   other.collision_enter_gun_powerUp(self)

               
                   
                   

               

                case "Door":
                 if  not is_already_colliding:
                  self.collision_enter(other)
                  other.collision_enter(self)

                    

            if self.gameObject.Tag == "Projectile" and other.gameObject.Tag == "Enemy":
                 
                if  not is_already_colliding:
                 self.collision_enter_projectile(other)
                 other.collision_enter_projectile(self)

            if self.gameObject.Tag == "Player" and other.gameObject.Tag == "EnemyProjectile":
                 
                if  not is_already_colliding:
                 self.collision_enter_projectile(other)
                 other.collision_enter_projectile(self)
        
         
          


        else:
            if is_already_colliding:
                
                #self.collision_exit_MysteryBox(other)
                self.collision_exit(other)
                #other.collision_exit_solid_object(self)
           
            #if self.gameObject.Tag=="Player":
             #p=self.gameObject.get_component("Player")
             #p.on_collision_solid_object_exit(other)
            

            
               
               
               
               


              
                
                

                



    def check_pixel_collision(self, collision_box1, collision_box2, mask1, mask2):
        offset_x = collision_box2.x - collision_box1.x
        offset_y = collision_box2.y - collision_box1.y

        return mask1.overlap(mask2,(offset_x,offset_y)) is not None



    def collision_enter(self, other):
        self._other_colliders.append(other)
        if "collision_enter" in self._listeners:
            self._listeners["collision_enter"](other)
    
    def collision_exit(self, other):
        self._other_colliders.remove(other)
        if "collision_exit" in self._listeners:
            self._listeners["collision_exit"](other)

    def pixel_collision_enter(self,other):
        self._other_masks.append(other)
        if "pixel_collision_enter" in self._listeners:
            self._listeners["pixel_collision_enter"](other)

    def pixel_collision_exit(self,other):
        self._other_masks.remove(other)
        if "pixel_collision_exit" in self._listeners:
            self._listeners["pixel_collision_exit"](other)
    
    def collision_enter_top(self, other):
        self._other_colliders.append(other)
        if "collision_enter_top" in self._listeners:
            self._listeners["collision_enter_top"](other)
    
    def collision_exit_top(self,other):
        self._other_colliders.remove(other)

        if "collition_exit_top" in self._listeners:
          self._listeners["collision_exit_top"](other)

    

    def collision_enter_powerUp(self, other):
        self._other_colliders.append(other)
        if "collision_enter_powerUp" in self._listeners:
            self._listeners["collision_enter_powerUp"](other)
    
    def collision_exit_powerUp(self,other):
        self._other_colliders.remove(other)

        if "collition_exit_powerUp" in self._listeners:
          self._listeners["collision_exit_powerUp"](other)

    
    def collision_enter_gun_powerUp(self, other):
        self._other_colliders.append(other)
        if "collision_enter_gun_powerup" in self._listeners:
            self._listeners["collision_enter_gun_powerup"](other)
    
    def collision_exit_gun_powerUp(self,other):
        self._other_colliders.remove(other)

        if "collition_exit_gun_powerUp" in self._listeners:
          self._listeners["collision_exit_gun_powerup"](other)
    
    
    
    def collision_enter_solid_object(self, other):
       # self._other_colliders.append(other)
        if "collision_enter_solid_object" in self._listeners:
            self._listeners["collision_enter_solid_object"](other)

    def collision_exit_solid_object(self, other):
       
        if "collision_exit_solid_object" in self._listeners:
            self._listeners["collision_exit_solid_object"](other)

    def collision_enter_projectile(self, other):
         self._other_colliders.append(other)
         if "collision_enter_projectile" in self._listeners:
            self._listeners["collision_enter_projectile"](other)

    def collision_enter_MysteryBox(self, other):
        self._other_colliders.append(other)
        if "collision_enter_MysteryBox" in self._listeners:
         self._listeners["collision_enter_MysteryBox"](other)
    
    def collision_exit_MysteryBox(self, other):
       
        if "collision_exit_MysteryBox" in self._listeners:
            self._listeners["collision_exit_MysteryBox"](other)

    
    def collision_enter_MysteryBox_bottom(self, other):
        self._other_colliders.append(other)
        if "collision_enter_bottom" in self._listeners:
         self._listeners["collision_enter_bottom"](other)




    
class MusicPlayer:
    def __init__(self,music_file):
        pygame.mixer.init()

        self.music_file = music_file
        
        self.load_music()
    
    def load_music(self):

        pygame.mixer.music.load(f"Assets\\{self.music_file}")
    
    def play_music(self, loop_count =-1 ):
        pygame.mixer.music.play(loop_count)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
         pygame.mixer.music.pause()

    def unpause_music(self):
         pygame.mixer.music.unpause()

    def set_volume(self,volume):
         
        pygame.mixer.music.set_volume(volume)
     
class SoundPlayer:
    def __init__(self,sound_file):

        pygame.mixer.init()
        self.sound_file = sound_file
        
        self.sound = pygame.mixer.Sound(f"Assets\\{self.sound_file}")
    
    def play_sound(self):
        self.sound.play()

    def set_volume(self,volume):
         
        pygame.mixer.Sound.set_volume(self.sound,volume)


    

class Camera(Component):

    camera_Position_x = 0
    movement = 0

    def __init__(self):
       
        type(self).camera_Position_x = 0
        Camera._movement = 0

    @staticmethod
    def get_movement():
        return Camera._movement

    @staticmethod
    def set_movement(value):
        Camera._movement = value

    @staticmethod
    def get_camera_position():
        return Camera._camera_position

    @staticmethod
    def set_camera_position(value):
        Camera._camera_position = value

    def update(self, delta_time):
        self.move_camera(self.get_movement())

    def move_camera(self, movement):
        
        #type(self).camera_Position.x += movement
        pass
        
        # key_state = pygame.key.get_pressed()
        # #her burde man definere hvis man er i Playing gamestate.
        # self._camera_position.y = 0
        # if self._camera_position.x < 0:
        #         self._camera_position.x = 0

        # if key_state[pygame.K_a] and self._camera_position.x > 0:
        #     self._camera_position += pygame.math.Vector2(-1, 0) * self._movement
        # if key_state[pygame.K_d] and self._camera_position.x < 1220:
        #     self._camera_position += pygame.math.Vector2(1, 0) * self._movement
    def collision_enter_projectile(self, other):
        self._other_colliders.append(other)
        if "collision_projectile" in self._listeners:
            self._listeners["collision_projectile"](other)
    
    
    def collision_enter_solid_object(self, other,is_already_colliding):
        
        if not is_already_colliding:
         self._other_colliders.append(other)

         if "collision_enter_solid_object" in self._listeners:
            self._listeners["collision_enter_solid_object"](other)
    
    def collision_exit_solid_object(self,other):
        
    
        

        if "collision_exit_solid_object" in self._listeners:
          
          self._listeners["collision_exit_solid_object"](other)

    

    

    

