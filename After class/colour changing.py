import pygame
def main():
    pygame.init()
    screen=pygame.display.set_mode((500,500))
    pygame.display.set_caption("colour changing sprite.")
    colors = {
    'red': pygame.Color('red'),
    'green': pygame.Color('green'),
    'blue': pygame.Color('blue'),
    'yellow': pygame.Color('yellow'),
    'white': pygame.Color('white')}
    current_colour=colors['white']
    x,y=30,30
    sprite_width,sprite_height=60,60
    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                done=True
        pressed= pygame.key.get_pressed()
        if pressed [pygame.K_LEFT]: x-=3
        if pressed [pygame.K_RIGHT]: x+=3
        if pressed [pygame.K_DOWN]: y+=3
        if pressed [pygame.K_UP]: y-=3
        x=min(max(0,x),500-sprite_width)
        y=min(max(0,y),500-sprite_height)
        if x ==0:
            current_colour=colors['blue']
        elif x ==500-sprite_width:
            current_colour=colors['green']
        elif y ==0:
            current_colour=colors['red']
        elif y ==500-sprite_height:
            current_colour=colors['yellow']
        else:
            current_colour=colors['white']
        screen.fill((0,0,200))
        pygame.draw.rect(screen, current_colour,

        (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__ == "__main__":
    main()