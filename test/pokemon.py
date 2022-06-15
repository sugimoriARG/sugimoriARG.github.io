from habilidad import *
from elemento import *
from efecto import *
import utils

class Pokemon:

    def __init__(self, nombre, elemento, vida, habilidades, pasivos):
        self.nombre = nombre
        self.elemento = elemento
        self.elementos_asignados = []
        self.vida = vida
        self.vida_maxima = vida
        self.efectos = []
        self.pasivos = pasivos
        self.habilidades = [h() if type(h) == type(self.__class__) else h for h in habilidades]
        self.habilidades_clases = habilidades
    
    def esta_vivo(self):
        return self.vida > 0

    def asignar_elemento(self, elemento):
        self.elementos_asignados.append(elemento)

    def agregar_efecto(self, efecto, oponente=None):
        # ver que no exista ya ese tipo de efecto
        self.efectos.append(efecto)
        efecto.aplicar(self, oponente)

    def quitar_efecto(self, efecto):
        if efecto in self.efectos:
            self.efectos.remove(efecto)

    def recibir_danio(self, danio, elemento):
        return self._restar_vida(elemento.calcular_danio(self, danio))

    def usar_habilidad(self, habilidad, oponente):
        # print(habilidad.__dict__)
        efecto_noataca = self.no_ataca_remover()
        if efecto_noataca:
            utils.print_noataco(self, habilidad, oponente, efecto_noataca)
            return []
        return habilidad.usar(self, oponente)

    def no_ataca_remover(self):
        efectos = [e for e in self.efectos if e.__class__ == EfectoNoAtacar]
        self.efectos = [e for e in self.efectos if e.__class__ != EfectoNoAtacar]
        return efectos
    
    def get_efectos_debilidad(self):
        efectos = [e for e in self.efectos if e.__class__ == EfectoDebilidad]
        return efectos
    
    def habilidades_disponibles(self, primer_turno=False):
        if primer_turno:
            return [h for h in self.habilidades if len(h.costes) == len(self.habilidades[0].costes)]
        return self.habilidades

    def _restar_vida(self, danio):
        self.vida -= danio
        if self.vida < 0:
            self.vida = 0
        return self.vida
    
    def curar(self, cantidad):
        self.vida += cantidad
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
        return self.vida

    def curar_todo(self):
        self.vida = self.vida_maxima
        return self.vida

    def ejecutar_efectos(self):
        # cuando inicia un turno nuevo se aplican los efectos sobre el pkm
        for efecto in self.efectos:
            efecto._aplicar_efecto(self)
        # self.sumar_turnos_efectos()
        # self.remover_efectos_viejos()

    def sumar_turnos_efectos(self):
        print(self.efectos)
        for e in self.efectos:
            e.turno_actual += 1
    
    def remover_efectos_viejos(self):
        for e in self.efectos:
            if not e.le_queda_turnos():
                self.efectos.remove(e)
                print(f'EFECTO {e} REMOVIDO')
    
    def tiene_agilidad(self):
        return 'EfectoAgilidad' in [p.__class__.__name__ for p in self.pasivos]

    def format_vida(self):
        return f'[{self.vida}/{self.vida_maxima}]'
    def format_elemento(self):
        return f'{self.elemento}'
    def format_efectos(self):
        return f'{",".join([e.__class__.__name__ for e in self.efectos])}'
    def format_nombre(self):
        return f'<<{self.nombre}>>'
    def __str__(self):
        return f"<<{self.nombre}>> {self.format_vida()} {self.elemento.format_color()} {self.efectos}"

# poke1 = Pokemon("poke_fuego", "fuego", 50, [GolpeFuego, Llamarada])

