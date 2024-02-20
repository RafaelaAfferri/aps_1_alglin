import numpy as np
import pygame

class Shooter(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.s0 = np.array([50, 350])
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(self.s0[0], self.s0[1], 50, 50)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
        


class Bullet(pygame.sprite.Sprite):
    def __init__(self, s0, v0, celestial_body_1):
        pygame.sprite.Sprite.__init__(self)



        
        self.v0 = np.array(v0, dtype=float)
        self.s0 = np.array(s0, dtype=float)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 255))
        self.rect = pygame.Rect(self.s0[0], self.s0[1], 10, 10)
        


    def update(self, celestial_body_1):

        #Gravitational force
        distance = np.linalg.norm(celestial_body_1.s0 - self.s0)
        gravtional_direction = (celestial_body_1.s0 - self.s0) / distance
        gravtional_force = (celestial_body_1.constant / distance**2) * gravtional_direction


        #Update velocity and position
        self.v0 = self.v0 + gravtional_force
        self.s0 += self.v0
        self.rect.center = self.s0
        


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.display.update()

    def collision(self, celestial_body_1):
        return self.rect.colliderect(celestial_body_1.rect)
        


class Celestial_body_1(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.s0 = np.array([300, 100])
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 225, 50))
        self.rect = pygame.Rect(self.s0[0], self.s0[1], 50, 50)
        self.constant = 1000

    def draw(self, screen):
        screen.blit(self.image, self.rect)


