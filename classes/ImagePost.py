from classes.Post import Post
from helpers import *
from classes.Filter import Filter
import pywhatkit
class ImagePost(Post):


    def __init__(self,username,location,description,Image,filter: Filter = None):
        super().__init__(username,location,description)
        self.Image_Path = Image
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
    def share(self,phone_number) ->None:
        pywhatkit.sendwhats_image(phone_number,self.Image_Path,self.description)
        print("message_succeed.")
