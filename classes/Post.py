import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    username: str
    location: str
    description: str
    likes_counter:int
    comments: any
    def __init__(self,username,location,description) -> None : #TODO: add parameters
        #TODO: write me!
        self.username =username
        self.location=location
        self.description=description
        self.likes_counter= 0
        self.comments = []
        pass

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        #leave it
        pass

    def display_header(self):
        Font = pygame.font.SysFont('ttf.chalkduster',UI_FONT_SIZE)
        User_Name = Font.render(self.username)
        screen.blits(User_Name, USER_NAME_X_POS,USER_NAME_Y_POS)
        location = Font.render(self.location)
        screen.blits(location,LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS)
        likes = Font.render(self.likes_counter)
        screen.blits(likes,LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS)

    def display_likes(self):
        self.likes_counter += 1

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



