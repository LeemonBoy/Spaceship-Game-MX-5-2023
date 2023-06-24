from game.components.enemies.ship import Ship
from game.components.enemies.big_ship import Big_ship

class EnemyHandler:

    ENEMIES = ["ship", "big_ship"]
    ENEMY_SCORE_INTERVAL = {
        "ship": 5,
        "big_ship": 10

    }

    def __init__(self):
        self.enemies = [ ]
        self.number_enemies_destroyed = 0 
        self.score_interval = 0
        self.current_interval_score = 0 

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if enemy.isdestoyed:
                self.number_enemies_destroyed += 1
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len (self.enemies) < 7:
            for enemy_type, score_iterval in self.ENEMY_SCORE_INTERVAL.items():
                if self.number_ == "big_ship":
                    if self.number_enemies_destroyed >= self.score_interval and enemy_type not in self.enemies:
                        self.enemies.append(Big_ship())
                        break
                else:
                    if self.number_enemies_destroyed >= self.score_interval and enemy_type not in self.enemies:
                        if enemy_type == "ship":
                            self.enemies.append(Ship())
                        elif enemy_type == "big_ship":
                            self.enemies.append(Big_ship())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        if isinstance(enemy, Big_ship):
            self.ENEMY_SCORE_INTERVAL["big_ship"] = float("inf")

    def resset(self):
        self.enemies = []
        self.number_enemies_destroyed = 0 