# importing the required libraries
import pygame as pg
from os import path

# initializing the pygame window
pg.init()
# set a title
pg.display.set_caption("First Game")
#  Since there are so many images, saving them in lists may be useful later on.
walkRight = [pg.image.load(path.join("Right", f'R{n}.png')) for n in range(1, 10)]
walkLeft = [pg.image.load(path.join("Left", f'L{n}.png')) for n in range(1, 10)]

bg = pg.image.load('bg.jpg')
char = pg.image.load('standing.png')
# declaring the global variables
width_of_rec = 40
height_of_rec = 60
position_on_x = 50
position_on_y = 50
speed = 5
# color to use later
black = (0, 0, 0)
red = (255, 0, 0)
# set the width and height of the game window
screen_width, screen_height = 500, 500

screen = pg.display.set_mode((screen_width, screen_height))

left = False
right = False
is_jump = True
walk_count = 0
jump_count = 10
# a loop that prevents the game from closing and allows you to close it with the close button.
run = True
while run:
    pg.time.delay(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # add movement to the character (the coordinates start on the left corner of the screen)
    # character cannot leave the screen
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and position_on_x > speed:
        position_on_x -= speed
    if keys[pg.K_RIGHT] and position_on_x < screen_width - width_of_rec:
        position_on_x += speed
    # character jump
    if is_jump:

        if keys[pg.K_SPACE]:
            is_jump = False
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            position_on_y -= (jump_count ** 2) / 2 * neg
            jump_count -= 1
        else:
            is_jump = True
            jump_count = 10

    # draw a character
    pg.draw.rect(screen, red, (position_on_x, position_on_y, width_of_rec, height_of_rec))
    pg.display.update()
    screen.fill(black)
pg.quit()
