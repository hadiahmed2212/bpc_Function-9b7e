import pygame
pygame.init()
screen_width, screen_height=500,500
display_surface= pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption('adding images in pygame')
backdropimg=pygame.transform.scale(pygame.image.load('backdrop.png'(),(screen_width,screen_height)))

#will finish in doubt class :D