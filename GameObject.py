import pygame
from Components import Transform


class GameObject:

    def __init__(self, position,game_world) -> None:
        self._components = {}
        self._transform = self.add_component(Transform(position))
        self._is_destroyed = False
        self._game_world=game_world
        self._Tag = "UnTaggedObject"

    @property
    def transform(self):
        return self._transform
    @property
    def Tag(self):
        return self._Tag
    
    @Tag.setter
    def Tag(self, value):
        self._Tag = value
    @property
    def is_destroyed(self):
        return self._is_destroyed

    def destroy(self):
        self._is_destroyed = True
        collider = self.get_component("Collider")
        self._game_world.colliders.remove(collider)
    



    def add_component(self, component):
        component_name = component.__class__.__name__
        self._components[component_name] = component
        component.gameObject = self
        return component
    
    def get_component(self, component_name):
        return self._components.get(component_name,None)

    def awake(self, game_world):
        for component in self._components.values():
            component.awake(game_world)

    def start(self):
        for component in self._components.values():
            component.start()

    def update(self, delta_time):
        for component in self._components.values():
            component.update(delta_time)