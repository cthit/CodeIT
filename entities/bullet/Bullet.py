import pygame

from behaviours.Collide import Collide
from behaviours.Health import Health
from behaviours.KnockBack import KnockBack
from entities.base.Entity import Entity
from src.GameMethods import GameMethods
from tiles.base.Tile import Tile


class Bullet(Entity):
    def __init__(self, x, y, name):
        Entity.__init__(self, x, y, name)
        c = self.get_behaviour(Collide)
        self.velocity = pygame.Vector2(0, 0)
        self.damage = 10
        self.mass = 10
        self.set_height(0.2)
        self.set_width(0.4)

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        super().update(delta_time, keys, config, game_methods)
        c = self.get_behaviour(Collide)
        if self.velocity.x < 0:
            self.is_flipped_x = True
        for colliding in c.check_inside():
            if isinstance(colliding, Tile):
                self.die()
                return
            health: Health = colliding.get_behaviour(Health)
            knock_back: KnockBack = colliding.get_behaviour(KnockBack)
            if knock_back is not None:
                knock_back.push(self.velocity, self.mass)
            if health is not None:
                health.damage(self.damage)
            game_methods.play_sound("hit-02.wav")
            self.die()

    def set_damage(self, damage):
        self.damage = damage

    def set_velocity(self, velocity):
        self.velocity = velocity







