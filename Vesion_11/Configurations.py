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
    _fps = 8# Fps de juego
    _game_over_screen_time=1
    _time_to_refresh=200

    #Configuraciones de la serpiente
    _snake_block_size=80 #tamaño de bloque de serpiente

    #Configuracionde la manzana
    _apple_block_size = _snake_block_size

    #ruta de los archivos multimedia
    _background_image_path = "../Media/background_image.jpg"
    _apple_image_path=["../Media/Apple1.png","../Media/Apple2.png",
                       "../Media/Apple3.png","../Media/Apple4.png"]
    _snake_head_images_path=["../Media/head1.png","../Media/head2.png",
                             "../Media/head3.png","../Media/head4.png",
                             "../Media/head5.png","../Media/head6.png",
                             "../Media/head7.png","../Media/head8.png"]
    _snake_body_images_path=["../Media/body1.png","../Media/body2.png","../Media/body3.png"]

    # Métodos de acceso

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
    def get_fps(cls)->int:
        """

        """
        return cls._fps       #Fps de juego


    @classmethod
    def get_game_over_screen_time(cls)->int:
        """

        """
        return cls._game_over_screen_time       #Fps de juego

    @classmethod
    def get_snake_block_size(cls)->int:

        return cls._snake_block_size

    @classmethod
    def get_apple_block_size(cls) -> int:
        return cls._apple_block_size

    @classmethod
    def get_background_image_path(cls)->str:
        """
        get para obtener el fondo de pantalla
        """
        return cls._background_image_path

    @classmethod
    def get_apple_image_path(cls) -> list:
        """
        get para obtener el fondo de pantalla
        """
        return cls._apple_image_path


    @classmethod
    def get_snake_head_image_path(cls) -> list:
        """
        get para obtener el fondo de pantalla
        """
        return cls._snake_head_images_path

    @classmethod
    def get_snake_body_image_path(cls) -> list:
        """
        get para obtener el fondo de pantalla
        """
        return cls._snake_body_images_path

    @classmethod
    def get_time_to_refresh(cls) -> int:
        """
        get para obtener el fondo de pantalla
        """
        return cls._time_to_refresh

