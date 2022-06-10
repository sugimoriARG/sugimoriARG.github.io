from utils import dado
from elemento import Normal

class Efecto:
    def __init__(self, elemento=Normal, probabilidad=[1,2,3,4,5,6], turno_final=1, turno_inicial=0, permanente=False, **kwargs):
        self.elemento = elemento() if type(elemento) == type(self.__class__) else elemento.copiar()
        self.probabilidad = probabilidad
        self.turno_final = turno_final
        self.turno_inicial = turno_inicial
        self.turno_actual = 0
        self.remover_con = []
        self.permanente = permanente
        self.aumento = kwargs.get('aumento', False)
        self.aumento_probabilidad = kwargs.get('aumento_probabilidad', False)
        self.aumento_repetible = kwargs.get('aumento_repetible', False)
    def __str__(self):
        return str(self.__dict__)
    def siempre(self):
        return len(self.probabilidad) == 6
    def nunca(self):
        return len(self.probabilidad) == 0
    def porcentaje(self):
        return len(self.probabilidad)/6
    def format_porcentaje(self):
        return f"{self.porcentaje()*100:.2f}%"
    def format_probabilidad2(self):
        return f"{len(self.probabilidad)}/6"
    def format_probabilidad(self):
        return "" if self.siempre() else f"{self.probabilidad}"
    def format_aumento(self):
        return "" if not self.aumento else f"{self.probabilidad}{self.aumento_repetible}"
    def format_extras(self):
        return " ".join([f"{self.format_probabilidad()}",f"{self.format_aumento()}"])
    def __str__(self):
        return f"{self.__class__.__name__} ({self.elemento} {getattr(self, 'cantidad', '')}){self.format_extras()}"


    def aplicar(self, pokemon, oponente): # pokemon es la victima, oponente es el atacante
        return self.copiar()._aplicar_en_copia(pokemon, oponente)
    
    def _aplicar_en_copia(self, pokemon, oponente): 
        # el turno 0 es el mismo instante que se aplica el efecto
        self.turno_actual += 1
        if self.turno_actual > self.turno_inicial:
            if self.turno_actual <= self.turno_final:
                if self.removible_con_dado() and dado() in self.remover_con:
                    pokemon.quitar_efecto(self)
                    return None
                if self.siempre() or dado() in self.probabilidad:
                    print(f"{pokemon.nombre} aplica {self} sobre {oponente.nombre}")
                    self._aplicar(pokemon, oponente)
                else:
                    print(f"{pokemon.nombre} no aplica {self} sobre {oponente.nombre}")
                return None
            else:
                if not self.permanente:
                    pokemon.quitar_efecto(self)

    def removible_con_dado(self):
        return getattr(self, 'remover_con', [])

    def copiar(self):
        return self.__class__(**self.__dict__)


### BASES ###
class EfectoBasePasivo(Efecto):
    def __init__(self, elemento, probabilidad=[1,2,3,4,5,6], turno_final=1, turno_inicial=0, permanente=True, **kwargs):
        super().__init__(elemento, probabilidad, turno_final, turno_inicial, permanente, **kwargs)
        self.remover_con = [1]
    def _aplicar(self, pokemon, oponente):
        self.elemento.aplicar(pokemon, oponente)

class EfectoBaseProximoTurno(Efecto):
    def __init__(self, turno_final=2, turno_inicial=1, **kwargs):
        super().__init__(turno_final=turno_final, turno_inicial=turno_inicial, **kwargs)

### FIN BASES ###

class EfectoDanio(Efecto):
    def __init__(self, cantidad, elemento, **kwargs):
        super().__init__(elemento=elemento, **kwargs)
        self.cantidad = cantidad
        
    def _aplicar(self, pokemon, oponente):
        oponente.recibir_danio(self.cantidad, self.elemento)
        if self.aumento and dado() in self.probabilidad:
            print('Vuelve a golpear!')
            oponente.recibir_danio(self.aumento, self.elemento)
            if self.aumento_repetible:
                while dado() in self.aumento_probabilidad:
                    print('Vuelve a golpear!')
                    oponente.recibir_danio(self.aumento, self.elemento)

class EfectoDrenar(Efecto):
    def __init__(self, cantidad, elemento, **kwargs):
        super().__init__(elemento=elemento, **kwargs)
        self.cantidad = cantidad

    def _aplicar(self, pokemon, oponente):
        pokemon.curar(oponente.vida - oponente.recibir_danio(self.cantidad, self.elemento))

class EfectoAgilidad(Efecto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _aplicar(self, pokemon, oponente):
        # No se aplica ya que es un efecto pasivo
        pass

class EfectoDureza(Efecto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _aplicar(self, pokemon, oponente):
        # TODO
        # No se aplica ya que es un efecto pasivo ??
        pass

class EfectoDormir(Efecto):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.remover_con = kwargs.get('remover_con', [])

    def _aplicar(self, pokemon, oponente):
        # No se aplica ya que es un efecto pasivo ??
        # pasar el turno
        pass

class EfectoDebilidad(EfectoBaseProximoTurno):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _aplicar(self, pokemon, oponente):
        # No se aplica ya que es un efecto pasivo ??
        pass


class AplicadorDeEfecto(Efecto):
    def __init__(self, efecto_a_aplicar, **kwargs):
        super().__init__(**kwargs)
        self.efecto_a_aplicar = efecto_a_aplicar

    def _aplicar(self, pokemon, oponente):
        if self.aumento and dado() in self.probabilidad:
            oponente.agregar_efecto(self.efecto_a_aplicar)

class EfectoNoAtacar(EfectoBaseProximoTurno):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _aplicar(self, pokemon, oponente):
        # No se aplica ya que es un efecto pasivo
        pass

class EfectoAutoataque(EfectoBaseProximoTurno):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _aplicar(self, pokemon, oponente):
        # No se aplica ya que es un efecto pasivo
        pass


# class EfectoDescansar(Efecto):
#     def __init__(self, turnos=1, **kwargs):
#         super().__init__(**kwargs)

#     def _aplicar(self, pokemon, oponente):
#         pokemon.curar_todo()
#         pokemon.agregar_efecto(EfectoDormir(remover_con=[5,6]))


