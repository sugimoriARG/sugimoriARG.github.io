import utils
import random
import time

sleep_time = 0

class Batalla:
    def __init__(self, entrenador1, entrenador2):
        self.e1 = entrenador1
        self.e2 = entrenador2
        self.turno_entrenador = None
        self.turno_oponente = None
        self.entrenador2_primero = None
        self.turno_batalla = 0
        self.turno_duelo = 0

    def inicializar_duelo(self):
        self.turno_duelo = 0
        if self.e1.poke_seleccionado.tiene_agilidad() and not self.e2.poke_seleccionado.tiene_agilidad():
            self.turno(self.e1)
        elif not self.e1.poke_seleccionado.tiene_agilidad() and self.e2.poke_seleccionado.tiene_agilidad():
            self.turno(self.e2)
    
    def turno(self, nuevo_entrenador_turno):
        # print('cambio turno##############')
        if nuevo_entrenador_turno == self.e1:
            self.turno_entrenador = nuevo_entrenador_turno
            self.turno_oponente = self.e2
        else:
            self.turno_entrenador = nuevo_entrenador_turno
            self.turno_oponente = self.e1
    
    def es_primer_turno(self):
        return self.turno_duelo <= 2

    def inicializar_batalla(self):
        self.turno_batalla = 0

    def incrementar_turno_duelo(self):
        self.turno_duelo += 1
    
    def cambiar_turno_duelo(self):
        if self.turno_entrenador == self.e1:
            self.turno(self.e2)
        else:
            self.turno(self.e1)

    def seleccionan_ambos_pokemon(self, ninguna=False):
        if self.entrenador2_primero: # usual al jugar contra bot
            self.e2.seleccion_pokemon(self, ninguna=ninguna)
            self.e1.seleccion_pokemon(self, ninguna=ninguna)
            self.turno(self.e2)
        else: # cuando se reta a un duelo
            self.e1.seleccion_pokemon(self, ninguna=ninguna)
            self.e2.seleccion_pokemon(self, ninguna=ninguna)
            self.turno(self.e1)

    def duelo(self):
        utils.print_inicio_duelo(self)
        self.inicializar_duelo()

        while self.e1.poke_seleccionado.esta_vivo() and self.e2.poke_seleccionado.esta_vivo():
            self.incrementar_turno_duelo()
            self.print_screen()
            # refactorizar elección de turnos, si tiene agilidad, etc.
            #e_turno, poke_turno, e_oponente, poke_oponente = (e1, poke1, e2, poke2) if turno%2==1 else (e2, poke2, e1, poke1)

            poke_turno = self.turno_entrenador.poke_seleccionado
            poke_oponente = self.turno_oponente.poke_seleccionado
            # print(f"Turno de {poke_turno}")
            # print(f"Oponente {poke_oponente}")
            # utils.imprimir_batalla(self)
            time.sleep(sleep_time)

            # primero se efectua el efecto existente en el pokemon
            poke_turno.ejecutar_buffs()

            res = self.turno_entrenador.turno(self)
            fin_seleccion, fin_turno, cambia_pokemon, resultado_accion = res

            # # seleccionar habilidad
            # .seleccion_habilidad(self)

            # time.sleep(sleep_time)

            # # aplicar efectos sobre el pokemon oponente
            # poke_turno_vida = poke_turno.vida
            # poke_oponente_vida = poke_oponente.vida
            # efectos = poke_turno.usar_habilidad(habilidad_seleccionada, poke_oponente)
            # print(f'la vida de {poke_turno.nombre} cambio de {poke_turno_vida} a {poke_turno.vida} => {poke_turno.vida - poke_turno_vida}')
            # print(f'la vida de {poke_oponente.nombre} cambio de {poke_oponente_vida} a {poke_oponente.vida} => {poke_oponente.vida - poke_oponente_vida}')
            
            # print(f"EFECTOS APLICADOS: {efectos}")

            # turno += 1
            self.cambiar_turno_duelo()
            if cambia_pokemon:
                # si hizo cambio de pokemon reinicia contador de duelo para tener poderes basicos
                self.turno_duelo = 0

        if self.e1.poke_seleccionado.esta_vivo() and not self.e2.poke_seleccionado.esta_vivo():
            print("{} gana el duelo con {} de vida".format(self.e1.poke_seleccionado.nombre, self.e1.poke_seleccionado.vida))
        elif self.e2.poke_seleccionado.esta_vivo() and not self.e1.poke_seleccionado.esta_vivo():
            print("{} gana el duelo con {} de vida".format(self.e2.poke_seleccionado.nombre, self.e2.poke_seleccionado.vida))
        else:
            print("Mueren ambos")
            
    def print_screen(self):
        # clean screen
        # print("-"*100)
        # print("Batalla")
        # if not self.e1.poke_seleccionado:
        #     print(f"batalla entre {self.e1.nombre} y {self.e2.nombre}")
        # else:
        #     print(f"{self.e1.nombre} vs {self.e2.nombre}")
        #     print(f"{self.e1.poke_seleccionado.nombre} vs {self.e2.poke_seleccionado.nombre}")
        utils.imprimir_batalla(self)
        
    def iniciar(self, entrenador2_primero=False):
        self.entrenador2_primero = entrenador2_primero
        self.inicializar_batalla()
        self.print_screen()
        self.seleccionan_ambos_pokemon(ninguna=False)
        while self.e1.tiene_poke_vivos_total() and self.e2.tiene_poke_vivos_total():
            self.duelo()
            if self.e1.poke_seleccionado.esta_vivo() and not self.e2.poke_seleccionado.esta_vivo() and self.e2.tiene_poke_vivos():
                self.e2.seleccion_pokemon(self, ninguna=False)
            elif self.e2.poke_seleccionado.esta_vivo() and not self.e1.poke_seleccionado.esta_vivo() and self.e1.tiene_poke_vivos():
                self.e1.seleccion_pokemon(self, ninguna=False)
            elif self.e1.tiene_poke_vivos() and self.e2.tiene_poke_vivos():
                self.seleccionan_ambos_pokemon()
        
        if not self.e1.tiene_poke_vivos_total() and not self.e2.tiene_poke_vivos_total():
            print("EMPATE")
        elif self.e1.tiene_poke_vivos_total() and not self.e2.tiene_poke_vivos_total():
            print("{} gana la batalla".format(self.e1.nombre))
        elif not self.e1.tiene_poke_vivos_total() and self.e2.tiene_poke_vivos_total():
            print("{} gana la batalla".format(self.e2.nombre))

