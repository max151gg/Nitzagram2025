import fontTools.ttLib
import pygame
from helpers import  *
from constants import *
from Post import Post
class TextPost(Post):
    background_color: tuple
    text: str
    text_color: str
    def __init__(self,username: str,location: str,description: str,text: str,text_color: tuple,background_color: tuple) -> None:
        super().__init__(username,location,description)
        self.background_color = background_color
        self.text_color = text_color
        self.text = text
        self.background_rect = pygame.Rect(POST_X_POS,POST_Y_POS,POST_WIDTH,POST_HEIGHT)


    def display_content(self):
        pygame.draw.rect(screen,self.background_color,self.background_rect)
        # Text = Font_Text_post.render(self.text,True,self.text_color)
        text_arr = from_text_to_array(self.text)
        # text_list_by_rows = ["".join(text_arr[i:i+ 20]) for i in  range(0,len(text_arr),20)]
        # print(text_list_by_rows)
        # print(text_arr)

        rows_num = len(text_arr)
        for row_number in range(rows_num):
            Text = Font_Text_post.render(text_arr[row_number], True, self.text_color)
            pos: tuple = center_text(rows_num,Text,row_number)

            screen.blit(Text,pos)