class Charmander(Pokemon):
    def __init__(self):
        super().__init__(
            "Charmander", 
            Fuego(), 
            50, 
            [
                GolpeBasico(
                    nombre="Rasguños",
                    efectos = [
                        EfectoDanio(
                            Normal, 
                            cantidad=10, 
                            aumento=20, 
                            aumento_probabilidad=[4,5,6]
                        ),
                    ]
                ),
                GolpeBasico(
                    nombre="Giro-fuego",
                    costes=[Fuego, Fuego],
                    efectos = [
                        EfectoDanio(
                            Fuego, 
                            cantidad=20, 
                            aumento=50, 
                            aumento_probabilidad=[5,6]
                        ),
                    ]
                ),
                GolpeBasico(
                    nombre="Lanzallamas",
                    costes=[Fuego, Fuego],
                    efectos = [
                        EfectoDanio(Fuego, cantidad=30)
                    ]
                ),
            ], 
            []
        )


# poke2 = Pokemon("poke_agua", "agua", 50, [GolpeAgua, Burbujas])

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__(
            "Squirtle", 
            Agua(), 
            600, 
            [
                GolpeBasico(
                    nombre="Cabezazo",
                    efectos = [EfectoDanio(Normal, cantidad=20)]
                ),
                GolpeBasico(
                    nombre="Refugio",
                    costes=[Normal, Normal],
                    efectos = [EfectoDureza(cantidad=10, stack=1)]
                ),
                GolpeBasico(
                    nombre="Burbujas",
                    costes=[Agua, Agua],
                    efectos = [
                        EfectoDanio(Agua, cantidad=20),
                        AplicadorDeEfecto(EfectoDebilidad(cantidad=10))
                    ]
                )
            ], 
            []
        )

# class Snorlax(Pokemon):
#     def __init__(self):
#         super().__init__("Snorlax", Normal(), 100, [GolpesFuria, Descansar, Cabezazo], [EfectoDureza])

class Machop(Pokemon):
    def __init__(self):
        super().__init__(
            "Machop", 
            Lucha(), 
            60, 
            [
                GolpeBasico(
                    nombre="Golpe karate",
                    costes=[Lucha],
                    efectos = [EfectoDanio(Lucha, cantidad=20)]
                ),
                GolpeBasico(
                    nombre="Gruñido",
                    efectos = [
                        AplicadorDeEfecto(EfectoDebilidad(cantidad=10,stack=1))
                    ]
                ),
                GolpeBasico(
                    nombre="Lluvia de golpes",
                    costes=[Lucha, Lucha],
                    efectos = [
                        EfectoDanio(
                            Lucha, 
                            cantidad=20, 
                            aumento=20,
                            aumento_probabilidad=[5,6],
                            aumento_repetible=True
                        )
                    ]
                )
            ], 
            []
        )

class Abra(Pokemon):
    def __init__(self):
        super().__init__(
            "Abra", 
            Psiquico(), 
            50, 
            [
                GolpeBasico(
                    nombre="Hipno-rayo",
                    costes=[Psiquico],
                    efectos = [
                        EfectoDanio(Psiquico, cantidad=10),
                        AplicadorDeEfecto(EfectoAutoataque(probabilidad=[1,2]))
                        ]
                ),
                GolpeBasico(
                    nombre="Confusion",
                    costes=[Psiquico, Psiquico],
                    efectos = [
                        EfectoDanio(Psiquico, cantidad=10),
                        AplicadorDeEfecto(EfectoAutoataque(probabilidad=[1,2,3], permanente=True))
                        ]
                ),
                GolpeBasico(
                    nombre="Rayo psiquico",
                    costes=[Psiquico, Psiquico, Psiquico],
                    efectos = [EfectoDanio(Psiquico, cantidad=40)]
                )
            ], 
            []
        )



class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__(
            "Bulbasaur", 
            Planta(), 
            600, 
            [
                GolpeBasico(
                    nombre="Lianas",
                    costes=[Planta],
                    efectos = [
                        EfectoDanio(Planta, cantidad=10),
                        AplicadorDeEfecto(EfectoNoAtacar(), probabilidad=[5,6])
                    ]
                ),
                GolpeBasico(
                    nombre="Embestida",
                    costes=[Normal, Normal],
                    efectos = [
                        EfectoDanio(Normal, cantidad=20)
                    ]
                ),
                GolpeBasico(
                    nombre="Hojas navaja",
                    costes=[Planta, Planta],
                    efectos = [EfectoDanio(Planta, cantidad=30)]
                )
            ], 
            []
        )


