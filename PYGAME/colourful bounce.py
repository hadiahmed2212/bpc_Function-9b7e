import pygame
import random
pygame.init()

sprite_clr_change_eve= pygame.USEREVENT +1
backdrop_clr_change_eve= pygame.USEREVENT +2

blue= pygame.Color('blue')
lightblue= pygame.Color('lightblue')
darkblue=pygame.Color('darkblue')

yellow= pygame.Color('yellow')
orange=pygame.Color('orange')
red=pygame.Color('red')
green=pygame.Color('green')

class sprite(pygame.sprite.Sprite):

    def __init__(self, color,height,width):
        super().__init__()
        self.img= pygame.Surface([width,height])
        self.img.fill(color)
        self.rect=self.image.get_rect()
        self.velocity= [random.choice([-1, 1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        if self.rect.left <= 0 or self.rect.right >= 400:
            self.velocity[0]= -self.velocity[1]
            boundary_hit=True
#will do remains next class
