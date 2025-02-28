from constants import *
from helpers import *
class Filter:


    def __init__(self,Filter_color, Alpha: int):
        self.Filter_color = Filter_color
        self.Alpha = Alpha
        self.Filter_rect = pygame.Surface((POST_WIDTH,POST_HEIGHT))
        self.Filter_rect.set_alpha(Alpha)
        self.Filter_rect.fill(Filter_color)


    def Show_filter(self):
        screen.blit(self.Filter_rect,(POST_X_POS,POST_Y_POS))
