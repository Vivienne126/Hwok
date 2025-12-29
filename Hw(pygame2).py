import pygame
import random

pygame.init()

WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Colide Game")

WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)

clock=pygame.time.Clock()
player_size=50
player=pygame.Rect(WIDTH//2 , HEIGHT//2 , player_size , player_size)
player_speed=5

enemy_size=50
enemies=[]
for i in range(7):
    x=random.randint(0,WIDTH-enemy_size)
    y=random.randint(0,HEIGHT-enemy_size)
    enemies.append(pygame.Rect(x , y , enemy_size , enemy_size))

score=0
font=pygame.font.Font(None , 36)
running=True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top>0:
        player.y=player.y-player_speed
    if keys[pygame.K_DOWN] and player.bottom<HEIGHT:
        player.y=player.y+player_speed
    if keys[pygame.K_LEFT] and player.left>0:
        player.x=player.x-player_speed
    if keys[pygame.K_RIGHT] and player.right<WIDTH:
        player.x=player.x+player_speed


    pygame.draw.rect(screen , BLUE , player)
    for enemy in enemies:
        pygame.draw.rect(screen , RED , enemy)

        if player.colliderect(enemy):
            score=score+1
            enemy.x=random.randint(0,WIDTH-enemy_size)
            enemy.y=random.randint(0,HEIGHT-enemy_size)

    score_text=font.render("Score:"+str(score) , True , BLACK)
    screen.blit(score_text , (10,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



#I did not use images but i used rectangles is this ok if not i can try with images