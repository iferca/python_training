import pygame as pg

pg.init()
pg.display.set_caption("First Game")

screen_height = 500
screen_width = 500

width_of_rec = 40
height_of_rec = 60
position_on_x = 50
position_on_y = 50
speed = 5
black = (0, 0, 0)
red = (255, 0, 0)


def draw_rectangle(screen):
    pg.draw.rect(screen, red, (position_on_x, position_on_y, width_of_rec, height_of_rec))
    pg.display.update()


def check_lateral_move(keys):
    if keys[pg.K_LEFT] and position_on_x > speed:
        position_on_x -= speed

    if keys[pg.K_RIGHT] and position_on_x < screen_width - width_of_rec:
        position_on_x += speed


def run_game():
    run = True
    screen = pg.display.set_mode((screen_width, screen_height))
    while run:
        pg.time.delay(100)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        keys = pg.key.get_pressed()
        check_lateral_move(keys)
        draw_rectangle(screen)
        screen.fill(black)
    pg.quit()


run_game()