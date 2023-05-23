import pygame
from random import randint


class Dino:
    def __init__(self, image_path, height, jump_sound_path, landing_sound_path, crash_sound_path):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey(pygame.Color('white'))
        x = self.image.get_size()[0]
        self.y = height // 2 - self.image.get_size()[1]
        self.rect = self.image.get_rect(topleft=(x,self.y))
        self.speed = 0
        self.max_speed = -10
        self.dy = 0
        self.jump_sound = pygame.mixer.Sound(jump_sound_path)
        self.landind_sound = pygame.mixer.Sound(landing_sound_path)
        self.crash_sound = pygame.mixer.Sound(crash_sound_path)
        self.touch = False
        self.crash = False
        self.timer = 0
        self.down = False
        self.dino_1 = pygame.image.load("images/dino/dino_1.png")
        self.dino_2 = pygame.image.load("images/dino/dino_2.png")
        self.dino_3 = pygame.image.load("images/dino/dino_3.png")
        self.dino_4 = pygame.image.load("images/dino/dino_4.png")
        self.dino_1.set_colorkey(pygame.Color('white'))
        self.dino_2.set_colorkey(pygame.Color('white'))
        self.dino_3.set_colorkey(pygame.Color('white'))
        self.dino_4.set_colorkey(pygame.Color('white'))

    def draw(self, sc):
        if self.timer < 5 or self.dy != 0:
            if self.down:
                sc.blit(self.dino_3, self.rect)
            else:
                sc.blit(self.dino_1, self.rect)
        elif self.timer < 10:
            if self.down:
                sc.blit(self.dino_4, self.rect)
            else:
                sc.blit(self.dino_2, self.rect)
        else:
            if self.down:
                sc.blit(self.dino_3, self.rect)
            else:
                sc.blit(self.dino_1, self.rect)
            self.timer = 0
        self.timer += 1
    def sat_down(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and not self.dy:
            self.down = True
            self.rect = self.dino_3.get_rect(bottomleft=self.rect.bottomleft)
        else:
            self.rect = self.dino_1.get_rect(bottomleft=self.rect.bottomleft)
            self.down = False
    def check_jump_possiblity(self):
        key = pygame.key.get_pressed()
        if (key[pygame.K_SPACE] or key[pygame.K_UP]) and not self.dy:
            self.jump_sound.play()
            return True
        return False
    def jump(self):
        if self.check_jump_possiblity():
            self.touch = True
            self.dy = 0.35
            self.speed = self.max_speed
        self.rect.y += self.speed
        self.speed += self.dy
        if self.rect.top >= self.y:
            if self.touch:
                self.landind_sound.play()
                self.touch = False
            self.dy = 0
            self.speed = 0

class Ground:
    def __init__(self, image_path, y, speed):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey(pygame.Color("white"))
        self.rect = self.image.get_rect(topleft=(0,y))
        self.speed = speed
    def draw(self, sc):
        sc.blit(self.image, self.rect)
    def move(self, whith):
        self.rect.x -= self.speed
        if self.rect.right <= whith:
            self.rect.x = 0
class Cloud:
    def __init__ (self, image_path, x, y, speed):
        self.image = pygame. image.load (image_path)
        self.image.set_colorkey (pygame.Color ('white'))
        self.rect = self.image.get_rect(topleft= (x, y))
        self.speed = speed

class Cloud:
    def __init__ (self, image_path, x, y, speed):
        self.image = pygame . image. load (image_path)
        self.image.set_colorkey (pygame.Color ('white'))
        self.rect = self.image. get_rect (topleft= (x, y))
        self.speed = speed
    def draw(self, sc):
        sc.blit(self.image, self.rect)
    def draw_clouds(clouds, sc):
        for cloud in clouds:
            cloud.draw (sc)
    def move(self, width, max_helight):
        if self.rect.right < 0:
            self.rect.left = randint(width, width + 100)
            self.rect.top = randint(0, max_helight)
        else:
            self.rect.x -= self.speed

class Odstacle:
    def __init__(self, speed, image_path, x, dino_bottom, flying):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey(pygame.Color("white"))
        y = dino_bottom - self.image.get_size()[1] + 20
        if flying:
            y -= 70
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.flying = flying

    def draw(self, sc):
        sc.blit(self.image, self.rect)

    def move(self):
        self.rect.x -= self.speed

