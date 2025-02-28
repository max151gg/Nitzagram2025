import pygame

from constants import *
from Post import Post
class TextPost(Post):
    def __init__(self,username,location,description,text,text_color,background_color) -> None:
        super().__init__(username,location,description)
        self.background_color = background_color
        self.text_color = text_color
        self.text = text
        self.background_rect = pygame.Rect(POST_X_POS,POST_Y_POS,POST_WIDTH,POST_HEIGHT)

    def display_content(self):
        pygame.draw.rect()

