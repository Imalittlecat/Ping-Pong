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
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < height -80:
            self.rect.y += self.speed
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < height -80:
            self.rect.y += self.speed


pygame.font.init()
font1 = pygame.font.Font(None, 80)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))


width = 600
height = 500
background = (200, 255, 255)
window = pygame.display.set_mode((width, height))
window.fill(background)


game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket1 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3