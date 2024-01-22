import random

from weapon import weapons
from health_bar import HealthBar

class Character:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = random.choice(weapons)

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()

class Player(Character):

    def __init__(self, name, health):
        super().__init__(name=name, health=health)
        self.health_bar = HealthBar(self)

    def equip(self, weapon):
        self.weapon = weapon
        print(f'{self.name.upper()} hit with {self.weapon.name.upper()}')


class Enemy(Character):

    def __init__(self, name, health):
        super().__init__(name=name, health=health)
        self.health_bar = HealthBar(self)

    def equip(self, weapon):
        self.weapon = weapon
        print(f'{self.name.upper()} hit with {self.weapon.name.upper()}')

