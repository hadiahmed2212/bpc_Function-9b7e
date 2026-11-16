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
icon=pygame.image.load(r'C:\Users\Administrator\Downloads\bpc_Function-9b7e\PYGAME\logo.jpg')
pygame.display.set_icon(icon)
playerimg=pygame.image.load(r'C:\Users\Administrator\Downloads\bpc_Function-9b7e\PYGAME\307f0e19-4bb6-418f-aa92-8dc7cefd6276.png')
playerimg=pygame.transform.scale(playerimg,(80,80))
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
    enemy_img.append(pygame.image.load(r'C:\Users\Administrator\Downloads\bpc_Function-9b7e\PYGAME\31905197-8ad4-4af0-8c03-655546e4d5b0.png'))
    # enemy_img = pygame.transform.scale(enemy_img, (20, 20))
    enemyx.append(random.randint(0, width-20))
    enemy_y.append(random.randint(enemy_stmin,enemy_stmax))
    enemyx_change.append(enemy_spdx)
    enemy_y_change.append(enemy_spdy)
    #part 2
bulletimg=pygame.image.load(r'C:\Users\Administrator\Downloads\bpc_Function-9b7e\PYGAME\6328c3e4-887a-453c-a703-87ec9ffb0c8f.png')
bulletimg=pygame.transform.scale(bulletimg,(80,80))
bulletx=0
bullety=player_sty
bulletx_change=0
bullety_change=bullet_spdy
bullet_state='ready'

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
over_font=pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score=font.render('score:'+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text=over_font.render('GAME OVER',True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletimg,(x+16,y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    dist=math.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
    return dist <colliding_dist
running=True
while running:
    screen.fill((0, 0, 0))

    screen.blit(bg,(0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                player_x_change = -5

            if event.key == pygame.K_RIGHT:

                player_x_change = 5

            if event.key == pygame.K_SPACE and bullet_state == "ready":

                bulletx = player_x

                fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            player_x_change = 0
    player_x+=player_x_change
    player_x=max(0, min(player_x, width - 64))
    for i in range(num_of_enemies):
        if enemy_y[i]>340:
            for j in range(num_of_enemies):
                enemy_y[j]=2000
            game_over_text()
            break
        enemyx[i]+=enemyx_change[i]
        if enemyx [i] <=0 or enemyx [i] >= width-64:
            enemyx_change[i]*=-1
            enemy_y[i]+=enemy_y_change[i]
        if iscollision(enemyx[i], enemy_y[i], bulletx, bullety):

            bullety= player_sty

            bullet_state = "ready"

            score_value += 1

            enemyx[i] = random.randint(0, width - 64)

            enemy_y[i] = random.randint(enemy_stmin,enemy_stmax)
        enemy(enemyx[i], enemy_y[i], i)

    if bullety <= 0:    
        bullety = player_sty
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletx, bullety)

        bulletY -= bullety_change
    player(player_x, player_y)
    show_score(textx, texty)
    pygame.display.update()            