# TODO: Convertir esto en clases, no hace falta instanciarlo
from colores import Colores

class Elemento:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.print_reset = Colores.RESET

    def format_color(self):
        return f'{self.print_color}{self.nombre.title()}{self.print_reset}'
    
    def descripcion(self):
        return f'{self.nombre.title()}'
    
    def calcular_danio(self, pokemon, danio):
        if self.nombre in pokemon.elemento.debilidades:
            return danio + 10
        elif self.nombre in pokemon.elemento.fortalezas:
            return danio - 10
        else:
            return danio

    def copiar(self):
        return self.__class__()
    
    def __eq__(self, __o: object) -> bool:
        return self.nombre == __o.nombre
    
    def __hash__(self):
        return self.nombre.__hash__()

    __str__ = descripcion

class Agua(Elemento):
    def __init__(self,**kwargs):
        super().__init__('agua')
        self.clase = __class__.__name__.lower()
        self.fortalezas = ['fuego', 'roca', 'tierra']
        self.print_color = Colores.AGUA
        self.debilidades = ['planta']

class Electrico(Elemento):
    def __init__(self,**kwargs):
        super().__init__('electrico')
        self.fortalezas = ['viento', 'agua']
        self.debilidades = ['planta', 'tierra', 'roca']
        self.print_color = Colores.ELECTRICO

class Fantasma(Elemento):
    def __init__(self,**kwargs):
        super().__init__('fantasma')
        self.fortalezas = ['psiquico']
        self.debilidades = []
        self.print_color = Colores.FANTASMA

class Fuego(Elemento):
    def __init__(self,**kwargs):
        super().__init__('fuego')
        self.fortalezas = ['planta', 'hielo', 'insecto']
        self.debilidades = ['agua', 'tierra', 'roca']
        self.print_color = Colores.FUEGO

class Hielo(Elemento):
    def __init__(self,**kwargs):
        super().__init__('hielo')
        self.fortalezas = ['planta']
        self.debilidades = ['fuego', 'agua']
        self.print_color = Colores.HIELO

class Insecto(Elemento):
    def __init__(self,**kwargs):
        super().__init__('insecto')
        self.fortalezas = ['planta', 'tierra', 'psiquico']
        self.debilidades = ['viento', 'veneno']
        self.print_color = Colores.INSECTO

class Lucha(Elemento):
    def __init__(self,**kwargs):
        super().__init__('lucha')
        self.fortalezas = ['hielo', 'roca']
        self.debilidades = ['psiquico', 'viento', 'veneno']
        self.print_color = Colores.LUCHA

class Normal(Elemento):
    def __init__(self,**kwargs):
        super().__init__('normal')
        self.fortalezas = []
        self.debilidades = ['roca']
        self.print_color = Colores.NORMAL

class Planta(Elemento):
    def __init__(self,**kwargs):
        super().__init__('planta')
        self.fortalezas = ['agua', 'tierra', 'roca']
        self.debilidades = ['fuego', 'hielo', 'veneno']
        self.print_color = Colores.PLANTA

class Psiquico(Elemento):
    def __init__(self,**kwargs):
        super().__init__('psiquico')
        self.fortalezas = []
        self.debilidades = ['fantasma']
        self.print_color = Colores.PSIQUICO

class Tierra(Elemento):
    def __init__(self,**kwargs):
        super().__init__('tierra')
        self.fortalezas = ['fuego', 'roca', 'veneno']
        self.debilidades = ['planta', 'viento', 'agua']
        self.print_color = Colores.TIERRA

class Veneno(Elemento):
    def __init__(self,**kwargs):
        super().__init__('veneno')
        self.fortalezas = ['planta', 'lucha', 'insecto']
        self.debilidades = ['psiquico', 'tierra', 'roca']
        self.print_color = Colores.VENENO

class Volador(Elemento):
    def __init__(self,**kwargs):
        super().__init__('volador')
        self.fortalezas = ['planta', 'lucha', 'insecto']
        self.debilidades = ['roca']
        self.print_color = Colores.VOLADOR
