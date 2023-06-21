import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2

class Ship(Enemy):
    WIDTH = 40
    HEIGTH = 60

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)

class Big_ship(Enemy):
    WIDTH = 100
    HEIGTH = 100
    SPEED_X = 5
    SPEED_Y = 5


    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)