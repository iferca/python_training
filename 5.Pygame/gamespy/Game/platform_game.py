import pygame as pg
from os import path

pg.init()
pg.display.set_caption("First Game")


class Player:
    position_on_x = 300
    position_on_y = 410
    width = 64
    height = 64
    right = False
    left = False
    walk_count = 0
    jump_count = 10
    is_jump = True
    speed = 5
    walk_right = [pg.image.load(path.join("Right", f'R{n}.png')) for n in range(1, 10)]
    walk_left = [pg.image.load(path.join("Left", f'L{n}.png')) for n in range(1, 10)]
    char = pg.image.load(path.join('standing.png'))
    standing = False


class Config:
    screen_height = 500
    screen_width = 500
    black = (0, 0, 0)
    red = (255, 0, 0)
    clock = pg.time.Clock()
    bg = pg.image.load(path.join("bg.jpg"))


class Projectile(object):
    def __init__(self, position_on_x, position_on_y, radius, color, facing):
        self.position_on_x = position_on_x
        self.position_on_y = position_on_y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.position_on_x, self.position_on_y), self.radius)


def draw_player(screen):
    if Player.walk_count + 1 >= 27:
        Player.walk_count = 0
    if Player.left:
        screen.blit(Player.walk_left[Player.walk_count // 3], (Player.position_on_x, Player.position_on_y))
        Player.walk_count += 1
    elif Player.right:
        screen.blit(Player.walk_right[Player.walk_count // 3], (Player.position_on_x, Player.position_on_y))
        Player.walk_count += 1
    else:
        if Player.right:
            screen.blit(Player.walk_right[0], (Player.position_on_x, Player.position_on_y))

        else:
            screen.blit(Player.walk_left[0], (Player.position_on_x, Player.position_on_y))


def draw_game(screen, bullets):
    screen.blit(Config.bg, (0, 0))
    for bullet in bullets:
        bullet.draw(screen)
    draw_player(screen)
    pg.display.update()


def check_move(keys):
    if keys[pg.K_LEFT] and Player.position_on_x > Player.speed:
        Player.position_on_x -= Player.speed
        Player.left = True
        Player.right = False
        Player.standing = False

    elif keys[pg.K_RIGHT] and Player.position_on_x < Config.screen_width - Player.width:
        Player.position_on_x += Player.speed
        Player.right = True
        Player.left = False
        Player.standing = False

    else:
        Player.standing = False
        Player.walk_count = 0


def jump(keys):
    if Player.is_jump:

        if keys[pg.K_UP]:
            Player.is_jump = False
            Player.right = False
            Player.left = False
            Player.walk_count = 0

    else:
        if Player.jump_count >= -10:
            neg = 1
            if Player.jump_count < 0:
                neg = -1
            Player.position_on_y -= (Player.jump_count ** 2) / 2 * neg
            Player.jump_count -= 1
        else:

            Player.is_jump = True
            Player.jump_count = 10


def run_game():
    bullets = []
    run = True
    screen = pg.display.set_mode((Config.screen_width, Config.screen_height))
    while run:

        Config.clock.tick(27)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        for bullet in bullets:
            if 500 > bullet.position_on_x > 0:
                bullet.position_on_x += bullet.speed
            else:
                bullets.pop(bullets.index(bullet))
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            if Player.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 3:
                bullets.append(
                    Projectile(round(Player.position_on_x + Player.width // 2),
                               round(Player.position_on_y + Player.height // 2), 6, Config.black,
                               facing))
        jump(keys)
        check_move(keys)
        draw_game(screen, bullets)
    pg.quit()


run_game()
