import random
import utils

class Entrenador:
    def __init__(self, nombre, pokemones, print_color=''):
        self.nombre = nombre
        self.pokemones = pokemones
        self.poke_seleccionado = None
        self.pociones = []
        self.pokebolas = 0
        self.print_color = print_color

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

    def elegir_poke(self, ninguna=False):
        # return random.choice(self.get_poke_vivos())
        self.seleccion_pokemon(batalla=None, ninguna=ninguna)
        

    def cambiar_pokemon(self, pokemon):
        self.poke_seleccionado = pokemon
        
    def tiene_poke_vivos(self):
        return len(self.get_poke_vivos()) > 0
    
    def tiene_poke_vivos_total(self):
        return self.tiene_poke_vivos() or self.poke_seleccionado.esta_vivo()
    
    def get_poke_vivos(self):
        return [p for p in self.pokemones if p.esta_vivo()]

    def get_poke_seleccionables(self):
        todos = self.get_poke_vivos()
        if self.poke_seleccionado and self.poke_seleccionado.esta_vivo():
            todos.remove(self.poke_seleccionado)
        return todos

    def get_poke_seleccionado(self):
        if not self.poke_seleccionado or self.poke_seleccionado.vida <= 0:
            self.poke_seleccionado = self.elegir_poke()
        return self.poke_seleccionado

    def usar_habilidad(self, habilidad, poke_oponente):
        self.get_poke_seleccionado().usar_habilidad(habilidad, poke_oponente)
    
    def seleccion_accion(self, batalla): # ver si agregar la opcion de volver al menu principal
        fin_seleccion = False
        while not fin_seleccion:
            opcion = utils.menu_seleccion_accion(self)
            fin_seleccion, fin_turno, cambia_pokemon, resultado_accion = opcion['valor'](batalla, **opcion['kwargs'])
        return fin_seleccion, fin_turno, cambia_pokemon, resultado_accion

    def seleccion_habilidad(self, batalla):
        fin_seleccion = fin_turno = cambia_pokemon = resultado_accion = False
        habilidad_seleccionada = utils.menu_seleccion_habilidad(batalla)
        if habilidad_seleccionada:
            print(f"Es el turno {batalla.turno_batalla} de {self.get_poke_seleccionado().nombre}. Utiliza {habilidad_seleccionada.format_nombre()}")
            print(f"{habilidad_seleccionada.texto_descripcion()}")
            resultado_accion = self.usar_habilidad(habilidad_seleccionada, batalla.turno_oponente.get_poke_seleccionado())
            fin_seleccion = fin_turno = True
        return fin_seleccion, fin_turno, cambia_pokemon, resultado_accion

    def seleccion_item(self, batalla):
        fin_seleccion = fin_turno = cambia_pokemon = resultado_accion = False
        item = utils.menu_seleccion_item(self)
        if item:
            print(f'{self.nombre} uso {item.nombre}')
        return fin_seleccion, fin_turno, cambia_pokemon, resultado_accion

    def seleccion_pokemon(self, batalla, ninguna=False):
        fin_seleccion = fin_turno = cambia_pokemon = resultado_accion = False
        pokemon = utils.menu_seleccion_pokemon(self, ninguna=ninguna)
        if pokemon:
            print(f'{self.nombre} selecciono {pokemon.nombre}')
            resultado_accion = self.cambiar_pokemon(pokemon)
            fin_seleccion = fin_turno = cambia_pokemon = True
        return fin_seleccion, fin_turno, cambia_pokemon, resultado_accion

    def turno(self, batalla):
        poke_turno = batalla.turno_entrenador.get_poke_seleccionado()
        poke_oponente = batalla.turno_oponente.get_poke_seleccionado()
        poke_turno_vida = poke_turno.vida
        poke_oponente_vida = poke_oponente.vida
        resultado = self.seleccion_accion(batalla)
        # puede usar un item
        # puede cambiar pokemon
        # self.get_poke_seleccionado()
        print(f'la vida de {poke_turno.nombre} cambio de [{poke_turno_vida}/{poke_turno.vida_maxima}] a [{poke_turno.vida}/{poke_turno.vida_maxima}] => {poke_turno.vida - poke_turno_vida}')
        print(f'la vida de {poke_oponente.nombre} cambio de [{poke_oponente_vida}/{poke_oponente.vida_maxima}] a [{poke_oponente.vida}/{poke_oponente.vida_maxima}] => {poke_oponente.vida - poke_oponente_vida}')
        return resultado
