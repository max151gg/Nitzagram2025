from constants import *
from helpers import from_text_to_array,screen
class Comment:
    Text: str


    def __init__(self,Text):
        self.Text = Text


    def display(self,i):
        Font = pygame.font.SysFont("chalkduster.tff",UI_FONT_SIZE)
        text = Font.render(self.Text,True,(0,0,0))
        screen.blit(text,(FIRST_COMMENT_X_POS,FIRST_COMMENT_Y_POS + i * COMMENT_LINE_HEIGHT))
        # s = ""
        # Text_seperated = []
        # for i in range(0,len(self.Text)):
        #     s += self.Text[i]
        #
        #     if i % 24 == 0 or i == len(self.Text) - 1:
        #         Text_seperated.append(s)
        #         s = ""
        # not_sure = 0
        # for comment in Text_seperated:
        #     text_font = Font.render(comment,UI_FONT_SIZE)
        #     screen.blits(text_font,FIRST_COMMENT_X_POS,FIRST_COMMENT_Y_POS + 0)
        #     not_sure += UI_FONT_SIZE

