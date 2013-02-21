import os, pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

import math
import random

class Settings:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.resourcepath = 'resources'

settings = Settings()

pygame.init()
screen = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption('My Game')
#pygame.mouse.set_visible(0)

sprite_group = pygame.sprite.RenderPlain()

def load_image(name, colorkey=-1, perpixelalpha=False):
    fullname = os.path.join(settings.resourcepath, name)
    
    try:
        image = pygame.image.load(fullname)
        if perpixelalpha:
            image = image.convert_alpha()
        else:
            image = image.convert()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(settings.resourcepath, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound

class MySprite(pygame.sprite.Sprite):
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        pygame.sprite.Sprite.__init__(self)
    
    def update(self):
        self.image = None
        self.rect = None

def main():
    
    bg = pygame.Surface(screen.get_size()).convert()
    #bg.blit(background_image, screen.get_rect(), background_image.get_rect())
        
    clock = pygame.time.Clock()
    
    # set up the rock spawner
    pygame.time.set_timer(USEREVENT + 1, 1000)

    while 1:
        # remove if doing variable time
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                pass
            elif event.type == KEYUP:
                pass
            elif event.type == MOUSEBUTTONDOWN:
                pass
        
        screen.blit(bg, (0, 0))
        
        sprite_group.update()
        sprite_group.draw(screen)
        
        pygame.display.flip()

if __name__ == '__main__': main()

