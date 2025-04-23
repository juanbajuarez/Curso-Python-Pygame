# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Primera version pygame
# versión 05
# Se agregó la clase configuración en el módulo configurations.py que
# va a iniciar


#Importar modulos para el videojuego.

import pygame
from  Configurations import Configurations
from Game_funtionalities import game_event,screen_refresh,snake_movement
from Snake import SnakeBlock
from pygame.sprite import  Group

def run_game()->None:
    """
    Función principal
    :return:
    """
    #Inicia modulo pygame
    pygame.init()

    #Se configura el reloj del juego
    clock=pygame.time.Clock()

    #Se inicializa la pantalla

    screen=pygame.display.set_mode(Configurations.get_screen_size())
    #se configura el título del juego
    pygame.display.set_caption(Configurations.get_game_title())

    #se crea el bloque inicial de la serpiente(cabeza)
    snake_head = SnakeBlock(is_head=True)
    snake_head.snake_head_init()

    # Se crea un grupo para almacenar el cuerpo de la serpiente
    snake_body = Group()
    snake_body.add(snake_head)

    #Ciclo principal del juego
    game_over=False

    while not game_over:
        game_over=game_event()

        #funciom movimiento
        snake_movement(snake_body)
        #Se dibuja los elementos gráficos em la pantalla
        screen_refresh(screen,clock,snake_body)
    #Se cierran los recursos del juego
    pygame.quit()


if __name__ == '__main__':
    run_game()