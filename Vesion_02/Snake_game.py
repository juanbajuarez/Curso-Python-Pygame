# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Primera version pygame confi
# versión 02
from turtle import Screen
from typing import Tuple

#Importar modulos para el video juego

import pygame
from  Configurations import Configurations
def run_game()->None:
    """
    Función principaljkjkjk
    :return:
    """
    #Inicia modulo pygame
    pygame.init()

    #Se inicializa la pantalla

    screen=pygame.display.set_mode(Configurations.get_screen_size())

    pygame.display.set_caption(Configurations.get_game_title())

    #Ciclo principal del juego

    game_over=False

    while not game_over:
        # Se verifican los eventos(teclado y ratón) del juego
        for event in pygame.event.get():
            #Un clic en cerrar el juego
            if event.type==pygame.QUIT:
                game_over=True
        #Se dibuja los elementos gráficos em la pantalla
        screen.fill(Configurations.get_background())

        #Se actualiza la pantalla
        pygame.display.flip()
    #Se cierran los recursos del juego
    pygame.quit()


if __name__ == '__main__':
    run_game()