import pygame.mouse

import helpers
from helpers import screen,mouse_in_button,draw_comment_text_box,read_comment_from_user
from constants import *
from classes.Comment import Comment
from ImagePost import ImagePost
from buttons import *
def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here

    running = True
    test = Comment("blabla")
    test.display(1)

    POST_INDEX = 0
    POSTS = [ImagePost("Blade", "Max apartment", "BOOO", "Images/20230918_172609.jpg"), \
             ImagePost("Blade", "Max apartment", "MAX AND I ARE CHILLING", "Images/20230918_172624.jpg"), \
             ImagePost("Blade", "Max apartment", "Max is starving me to death:(", "Images/20230918_172632.jpg"), \
             ImagePost("Blade", "Max apartment", "I am going to vacation wish me luck:)", "Images/20230918_172648.jpg"), \
             ImagePost("Blade", "Max apartment", "Why is max father so hot?????",
                       "Images/rn_image_picker_lib_temp_b2cedd25-01d7-4544-99d7-751480f4eb3b.jpg"), \
             ImagePost("Blade", "Max apartment", "I am starting my own business", "Images/02ef4b2047d0fbd8.png")]
    Post1 = ImagePost("blabla", "nig", "NMone", r"Images\noa_kirel.jpg")
    while running:
        first_comment = 0
        # Post1.display()
        Post1.add_cooment(test)
        mouse_x,mouse_y = pygame.mouse.get_pos()
        poses =pygame.mouse.get_pos()
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(click_post_button,(poses)):
                    if POST_INDEX == len(POSTS) -1 :
                        POST_INDEX = 0
                    POST_INDEX += 1
                if mouse_in_button(like_button,poses):
                    POSTS[POST_INDEX].Add_Like()
                if mouse_in_button(comment_button,poses):
                    draw_comment_text_box()
                    new_comment = read_comment_from_user()
                    new_comment = Comment(new_comment)
                    POSTS[POST_INDEX].add_cooment(new_comment)
                if mouse_in_button(view_more_comments_button,poses) :
                    if POSTS[POST_INDEX].comments_display_index >= len(POSTS[POST_INDEX].comments):
                        POSTS[POST_INDEX].comments_display_index = 4
                    else:
                        POSTS[POST_INDEX].comments_display_index += 4

        # helpers.read_comment_from_user()

        # Display the background, presented Image, likes, comments, tags and location(on the Image)

        Ofek_Shani_choen = Comment("I am dying on you!!!!!!!!!!!")
        # Ofek_Shani_choen.display(1)





        #----------------------------------------------------------------------------------
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        # Post1.display()

        POSTS[POST_INDEX].display()
        # print(POSTS[POST_INDEX].likes_counter)
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
