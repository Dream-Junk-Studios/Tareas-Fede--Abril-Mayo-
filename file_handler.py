import contextlib


class Singleton(type):
    """
    Esta clase implementa el patrón Singleton para asegurarse de que sólo exista una instancia
    de la clase FileHandler.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class FileHandler(metaclass=Singleton):
    """
    Esta clase se utiliza para manejar los archivos y su contenido.
    """
    def __init__(self):
        self._archivo = None

    @contextlib.contextmanager
    def abrir_archivo(self, nombre_archivo, modo="r", codificacion=None):
        if self._archivo is not None:
            raise ValueError("El archivo ya está abierto.")
        try:
            self._archivo = open(nombre_archivo, modo, encoding=codificacion)
            yield self._archivo
        finally:
            self.cerrar_archivo()

    def leer_archivo(self):
        if self._archivo is None:
            raise ValueError("El archivo no está abierto.")
        return self._archivo.read()

    def escribir_archivo(self, contenido):
        if self._archivo is None:
            raise ValueError("El archivo no está abierto.")
        self._archivo.write(contenido)

    def cerrar_archivo(self):
        if self._archivo is not None:
            self._archivo.close()
            self._archivo = None