from game.components.power_up.power_up import PowerUp
from game.utils.constants import SHIELD

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        super().init(self.image) 