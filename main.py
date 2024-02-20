import pygame
from classes import *

pygame.init()


#Inicializate screen
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
FPS = 60 


#Incializate obejcts
shooter = Shooter()
celestial_body_1 = Celestial_body_1()

#Game colors
BLACK = (0, 0, 0)

#Game variables
shoot = False
bullet_list = []




#GAME LOOP
running = True
while running:

    clock.tick(FPS)

    #EVENTS
    for event in pygame.event.get():

        #Shoot the bullets
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot = True
        elif event.type == pygame.MOUSEBUTTONUP:
            shoot = False
        if shoot:
            y = pygame.mouse.get_pos()
            v = y - shooter.s0
            v = v/np.linalg.norm(v)

            

            bullet = Bullet(shooter.s0, v*2, celestial_body_1)

            bullet_list.append(bullet)
            

        if event.type == pygame.QUIT:
            running = False


    #UPDATED OBEJCTS

    #Update bullets according to the celestial body
    for bullet in bullet_list:
        bullet.update(celestial_body_1)


    #Delete bullets that go off screen
    new_bullets = []
    for bullet in bullet_list:
        if pygame.Rect(0, 0, 400, 400).colliderect(bullet.rect):
            bullet.kill()
            # new_bullets.append(bullet)
        if bullet.collision(celestial_body_1):
            bullet.kill()
            # new_bullets.append(bullet)
    # bullet_list = new_bullets
            
    
    #DRAW OBJECTS

    #Draw backgorund
    screen.fill(BLACK)

    #Draw shooter
    shooter.draw(screen)

    #Draw celestial body
    celestial_body_1.draw(screen)

    #Draw bullets
    for bullet in bullet_list:
        bullet.draw(screen)




    #Update screen
    pygame.display.update()




pygame.quit()

    
