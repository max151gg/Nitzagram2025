from constants import *
from Post import Post
import pygame
from helpers import *
class ImagePost(Post):


    def __init__(self,username,location,description,Image):
        super().__init__(username,location,description)
        self.Image = pygame.image.load(Image)
        self.Image = pygame.transform.scale(self.Image,(POST_WIDTH,POST_HEIGHT))

    def display(self):
        super().display()
        # screen.blit(self.Image, (POST_X_POS,POST_Y_POS))
    def display_content(self):
        screen.blit(self.Image,(POST_X_POS,POST_Y_POS))
