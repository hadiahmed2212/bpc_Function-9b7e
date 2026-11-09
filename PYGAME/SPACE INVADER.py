import math
import pygame
import random
width=800
height=500
screen_size=500,500
player_sty=0
player_stx=0
enemy_sty=380
enemy_stmin=50
enemy_stmax=150
enemy_spdx=4
enemy_spdy=40
bullet_spdy=10
colliding_dist=27

pygame.init()
screen = pygame.display.set_mode((width,height))
bg= pygame.image.load(r'C:\Users\Administrator\Downloads\bpc_Function-9b7e\PYGAME\bg.png')
pygame.display.set_caption("space invader")
icon=pygame.image.load(r'C:\Users\Administrator\Downloads\bpc_Function-9b7e\PYGAME\icon.jpeg')
pygame.display.set_icon(icon)
playerimg=pygame.image.load(r'C:\Users\Administrator\Downloads\bpc_Function-9b7e\PYGAME\rocket.jpg')

player_x=player_stx
player_y=player_sty
player_x_change=0

enemy_img=[]
enemyx=[]
enemy_y=[]
enemyx_change=[]
enemy_y_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load(r'C:\Users\Administrator\Downloads\bpc_Function-9b7e\PYGAME\rocket.jpg'))
    enemyx.append(random.randint(0, width-64))
    enemy_y.append(random.randint(enemy_stmin,enemy_stmax))
    enemyx_change.append(enemy_spdx)
    enemy_y_change.append(enemy_spdy)
    #part 2 will be completed