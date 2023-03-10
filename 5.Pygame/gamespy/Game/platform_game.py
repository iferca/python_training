import pygame as pg
from os import path

pg.init()
pg.font.init()
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


class Enemy(object):
    walk_right = [pg.image.load(path.join("RightE", f'R{n}E.png')) for n in range(1, 12)]
    walk_left = [pg.image.load(path.join("LeftE", f'L{n}E.png')) for n in range(1, 12)]

    def __init__(self, position_on_x, position_on_y, width, height, end):
        self.position_on_x = position_on_x
        self.position_on_y = position_on_y
        self.width = width
        self.height = height
        self.path = [position_on_x, end]
        self.walk_count = 0
        self.speed = 3
        self.hitbox = (self.position_on_x + 17, self.position_on_y + 2, 31, 57)  # NEW
        self.health = 10  # NEW
        self.visible = True  # NEW

    def draw(self, screen):
        self.move()
        if self.visible:  # NEW
            if self.walk_count + 1 >= 33:
                self.walk_count = 0

            if self.speed > 0:
                screen.blit(self.walk_right[self.walk_count // 3], (self.position_on_x, self.position_on_y))
                self.walk_count += 1
            else:
                screen.blit(self.walk_left[self.walk_count // 3], (self.position_on_x, self.position_on_y))
                self.walk_count += 1
            pg.draw.rect(screen, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))  # NEW
            pg.draw.rect(screen, (0, 128, 0),
                         (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))  # NEW
            self.hitbox = (self.position_on_x + 17, self.position_on_y + 2, 31, 57)
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.speed > 0:
            if self.position_on_x < self.path[1] + self.speed:
                self.position_on_x += self.speed
            else:
                self.speed = self.speed * -1
                self.position_on_y += self.speed
                self.walk_count = 0
        else:
            if self.position_on_x > self.path[0] - self.speed:
                self.position_on_x += self.speed
            else:
                self.speed = self.speed * -1
                self.position_on_x += self.speed
                self.walk_count = 0

    def hit(self):  # ALL NEW
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')


class Config:
    screen_height = 500
    screen_width = 500
    black = (0, 0, 0)
    red = (255, 0, 0)
    clock = pg.time.Clock()
    bg = pg.image.load(path.join("bg.jpg"))
    score = 0


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


def print_font(screen):
    comicsans_font = pg.font.SysFont("comicsans", 30, True)
    text = comicsans_font.render("Score: " + str(Config.score), 1,
                                 Config.black)  # Arguments are: text, anti-aliasing, color
    screen.blit(text, (390, 10))


def draw_game(screen, bullets, goblin):
    screen.blit(Config.bg, (0, 0))
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    print_font(screen)
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
    shoot_loop = 0
    goblin = Enemy(100, 410, 64, 64, 300)
    bullets = []
    run = True
    screen = pg.display.set_mode((Config.screen_width, Config.screen_height))
    while run:

        Config.clock.tick(27)
        if shoot_loop > 0:
            shoot_loop += 1
        if shoot_loop > 3:
            shoot_loop = 0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        for bullet in bullets:
            if bullet.position_on_y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] \
                    and bullet.position_on_y + bullet.radius > goblin.hitbox[1]:

                if bullet.position_on_x + bullet.radius > goblin.hitbox[0] and bullet.position_on_x - bullet.radius < \
                        goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    Config.score += 1  # NEW
                    bullets.pop(bullets.index(bullet))

            if 500 > bullet.position_on_x > 0:
                bullet.position_on_x += bullet.speed
            else:
                bullets.pop(bullets.index(bullet))

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and shoot_loop == 0:
            if Player.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 3:
                bullets.append(
                    Projectile(round(Player.position_on_x + Player.width // 2),
                               round(Player.position_on_y + Player.height // 2), 6, Config.black,
                               facing))

            shoot_loop = 1
        jump(keys)
        check_move(keys)
        draw_game(screen, bullets, goblin)
    pg.quit()


run_game()
