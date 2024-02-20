import pygame
from classes import *

pygame.init()


#Inicializate screen
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
FPS = 60 


#Incializate obejcts
shooter = Shooter()
celestial_body_1 = Celestial_body(np.array([300, 100]),1000, (40,40))
celestial_body_2 = Celestial_body(np.array([100, 100]),800, (50,50))
target = Target(np.array([200, 200]), (30, 30))

#Game colors
BLACK = (0, 0, 0)

#Game variables
shoot = False
bullet_list = []
control_velocity = 100
jogo = True




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
            v = v/control_velocity

            

            bullet = Bullet(shooter.s0, v*2)

            bullet_list.append(bullet)
            

        if event.type == pygame.QUIT:
            running = False


    #UPDATED OBEJCTS

    #Update bullets according to the celestial body
    for bullet in bullet_list:
        bullet.update(celestial_body_1, celestial_body_2)


    #Delete bullets that go off screen
    for bullet in bullet_list:
        if not pygame.Rect(0, 0, 400, 400).colliderect(bullet.rect):
            bullet_list.remove(bullet)
        elif bullet.collision(celestial_body_1):
            bullet_list.remove(bullet)
        elif bullet.collision(celestial_body_2):
            bullet_list.remove(bullet)
        elif bullet.collision(target):
            bullet_list.remove(bullet)
            bullet.points += 1

            
    
    
    #DRAW OBJECTS

    #Draw backgorund
    screen.fill(BLACK)

    #Draw shooter
    shooter.draw(screen)

    #Draw celestial body
    celestial_body_1.draw(screen)
    celestial_body_2.draw(screen)

    #Draw target
    target.draw(screen)

    #Draw bullets
    for bullet in bullet_list:
        bullet.draw(screen)




    #Update screen
    pygame.display.update()




pygame.quit()

    
