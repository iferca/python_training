import pygame as pg
from os import path

pg.init()
pg.display.set_caption("First Game")


class Config:
    screen_height = 500
    screen_width = 500
    width_of_rec = 64
    height_of_rec = 64
    position_on_x = 50
    position_on_y = 50
    speed = 5
    black = (0, 0, 0)
    red = (255, 0, 0)
    jump_count = 10
    is_jump = True
    walkRight = [pg.image.load(path.join("Right", f'R{n}.png')) for n in range(1, 10)]
    walkLeft = [pg.image.load(path.join("Left", f'L{n}.png')) for n in range(1, 10)]
    char = pg.image.load('standing.png')
    bg = pg.image.load('bg.jpg')
    right = False
    left = False
    walk_count = 0


def draw_rectangle(screen):
    pg.draw.rect(screen, Config.red,
                 (Config.position_on_x, Config.position_on_y, Config.width_of_rec, Config.height_of_rec))
    pg.display.update()


def check_lateral_move(keys):
    if keys[pg.K_LEFT] and Config.position_on_x > Config.speed:
        Config.position_on_x -= Config.speed

    if keys[pg.K_RIGHT] and Config.position_on_x < Config.screen_width - Config.width_of_rec:
        Config.position_on_x += Config.speed


def jump(keys):
    if Config.is_jump:

        if keys[pg.K_SPACE]:
            Config.is_jump = False
    else:
        if Config.jump_count >= -10:
            neg = 1
            if Config.jump_count < 0:
                neg = -1
            Config.position_on_y -= (Config.jump_count ** 2) / 2 * neg
            Config.jump_count -= 1
        else:
            Config.is_jump = True
            Config.jump_count = 10


def run_game():
    run = True
    screen = pg.display.set_mode((Config.screen_width, Config.screen_height))
    while run:
        pg.time.delay(100)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()
        jump(keys)
        check_lateral_move(keys)
        draw_rectangle(screen)
        screen.fill(Config.black)
    pg.quit()


run_game()
