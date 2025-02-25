import pygame
from helpers import screen
from constants import *
from Comment import Comment
from ImagePost import ImagePost

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


    while running:
        Post1 = ImagePost("blabla","nig","NMone",r"Images\noa_kirel.jpg")
        Post1.display()
        mouse_x,mouse_y = pygame.mouse.get_pos()
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_x > POST_X_POS and \
                    mouse_x < POST_X_POS + POST_WIDTH and mouse_y < POST_Y_POS \
                    and mouse_y < POST_Y_POS + POST_HEIGHT :
                pass


        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        Ofek_Shani_choen = Comment("I am dying on you!!!!!!!!!!!")
        Ofek_Shani_choen.display(1)






        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
