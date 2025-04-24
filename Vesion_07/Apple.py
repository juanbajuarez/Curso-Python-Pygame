import pygame
from pygame.sprite import Sprite
from Configurations import  Configurations
from random import randint

class Apple(Sprite):
    """
    Clase para formar la manzana
    """

    def __init__(self):
        super().__init__()

        self.image=pygame.Surface((Configurations.get_apple_block_size(),Configurations.get_apple_block_size()))
        self.image.fill(Configurations.get_apple_head_color())

        self.rect=self.image.get_rect()

    def blit (self,screen:pygame.surface.Surface)-> None:
        """
        Se utiliza para dibujar la manzana.
        :param screen
        """
        screen.blit(self.image,self.rect)

    def random_position(self)->None:
        """
        Se utiliza para inicializar la ubicación de la manzana
        """
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        apple_block_size = Configurations.get_apple_block_size()

        # posicion aleatora de la cabeza de la snake
        self.rect.x = apple_block_size * randint(0, (screen_width // apple_block_size) - 1)
        self.rect.y = apple_block_size * randint(0, (screen_height // apple_block_size) - 1)


