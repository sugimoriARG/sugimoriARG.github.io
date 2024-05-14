from efecto import Efecto
import utils

class Buff(Efecto):
    def __init__(self, turno_final=1, turno_inicial=0, permanente=False, remover_con=[], max_stack=1, **kwargs):
        super().__init__(**kwargs)
        self.turno_final = turno_final
        self.turno_inicial = turno_inicial
        self.turno_actual = 0
        self.remover_con = remover_con
        self.permanente = permanente
        self.max_stack = max_stack
    
    def __str__(self):
        return f"{self.__class__.__name__} turnos_restantes({self.turnos_restantes()})"
    def __repr__(self):
        return f'{self.__dict__}'

    def tick_buff(self, pokemon):
        print('tick buff ', self.turnos_restantes())
        if not self.le_queda_turnos() or (self.remover_con and utils.dado() in self.remover_con):
            print(f'no le queda turnos a {self} sobre {pokemon}')
            pokemon.quitar_buff(self)
            return None
        # DO IT
        print(f'Se ejecuta {self}')
        self._aplicar()
        self.turno_actual += 1
        print(f'Se quedan {self.turnos_restantes()} turnos a {self} sobre {pokemon}')

    def le_queda_turnos(self):
        print(self.__class__.__name__, self.turno_actual , self.turno_final)
        return self.permanente or self.turno_actual < self.turno_final

    def turnos_restantes(self):
        print(self.__class__.__name__, self.turno_actual , self.turno_final)
        if self.permanente:
            return -1
        else:
            return self.turno_final - self.turno_actual

class BuffAgilidad(Buff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class BuffDureza(Buff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class BuffDormir(Buff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.remover_con = kwargs.get('remover_con', [])

class BuffDebilidad(Buff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class BuffNoAtacar(Buff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class BuffAutoataque(Buff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# class BuffDescansar(Buff):
#     def __init__(self, turnos=1, **kwargs):
#         super().__init__(**kwargs)

#     def _aplicar(self, pokemon, oponente):
#         pokemon.curar_todo()
#         pokemon.agregar_efecto(EfectoDormir(remover_con=[5,6]))

