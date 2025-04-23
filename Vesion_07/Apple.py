import pygame
from pygame import Sprite
from Configurations import  Configurations

class Apple(Sprite):

    def __init__(self):
        super().__init__()

        self.image=pygame.Surface((10,10))
        self.image.fill((255,50,50))

        self.rect=self.image.get_rect()

    def blit (self,screen:pygame.surface.Surface)-> None:
        """
        Se utiliza para dibujar la manzana
        :param screen
        """
        screen.blit(self.image,self.rect)

