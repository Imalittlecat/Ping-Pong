#Игра Ping Pong
import pygame
from pygame.locals import *
#from random import randint
#from time import time as timer

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, size_x, size_y):
        pygame.sprite.Sprite.__init__(self)
        #super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed   
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y, points):
        super().__init__(player_image, player_x, player_y, player_speed, size_x, size_y)
        self.points = points
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < height -80:
            self.rect.y += self.speed
            if self.rect.y > 550:
                self.rect.y = 550
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < height -80:
            self.rect.y += self.speed
            if self.rect.y > 550:
                self.rect.y = 550


img_back = 'galaxy.jpg'
img_asteroid = 'asteroid.png'
img_ball1 = 'tenis_ball.png'
img_racket = 'racket.png'


pygame.font.init()
font1 = pygame.font.Font(None, 80)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play()


width = 1200
height = 700
background = pygame.transform.scale(pygame.image.load(img_back), (width, height))
window = pygame.display.set_mode((width, height))



game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

racket1 = Player(img_racket, 30, 200, 4, 50, 150, 0)
racket2 = Player(img_racket, 1120, 200, 4, 50, 150, 0)
ball = GameSprite(img_asteroid, 200, 200, 4, 50, 50)

speed_x = 5
speed_y = 5

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if pygame.sprite.collide_rect(racket1, ball) or pygame.sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            racket1.point += 1
            if racket1.point > 5:
                finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
        
        racket1.reset()
        racket2.reset()
        ball.reset()

    pygame.display.update()
    clock.tick(FPS)