from constants import *
from helpers import *




class Heart:
    Heart_Size:int


    def __init__(self,x_pos,y_pos = WINDOW_HEIGHT , Heart_Size = 30,Heart_speed = 20) ->None:
        self.x_pos = x_pos
        self.y_pos = WINDOW_HEIGHT
        self.Heart_Size = Heart_Size
        self.Heart_Image = pygame.image.load("Images/heart.png")
        self.Heart_Image = pygame.transform.scale(self.Heart_Image,(Heart_Size,Heart_Size))
        self.Heart_Speed = Heart_speed


    def move(self):
        print("func works")
        print(f"x_pos: {self.x_pos}, y_pos: {self.y_pos}")
        self.y_pos -= self.Heart_Speed
        screen.blit(self.Heart_Image,(self.x_pos,self.y_pos))
