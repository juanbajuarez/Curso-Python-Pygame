import pygame
from Configurations import Configurations

class Background:

    """
    Clase que contiene el fondo de pantalla
    """
    def __init__(self):
        """

        """
        background_image_path=Configurations.get_background_image_path()
        self.image=pygame.image.load(background_image_path)

        #Se escala la imagen al tamaño de la pantalla
        screen_size=Configurations.get_screen_size()
        self.image=pygame.transform.scale(self.image,screen_size)

        self.rect = self.image.get_rect()

    def blit (self,screen:pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla
        """
        screen.blit(self.image,self.rect)

class Audio:
    def __init__(self):
        #Se carga la música del juego
        pygame.mixer.music.load("../media/music.mp3")

        self._start_sound=pygame.mixer.Sound("../media/start_sound.wav")
        self._eats_apple_sound=pygame.mixer.Sound("../eats_apple_sound.wav")
        self._game_over_sound=pygame.mixer.Sound("../game_over_sound.wav")

    @classmethod
    def play_music(cls,volumen)->None:
        pygame.mixer.music.play(loop=-1)        #El -1 indica que se reproduce
        pygame.mixer.music.set_volume(volumen)  #en el bucle

