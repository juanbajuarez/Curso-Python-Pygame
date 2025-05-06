# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Primera version pygame dfdfdughuuh
# versión 02

import pygame


from Configurations import Configurations
def game_event()->bool:
    """
    Funcion que administra los eventos del juego
    :return: la bandera del fin deñ juegoo
    """
    game_over=False
    # Se verifican los eventos(teclado y ratón) del juego
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True
    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface)->None:
    """
    Funcion que administra los elementos visuales del juego
    """
    #Fondo de la pantalla en rgb
    screen.fill(Configurations.get_background())

    # Se actualiza la pantalla
    pygame.display.flip()