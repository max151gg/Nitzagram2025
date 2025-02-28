from constants import *
from Post import Post
import pygame
from helpers import *
from Filter import Filter
class ImagePost(Post):


    def __init__(self,username,location,description,Image,filter: Filter = None):
        super().__init__(username,location,description)
        self.Image = pygame.image.load(Image)
        self.Image = pygame.transform.scale(self.Image,(POST_WIDTH,POST_HEIGHT))
        self.filter = filter
    def display(self):
        super().display()
        # screen.blit(self.Image, (POST_X_POS,POST_Y_POS))
    def display_content(self):
        screen.blit(self.Image,(POST_X_POS,POST_Y_POS))
        if self.filter != None:
            self.filter.Show_filter()
