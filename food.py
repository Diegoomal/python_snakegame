
import numpy as np
from configs import Configs
from square import Square


class Food(Square):

    def __init__(self, x=20, y=20, color='purple'):
        super().__init__(x, y, color)
        self.x = self.get_random_position_x()
        self.y = self.get_random_position_y()
        self.color = color
        
    def create(self):
        return [ Square(self.x, self.y, self.color) ]
    
    def get_random_position_x(self):
        return np.random.randint(Configs.GRID_SIZE, (Configs.WIDTH/Configs.GRID_SIZE)) * Configs.GRID_SIZE - Configs.GRID_SIZE
    
    def get_random_position_y(self):
        return np.random.randint(Configs.GRID_SIZE, (Configs.HEIGHT/Configs.GRID_SIZE)) * Configs.GRID_SIZE - Configs.GRID_SIZE