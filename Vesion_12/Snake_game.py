# Autor: Juan Bautista Juárez
# Fecha: Marzo de 2025
# Descripción: Primera version pygame
# versión 1.2
# Se agregó la clase configuración en el módulo configurations.py que
# va a iniciar

#Importar modulos para el videojuego.

import pygame
from Configurations import Configurations
from Game_funtionalities import game_events, screen_refresh, snake_movement,check_collitions,game_over_screen
from Snake import SnakeBlock
from pygame.sprite import Group
from Apple import Apple
from  Media import Background,Audio,Scoreboard


def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se inicializa el módulo de pygame y se realizan las configuraciones iniciales.
    pygame.init()
    screen = pygame.display.set_mode(Configurations.get_screen_size())  # Resolución de la pantalla (ancho, alto).
    pygame.display.set_caption(Configurations.get_game_title())         # Se configura el título de la ventana.
    clock = pygame.time.Clock()                     #  Se usa para controlar la velocidad de fotogramas (FPS).

    # Se crea el bloque inicial de la serpiente (cabeza) y se inicializa en un lugar aleatorio de la pantalla.
    snake_head = SnakeBlock(is_head = True)
    snake_head.snake_head_init()

    # Se crea un grupo que va a almacenar el cuerpo de la serpiente, por lo que se agrega la cabeza de la serpiente.
    snake_body = Group()
    snake_body.add(snake_head)

    #Se crea el bloque inicial de la manzana
    apple=Apple()
    apple.random_position(snake_body)

    #Se crea un bloque inicial de la manzana
    apples=Group()
    apples.add(apple)

    background=Background()

    # Se crea el objeto con el sonido del juego y se reproduce la música y el sonido inicial del juego.
    audio = Audio()
    audio.play_music(volume=Configurations.get_music_volume())
    audio.play_star_sound()

    #Se crea el objeto con el score del juego

    scoreboard=Scoreboard()

    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:
        # Función que administra los eventos del juego.
        game_over = game_events()

        #Condicion de que se cerró la ventana.
        if game_over:
            break

        # Función que administra el movimiento de la serpiente.
        snake_movement(snake_body)

        #Se revisan las colisiones en el juego
        game_over=check_collitions(screen,snake_body,apples,audio)

        #si se ah perdido
        if game_over:
            game_over_screen(audio)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, snake_body,apples,background,scoreboard)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    run_game()