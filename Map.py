from Components import Component
import pygame
class Map(Component):

    def awake(self, game_world):
        
        self._game_world = game_world

        sr = self._gameObject.get_component("SpriteRenderer")


        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(), game_world.screen.get_height())
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(),sr.sprite_image.get_height())
        #self._gameObject.transform.position.x = (self._screen_size.x) - (self._sprite_size.x)
        self._gameObject.transform.position.y = (self._screen_size.y) - (self._sprite_size.y)
        collider = self._gameObject.get_component("Collider")
        collider.subscribe("collider_ground",self.on_ground_collision)


    def start(self):
        pass

    def update(self, delta_time):
        pass

    def on_ground_collision(self, other):
        pass