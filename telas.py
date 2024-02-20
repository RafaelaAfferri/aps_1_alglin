import pygame
import numpy as np
from classes import *
from constante import *






class Fase_1():
    def __init__(self):
        self.shooter = Shooter()
        self.celestial_body_2 = Celestial_body((300, 300), 100, (50, 50))
        self.target = Target(np.array([200, 200]), (30, 30))
        self.bullet_list = []
        self.shoot = False
        self.control_velocity = 50
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 12)
        

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
                y = pygame.mouse.get_pos()
                v = y - self.shooter.s0
                v = v/self.control_velocity

            

                bullet = Bullet(self.shooter.s0, v)

                self.bullet_list.append(bullet)
                print(self.shooter.points)
            
            if self.shooter.points == 5:
                return Fase_2()

            if event.type == pygame.QUIT:
                return -1

        #UPDATED OBEJCTS

        #Update bullets according to the celestial body
        for bullet in self.bullet_list:
            bullet.update([ self.celestial_body_2])


        #Delete bullets that go off screen
        for bullet in self.bullet_list:
            if not pygame.Rect(0, 0, 400, 400).colliderect(bullet.rect):
                self.bullet_list.remove(bullet)
            
            elif bullet.collision(self.celestial_body_2):
                self.bullet_list.remove(bullet)
            elif bullet.collision(self.target):
                self.bullet_list.remove(bullet)
                self.shooter.points += 1

        return self
    def draw(self, screen):
        #DRAW OBJECTS

        #Draw backgorund
        screen.fill(BLACK)

        #Draw shooter
        self.shooter.draw(screen)

        #Draw celestial body
        self.celestial_body_2.draw(screen)

        #Draw target
        self.target.draw(screen)

        text_surface = self.font.render(f"Pontos Acumulados", True, (255,255,255))
        screen.blit(text_surface, (10, 10))
        for i in range(self.shooter.points):
            point_surface = pygame.Surface((5, 5))
            point_surface.fill((255, 0, 0))
            screen.blit(point_surface, (10 + (i*10), 20))

        #Draw bullets
        for bullet in self.bullet_list:
            bullet.draw(screen)


        #Update screen
        pygame.display.update()


class Fase_2():
    def __init__(self):
        self.shooter = Shooter()
        self.celestial_body_1 = Celestial_body((100, 100), 1000, (50, 50))
        self.celestial_body_2 = Celestial_body((300, 300), 800, (50, 50))
        self.target = Target(np.array([200, 200]), (30, 30))
        self.bullet_list = []
        self.shoot = False
        self.control_velocity = 50
        self.clock = pygame.time.Clock()
        

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
                y = pygame.mouse.get_pos()
                v = y - self.shooter.s0
                v = v/self.control_velocity

            

                bullet = Bullet(self.shooter.s0, v)

                self.bullet_list.append(bullet)
                print(self.shooter.points)

            if event.type == pygame.QUIT:
                return -1

        #UPDATED OBEJCTS

        #Update bullets according to the celestial body
        for bullet in self.bullet_list:
            bullet.update([self.celestial_body_1, self.celestial_body_2])


        #Delete bullets that go off screen
        for bullet in self.bullet_list:
            if not pygame.Rect(0, 0, 400, 400).colliderect(bullet.rect):
                self.bullet_list.remove(bullet)
            elif bullet.collision(self.celestial_body_1):
                self.bullet_list.remove(bullet)
            elif bullet.collision(self.celestial_body_2):
                self.bullet_list.remove(bullet)
            elif bullet.collision(self.target):
                self.bullet_list.remove(bullet)
                self.shooter.points += 1

        return self
    def draw(self, screen):
        #DRAW OBJECTS

        #Draw backgorund
        screen.fill(BLACK)

        #Draw shooter
        self.shooter.draw(screen)

        #Draw celestial body
        self.celestial_body_1.draw(screen)
        self.celestial_body_2.draw(screen)

        #Draw target
        self.target.draw(screen)

        #Draw bullets
        for bullet in self.bullet_list:
            bullet.draw(screen)


        #Update screen
        pygame.display.update()

class Jogo():
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption('Jogo da Rafa')
        self.screen_height=400
        self.screen_width=400
        self.current_screen=Fase_1()

        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.clock = pygame.time.Clock()
        

        
    
    def game_loop(self):
        self.clock.tick(FPS)
        running=True 
        while running:
            self.current_screen= self.current_screen.run()
            
            if self.current_screen==-1:
                running=False
            else:
                self.current_screen.draw(self.screen)

        pygame.quit()


if __name__ == '__main__':
    Jogo().game_loop()  
