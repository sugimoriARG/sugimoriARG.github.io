# TODO: Convertir esto en clases, no hace falta instanciarlo

class Elemento:
    def __init__(self, nombre: str):
        self.nombre = nombre

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
    
    __str__ = descripcion

class Agua(Elemento):
    def __init__(self,**kwargs):
        super().__init__('agua')
        self.clase = __class__.__name__.lower()
        self.fortalezas = ['fuego', 'roca', 'tierra']
        self.debilidades = ['planta']

class Electrico(Elemento):
    def __init__(self,**kwargs):
        super().__init__('electrico')
        self.fortalezas = ['viento', 'agua']
        self.debilidades = ['planta', 'tierra', 'roca']

class Fantasma(Elemento):
    def __init__(self,**kwargs):
        super().__init__('fantasma')
        self.fortalezas = ['psiquico']
        self.debilidades = []

class Fuego(Elemento):
    def __init__(self,**kwargs):
        super().__init__('fuego')
        self.fortalezas = ['planta', 'hielo', 'insecto']
        self.debilidades = ['agua', 'tierra', 'roca']

class Hielo(Elemento):
    def __init__(self,**kwargs):
        super().__init__('hielo')
        self.fortalezas = ['planta']
        self.debilidades = ['fuego', 'agua']

class Insecto(Elemento):
    def __init__(self,**kwargs):
        super().__init__('insecto')
        self.fortalezas = ['planta', 'tierra', 'psiquico']
        self.debilidades = ['viento', 'veneno']

class Lucha(Elemento):
    def __init__(self,**kwargs):
        super().__init__('lucha')
        self.fortalezas = ['hielo', 'roca']
        self.debilidades = ['psiquico', 'viento', 'veneno']

class Normal(Elemento):
    def __init__(self,**kwargs):
        super().__init__('normal')
        self.fortalezas = []
        self.debilidades = ['roca']

class Planta(Elemento):
    def __init__(self,**kwargs):
        super().__init__('planta')
        self.fortalezas = ['agua', 'tierra', 'roca']
        self.debilidades = ['fuego', 'hielo', 'veneno']

class Psiquico(Elemento):
    def __init__(self,**kwargs):
        super().__init__('psiquico')
        self.fortalezas = []
        self.debilidades = ['fantasma']

class Tierra(Elemento):
    def __init__(self,**kwargs):
        super().__init__('tierra')
        self.fortalezas = ['fuego', 'roca', 'veneno']
        self.debilidades = ['planta', 'viento', 'agua']

class Veneno(Elemento):
    def __init__(self,**kwargs):
        super().__init__('veneno')
        self.fortalezas = ['planta', 'lucha', 'insecto']
        self.debilidades = ['psiquico', 'tierra', 'roca']

class Volador(Elemento):
    def __init__(self,**kwargs):
        super().__init__('volador')
        self.fortalezas = ['planta', 'lucha', 'insecto']
        self.debilidades = ['roca']
