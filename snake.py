
from configs import Configs
from square import Square


class Snake(Square):

    def __init__(self, x=20, y=20, color='white'):
        super().__init__(x, y, color)
        self.x = x
        self.y = y
        self.color = color

    def create(self):
        return [ 
            Square(self.x, self.y, self.color)
            , Square(self.x, self.y, self.color)
            , Square(self.x, self.y, self.color)
            , Square(self.x, self.y, self.color)
        ]