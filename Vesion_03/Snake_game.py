# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Primera version pygame dfdfdughuuh
# versión 02
# Se agregó la clase configuración en el módulo configurations.py que
# va a iniciar

from turtle import Screen
from typing import Tuple

#Importar modulos para el video juego.

import pygame
from  Configurations import Configurations
from Game_funtionalities import game_event,screen_refresh
from Snake import SnakeBlock
def run_game()->None:
    """
    Función principa
    :return:
    """
    #Inicia modulo pygame
    pygame.init()

    #Se configura el reloj del juego
    clock=pygame.time.Clock()

    #Se inicializa la pantalla

    screen=pygame.display.set_mode(Configurations.get_screen_size())
    #se configura el titulo del juego
    pygame.display.set_caption(Configurations.get_game_title())

    #se crea el bloque inicial de la serpiente(cabeza)
    snake_head = SnakeBlock(is_head=True)
    snake_head.snake_head_init()

    #Ciclo principal del juego
    game_over=False

    while not game_over:
        game_over=game_event()
        #Se dibuja los elementos gráficos em la pantalla
        screen_refresh(screen,clock,snake_head)
    #Se cierran los recursos del juego
    pygame.quit()


if __name__ == '__main__':
    run_game()