from typing import List
from efecto import EfectoDanio #, EfectoAumentoDanio, EfectoDisminucionDanio
from elemento import Agua, Electrico, Fantasma, Fuego, Hielo, Insecto, Lucha, Normal, Planta, Psiquico, Tierra, Veneno, Volador
from utils import dado
from collections import Counter

# Una habilidad es un paquete de efectos
class Habilidad:
    
    def __init__(self, nombre, costes, probabilidad, descripcion, efectos: List[EfectoDanio]):
        self.nombre = nombre
        self.costes = [c() for c in costes]
        self.costes_classes = costes
        self.probabilidad = probabilidad
        self.descripcion = descripcion
        self.efectos = efectos

    # def siempre(self):
    #     return len(self.probabilidad) != 6
    
    # def nunca(self):
    #     return len(self.probabilidad) == 0

    def usar(self, pokemon, oponente):
        efectos_aplicados = []
        for efecto in self.efectos:
            efectos_aplicados.append(efecto.aplicar(pokemon, oponente))
        return efectos_aplicados

    def porcentaje(self):
        return len(self.probabilidad)/6
    
    def format_porcentaje(self):
        return f"{self.porcentaje()*100:.2f}%"

    def format_probabilidad(self):
        return f"{len(self.probabilidad)}/6"

    def format_costes(self):
        costes = [f'{c.format_color()}x{cant}' for c, cant in Counter(self.costes).items()]
        return f"{','.join(costes)}"
    
    def format_nombre(self):
        return f"{self.nombre.title()}"

    def texto_descripcion(self):
        descripcion_efectos=""
        descripcion_efectos = ', '.join(f'{efecto!s}' for efecto in self.efectos)  
        color = self.costes[0].print_color
        return f"{self.format_nombre()} <{self.format_costes()} | {descripcion_efectos}>"
        # return f"Habilidad: {self.nombre.title()}\nCoste: {','.join(self.costes)}\nProbabilidad: {self.format_porcentaje()}\nEfectos: {descripcion_efectos}"

    __str__ = texto_descripcion

class GolpeBasico(Habilidad):
    def __init__(self, **kwargs):
        super().__init__(
            nombre = kwargs.get('nombre', 'golpe básico'),
            costes = kwargs.get('costes', [Normal]),
            probabilidad = kwargs.get('probabilidad', [1,2,3,4,5,6]), # no se usa
            descripcion = kwargs.get('descripcion', 'golpe básico'),
            efectos = kwargs.get('efectos', [EfectoDanio(Normal, cantidad=0)])
        )
