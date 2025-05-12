import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import randint, choice


class SnakeBlock(Sprite):
    #Atributos de clase(banderas de movimiento de la serpiente)
    _is_moving_right=False
    _is_moving_left=False
    _is_moving_up=False
    _is_moving_down=False

    def __init__(self, is_head: bool = False):
        """
        Constructor de la serpiente, en donde se llama al constructor padre de Sprite.
        :param is_head: Indica si el bloque es o no la cabeza de la serpiente.
        """
        # Se llama al constructor de la clase padre.
        super().__init__()

        # Lista que almacena los frames de la cabeza de la serpiente.
        self._head_frames = []

        # Cada uno de los frames se debe de escalar antes de ser guardado en la lista.
        snake_block_size = Configurations.get_snake_block_size()

        # Si es la cabeza de la serpiente, se almacenan todos los frames que dan la impresión de movimiento.
        if is_head:

            for i in range(len(Configurations.get_snake_heads_path())):
                frame = pygame.image.load(Configurations.get_snake_heads_path()[i])
                frame = pygame.transform.scale(frame, (snake_block_size, snake_block_size))
                self._head_frames.append(frame)

            # Se incluyen dos atributos más para la cabeza de la serpiente.
            # Además, la imagen se selecciona como el primer elemento de la lista con los frames.
            self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
            self._frame_index = 0

            # Índice de la lista.
            self.image = self._head_frames[self._frame_index]
            self._frame_index = 1

        else:
            # Se selecciona una imagen aleatoria para el cuerpo de la serpiente.
            body_images_path = Configurations.get_snake_body_images_path()
            random_body_image_path = choice(body_images_path)
            self.image = pygame.image.load(random_body_image_path)

            # Se escala la imagen al tamaño del bloque.
            snake_block_size = Configurations.get_snake_block_size()
            self.image = pygame.transform.scale(self.image, (snake_block_size, snake_block_size))

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

    def blit(self,screen:pygame.surface.Surface)->None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        :param screen: Pantalla donde se dibuja
        """
        angle=0
        if SnakeBlock.get_is_moving_up():
            angle=90
        elif SnakeBlock.get_is_moving_left():
            angle=180
        elif SnakeBlock.get_is_moving_down():
            angle=270

        image_flip=pygame.transform.rotate(self.image,angle)
        screen.blit(image_flip,self.rect)

    def snake_head_init(self)->None:
        screen_width=Configurations.get_screen_size()[0]
        screen_height=Configurations.get_screen_size()[1]
        snake_block_size=Configurations.get_snake_block_size()

        #posicion aleatora de la cabeza de la snake
        self.rect.x=snake_block_size*randint(0,(screen_width//snake_block_size)-1)
        self.rect.y=snake_block_size*randint(0,(screen_height//snake_block_size)-1)

    def animate_snake_head(self) -> None:
        """
        Se utiliza para actualizar el frame visible de la cabeza de la serpiente, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        time_to_refresh = Configurations.get_time_to_refresh_head_snake_frames()
        needs_refresh = (current_time - self._last_update_time) >= time_to_refresh

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._head_frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._head_frames):
                self._frame_index = 0

    #right
    @classmethod
    def get_is_moving_right(cls)->bool:
        """
        Getter para la bandera _is_moving_right
        """
        return cls._is_moving_right

    @classmethod
    def set_is_moving_right(cls,value:bool)->None:
        """
        Setter para la bandera _is_moving_right
        """
        cls._is_moving_right=value

    #left
    @classmethod
    def get_is_moving_left(cls)->bool:
        """
        Getter para la bandera _is_moving_right
        """
        return cls._is_moving_left

    @classmethod
    def set_is_moving_left(cls,value:bool)->None:
        """
        Setter para la bandera _is_moving_right
        """
        cls._is_moving_left=value

    #Up
    @classmethod
    def get_is_moving_up(cls)->bool:
        """
        Getter para la bandera _is_moving_right
        """
        return cls._is_moving_up

    @classmethod
    def set_is_moving_up(cls,value:bool)->None:
        """
        Setter para la bandera _is_moving_right
        """
        cls._is_moving_up=value

    #down
    @classmethod
    def get_is_moving_down(cls)->bool:
        """
        Getter para la bandera _is_moving_right
        """
        return cls._is_moving_down

    @classmethod
    def set_is_moving_down(cls,value:bool)->None:
        """
        Setter para la bandera _is_moving_right
        """
        cls._is_moving_down=value