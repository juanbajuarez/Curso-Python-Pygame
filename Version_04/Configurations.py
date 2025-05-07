# Autor: Juan Bautista Juárez
# Fecha: Marzo de
# Descripción: juegos

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)            # Alto por ancho
    _game_title = "Snake game en Pygame"  #Título del juego
    _background = (255, 100, 50)          #Fondo de la pantalla en RGB
    _fps = 12  # Fps de juego

    #Configuraciones de la serpiente
    _snake_block_size=80 #tamaño de bloque de serpiente
    _snake_head_color=(40,20,255) #color de la cabeza de la serpiente
    _snake_body_color=(10,255,30)

    #Métodos de acceso

    @classmethod
    def get_screen_size(cls)->tuple[int,int]:
        """
        Getter para _screen_size
        :return:
        """
        return cls._screen_size
    @classmethod
    def get_game_title(cls)->str:
        """
        Getter para _game_title
        :return:
        """
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int,int,int]:
        """
        Getter para _background
        :return:
        """
        return cls._background

    @classmethod
    def get_fps(cls)->int:
        """

        """
        return cls._fps       #Fps de juego

    @classmethod
    def get_snake_block_size(cls)->int:

        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls)-> tuple[int,int,int]:

        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        return cls._snake_head_color

