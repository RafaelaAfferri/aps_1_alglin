import numpy as np
import pygame
from constante import *

class Shooter(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.s0 = np.array(SHOOTER_POSITION)
        self.image = pygame.image.load(SHOOTER)
        self.image = pygame.transform.scale(self.image, SHOOTER_SIZE)
        self.rect = pygame.Rect(self.s0[0], self.s0[1], 50, 50)
        self.points = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
        


class Bullet(pygame.sprite.Sprite):
    def __init__(self, s0, v0):
        pygame.sprite.Sprite.__init__(self)
        self.v0 = np.array(v0, dtype=float)
        self.s0 = np.array(s0 + 55, dtype=float)
        self.image = pygame.image.load(BULLET)
        self.image = pygame.transform.scale(self.image, BULLET_SIZE)
        self.rect = pygame.Rect(self.s0[0], self.s0[1], 10, 10)
        


    def update(self, list_celestials):

        

        #Calculate gravitational force
        for celestial_body in list_celestials:
            distance = np.linalg.norm(celestial_body.s0 - self.s0)
            gravtional_direction = (celestial_body.s0 - self.s0) / distance
            gravtional_force = (celestial_body.constant / distance**2) * gravtional_direction
            self.v0 = self.v0 + gravtional_force
            
                                                                                                                
        #Update velocity and position
        self.s0 += self.v0
        self.rect.center = self.s0
        


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.display.update()

    def collision(self, body):
        return self.rect.colliderect(body.rect)
        

        


class Celestial_body(pygame.sprite.Sprite):
    def __init__(self, s0, constant, size, texture):

        pygame.sprite.Sprite.__init__(self)

        self.s0 = s0
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = pygame.Rect(self.s0[0], self.s0[1],size[0], size[1])
        self.constant = constant

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Target(pygame.sprite.Sprite):
    def __init__(self, s0, size):
        pygame.sprite.Sprite.__init__(self)

        self.s0 = s0
        self.image = pygame.image.load(TARGET)
        self.image = pygame.transform.scale(self.image, TARGET_SIZE)
        self.rect = pygame.Rect(self.s0[0], self.s0[1], size[0], size[1])

    def draw(self, screen):
        screen.blit(self.image, self.rect)





