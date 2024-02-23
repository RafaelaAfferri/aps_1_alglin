import pygame
import numpy as np
from classes import *
from constante import *






class Fase_1():
    def __init__(self):
        self.shooter = Shooter()
        self.celestial_body_2 = Celestial_body(CELESTIAL_BODY_2_POSITION_FIRST_POSITION, CELESTIAL_BODY_2_CONSTANT, CELESTIAL_BODY_2_SIZE, PLANET_2)
        self.target = Target(np.array(TARGET_POSITION_1), TARGET_SIZE)
        self.bullet_list = []
        self.shoot = False
        self.control_velocity = CONTROL_VELOCITY
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        self.background = pygame.image.load(BACKGROUND)
        self.plataform = pygame.image.load(FLOOR)
        self.plataform = pygame.transform.scale(self.plataform,PLATAFORM_SIZE)
        

    def run(self):

        self.clock.tick(FPS)

        #EVENTS
        for event in pygame.event.get():

            #Shoot the bullets
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.shoot = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.shoot = False
            if self.shoot:

                #Get the mouse position
                y = pygame.mouse.get_pos()
                v = y - self.shooter.s0
                v = v/self.control_velocity

                #Create the bullet
                bullet = Bullet(self.shooter.s0, v)

                self.bullet_list.append(bullet)
            
            #Calculate the points
            if self.shooter.points >= 5:
                return Fase_2()

            if event.type == pygame.QUIT:
                return -1

        #UPDATED OBEJCTS

        #Update bullets according to the celestial body
        for bullet in self.bullet_list:
            bullet.update([ self.celestial_body_2])

        for bullet in self.bullet_list:

            #Delete bullets that go off screen
            if not pygame.Rect(0, 0, 400, 400).colliderect(bullet.rect):
                self.bullet_list.remove(bullet)

            #Delete bullets that collide with the celestial body
            elif bullet.collision(self.celestial_body_2):
                self.bullet_list.remove(bullet)
            elif bullet.collision(self.target):
                self.bullet_list.remove(bullet)
                self.shooter.points += 1

        return self
    def draw(self, screen):
        #DRAW OBJECTS

        #Draw backgorund
        # screen.fill(BLACK)
        screen.blit(self.background, (0, 0))

        #Draw shooter
        self.shooter.draw(screen)

        #Draw celestial body
        self.celestial_body_2.draw(screen)

        #Draw target
        self.target.draw(screen)

        #Draw plataform
        screen.blit(self.plataform, (25, 350))
        
        #Draw points
        text_surface = self.font.render(f"Pontos", True, (255,255,255))
        screen.blit(text_surface, (10, 10))
        for i in range(self.shooter.points):
            image_pontos = pygame.image.load(BULLET)
            image_pontos = pygame.transform.scale(image_pontos, (10, 10))
            screen.blit(image_pontos, (10 + (i*15), 30))

        #Draw bullets
        for bullet in self.bullet_list:
            bullet.draw(screen)

        

        #Update screen
        pygame.display.update()


class Fase_2():
    def __init__(self):
        self.shooter = Shooter()
        self.celestial_body_1 = Celestial_body(CELESTIAL_BODY_1_POSITION, CELESTIAL_BODY_1_CONSTANT, CELESTIAL_BODY_1_SIZE, PLANET_1)
        self.celestial_body_2 = Celestial_body(CELESTIAL_BODY_2_POSITION_SECOND_POSITION, CELESTIAL_BODY_2_CONSTANT, CELESTIAL_BODY_2_SIZE, PLANET_2)
        self.target = Target(np.array(TARGET_POSITION_1), TARGET_SIZE)
        self.bullet_list = []
        self.shoot = False
        self.control_velocity = CONTROL_VELOCITY
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 15)
        self.background = pygame.image.load(BACKGROUND)
        self.plataform = pygame.image.load(FLOOR)
        self.plataform = pygame.transform.scale(self.plataform, PLATAFORM_SIZE)

    def run(self):

        self.clock.tick(FPS)

        #EVENTS
        for event in pygame.event.get():
            #Shoot the bullets
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.shoot = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.shoot = False
            if self.shoot:
                #Get the mouse position
                y = pygame.mouse.get_pos()
                v = y - self.shooter.s0
                v = v/self.control_velocity


                bullet = Bullet(self.shooter.s0, v)

                self.bullet_list.append(bullet)
            if self.shooter.points >= 5:
                return Tela_final()

            if event.type == pygame.QUIT:
                return -1

        #UPDATED OBEJCTS

        #Update bullets according to the celestial body
        for bullet in self.bullet_list:
            bullet.update([self.celestial_body_1, self.celestial_body_2])


        for bullet in self.bullet_list:
            #Delete bullets that go off screen
            if not pygame.Rect(0, 0, 400, 400).colliderect(bullet.rect):
                self.bullet_list.remove(bullet)
            #Delete bullets that collide with the celestial body
            elif bullet.collision(self.celestial_body_1):
                self.bullet_list.remove(bullet)
            elif bullet.collision(self.celestial_body_2):
                self.bullet_list.remove(bullet)
            #Calculate the points
            elif bullet.collision(self.target):
                self.bullet_list.remove(bullet)
                self.shooter.points += 1

        return self
    def draw(self, screen):
        #DRAW OBJECTS

        #Draw backgorund
        screen.fill(BLACK)
        screen.blit(self.background, (0, 0))

        #Draw shooter
        self.shooter.draw(screen)

        #Draw celestial body
        self.celestial_body_1.draw(screen)
        self.celestial_body_2.draw(screen)

        #Draw target
        self.target.draw(screen)

        #Draw plataform
        screen.blit(self.plataform, (25, 350))
        
        #Draw bullets
        for bullet in self.bullet_list:
            bullet.draw(screen)

        #Draw points
        text_surface = self.font.render(f"Pontos", True, (255,255,255))
        screen.blit(text_surface, (10, 10))
        for i in range(self.shooter.points):
            image_pontos = pygame.image.load(BULLET)
            image_pontos = pygame.transform.scale(image_pontos, (10, 10))
            screen.blit(image_pontos, (10 + (i*15), 30))



        #Update screen
        pygame.display.update()


class Tela_final():
    def __init__(self):
        self.background = pygame.image.load(FINAL)
        self.clock = pygame.time.Clock()

        #Create the button
        self.play_again = pygame.Rect(100, 220, 200, 25)

    def run(self):
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            #Check if the button was clicked
            y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_again.collidepoint(y):
                    return Fase_1()

        return self


    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.update()

class Tela_Inicial():
    def __init__(self):
        self.background = pygame.image.load(INICIAL)
        self.clock = pygame.time.Clock()

        #Create the button
        self.play_again = pygame.Rect(145, 189, 110, 25)

    def run(self):
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            #Check if the button was clicked
            y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_again.collidepoint(y):
                    return Fase_1()

        return self


    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.update()

class Jogo():
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption('Alien Hunt')
        self.current_screen=Tela_Inicial()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        

        
    
    def game_loop(self):
        self.clock.tick(FPS)
        running=True 
        while running:

            #Get the current screen
            self.current_screen= self.current_screen.run()
            
            #Mecanism to change the screen
            if self.current_screen==-1:
                running=False
            else:
                self.current_screen.draw(self.screen)

        pygame.quit()


if __name__ == '__main__':
    Jogo().game_loop()  
