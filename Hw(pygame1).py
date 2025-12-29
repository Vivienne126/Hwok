import pygame

pygame.init()

screen=pygame.display.set_mode((600 , 400))
pygame.display.set_caption("PYGAME")

player=pygame.Rect(50,50,50,50)
box=pygame.Rect(300,200,50,50)

clock=pygame.time.Clock()

speed=5
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.y=player.y-speed

    if keys[pygame.K_DOWN]:
        player.y=player.y+speed
        
    if keys[pygame.K_LEFT]:
        player.x=player.x-speed
        
    if keys[pygame.K_RIGHT]:
        player.x=player.x+speed

    screen.fill((0,0,0))

    pygame.draw.rect(screen , (0,255,0) , player)
    pygame.draw.rect(screen , (255,0,0) , box )

    clock.tick(60)

    pygame.display.update()

pygame.quit()

    

    