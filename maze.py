

from pygame import *

'''Необходимые классы'''


# класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (40, 40))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_const = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LSHIFT]:
            self.speed = self.speed_const // 2
        else:
            self.speed = self.speed_const

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.image = transform.scale(image.load('s1_mirror.gif'), (40, 40))
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
            self.image = transform.scale(image.load('s1.gif'), (40, 40))
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            print(self.speed)
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed






# класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
    def update(self, left_order, right_order):
        if self.rect.x <= left_order:
            self.side = "right"
        if self.rect.x >= right_order:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


# класс для спрайтов-препятствий
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

        # draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


# Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("back.jpg"), (win_width, win_height))

# Персонажи игры:
player = Player('s1.gif', 5, win_height - 80, 4)
monster = Enemy('s1.png', win_width - 80, 280, 2)

final = GameSprite('s3.png', win_width - 120, win_height - 80, 0)

w1 = Wall(154, 205, 50, 100, 20, 590, 10)

w2 = Wall(154, 205, 50, 100, 480, 350, 10)

w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 190, 100, 10, 380)

w5 = Wall(154, 205, 50, 290, 20, 10, 380)

w6 = Wall(154, 205, 50, 390, 100, 10, 380)

w7 = Wall(154, 205, 50, 390, 300, 90, 10)

w8 = Wall(154, 205, 50, 390, 100, 220, 10)


w9 = Wall(154, 205, 50, 680, 20, 10, 450)

w10 = Wall(154, 205, 50, 500, 180, 180, 10)
game = True
clock = time.Clock()
FPS = 60

finish = False
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

# музыка
# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

# money = mixer.Sound('money.ogg')
# kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update(470, 620)


        player.reset()
        monster.reset()

        final.reset()

        w1.draw_wall()
        w2.draw_wall()

        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()

            # Ситуация "Проигрыш"
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1)\
            or sprite.collide_rect(player, w2)\
            or sprite.collide_rect(player, w3)\
            or sprite.collide_rect(player, w4)\
            or sprite.collide_rect(player, w5)\
            or sprite.collide_rect(player, w6)\
            or sprite.collide_rect(player, w7)\
            or sprite.collide_rect(player, w8)\
            or sprite.collide_rect(player, w9)\
            or sprite.collide_rect(player, w10):
        finish = True
        window.blit(lose, (200, 200))
        # kick.play()

        # Ситуация "Выигрыш"
    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        # money.play()

    display.update()
    clock.tick(FPS)
