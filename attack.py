import pygame
import hitbox
import model


class Attack(model.Model):
    def __init__(self, damage, effects, paths, height):
        super().__init__(paths, height, True)
        self.damage = damage
        self.cur_damage = damage
        self.effects = effects
        self.counter = len(self.common_hitboxes['default'])

    def update(self, x, y, cell, width, height, direction, crouch=False, upd=True):
        dr = direction
        if dr:
            dr = 'sos'
        super().update(x, y, cell, width, height, dr, crouch, True)
        self.counter -= 1

    def reboot(self):
        super().reboot()
        self.counter = len(self.common_hitboxes['default'])
        self.cur_damage = self.damage
