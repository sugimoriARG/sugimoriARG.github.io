import utils
from elemento import Normal

class Efecto:
    def __init__(self, cantidad=0, elemento=Normal, probabilidad=[1,2,3,4,5,6], **kwargs):
        self.elemento = elemento() if type(elemento) == type(self.__class__) else elemento.copiar()
        self.probabilidad = probabilidad
        self.cantidad = cantidad
        self.aumento = kwargs.get('aumento', False)
        self.aumento_probabilidad = kwargs.get('aumento_probabilidad', [])
        self.aumento_repetible = kwargs.get('aumento_repetible', False)
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
        return "" if self.siempre() else f"{','.join(map(str, self.probabilidad))}"
    def format_aumento_probabilidad(self):
        return f"{','.join(map(str, self.aumento_probabilidad))}"
    def format_aumento(self):
        return "" if not self.aumento else f"{self.aumento}"
    def format_repetible(self):
        return "repetible" if self.aumento_repetible else "no repetible"
    def format_extras(self):
        return "" if not self.aumento else f' Aumento({self.format_aumento_probabilidad()}/{self.format_aumento()}/{self.format_repetible()})'
    def format_detalle(self):
        return ','.join([f"{self.elemento}"] + [f"{self.cantidad}"])
    def __str__(self):
        return f"{self.__class__.__name__}({self.format_detalle()}){self.format_extras()}"
    def __repr__(self):
        return f'{self.__dict__}'

    def aplicar(self, pokemon, oponente): # pokemon es la victima, oponente es el atacante
        if self.siempre() or utils.dado() in self.probabilidad:
            print(f"{pokemon.nombre} aplica {self} sobre {oponente.nombre}!!")
            self._aplicar(pokemon, oponente)
        else:
            print(f"{pokemon.nombre} no aplica {self} sobre {oponente.nombre}")
        return None

    def _aplicar(self, *args, **kwargs):
        pass

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

class EfectoBaseProximoTurnoEnemigo(Efecto):
    def __init__(self, turno_final=1, turno_inicial=0, **kwargs):
        super().__init__(turno_final=turno_final, turno_inicial=turno_inicial, **kwargs)

### FIN BASES ###

class EfectoDanio(Efecto):
    def __init__(self, elemento, **kwargs):
        super().__init__(elemento=elemento, **kwargs)
        
    def _aplicar(self, pokemon, oponente):
        # oponente.recibir_danio(self.cantidad, self.elemento)
        efectos_debil = pokemon.get_efectos_debilidad()
        utils.print_efectos_debilidad(pokemon, oponente, efectos_debil)
        debil = sum([e.cantidad for e in efectos_debil])
        cantidad = self.cantidad - debil
        if self.aumento and utils.dado() in self.aumento_probabilidad:
            print('Vuelve a golpear!')
            # oponente.recibir_danio(self.aumento, self.elemento)
            cantidad += self.aumento
            if self.aumento_repetible:
                while utils.dado() in self.aumento_probabilidad:
                    print('Vuelve a golpear!')
                    # oponente.recibir_danio(self.aumento, self.elemento)
                    cantidad += self.aumento
        oponente.recibir_danio(cantidad, self.elemento)

class EfectoDrenar(Efecto):
    def __init__(self, elemento, **kwargs):
        super().__init__(elemento=elemento, **kwargs)

    def _aplicar(self, pokemon, oponente):
        pokemon.curar(oponente.vida - oponente.recibir_danio(self.cantidad, self.elemento))

class AplicarBuff(Efecto):
    def __init__(self, buff_a_aplicar, a_oponente=True, **kwargs):
        super().__init__(**kwargs)
        self.buff_a_aplicar = buff_a_aplicar
        self.a_oponente = a_oponente

    def _aplicar(self, pokemon, oponente):
        if self.a_oponente:
            # aplica a oponente (normalmente)
            oponente.agregar_buff(self.buff_a_aplicar.copiar())
        else:
            # aplica a self
            pokemon.agregar_buff(self.buff_a_aplicar.copiar())
    
    def __str__(self):
        return f"AplicarBuff({self.buff_a_aplicar}, {self.probabilidad})"

