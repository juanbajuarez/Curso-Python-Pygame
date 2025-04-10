import pygame
from pygame.sprite import Sprite
class SnakeBlock(Sprite):
    def __init__(self):
        """
        Constructor de la clase
        """
        super().__init__()

        color=(0,0,255)
        self.image=pygame.Surface((50,45))
        self.image.fill(color)

        self.rect=self.image.get_rect()

    def blit(self,screen:pygame.surface.Surface)->None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        :param screen: Pantalla donde se dibuja
        """
        screen.blit(self.image,self.rect)


