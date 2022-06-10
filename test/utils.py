import random

def imprimir_menu(opciones: dict):
   for k, v in opciones.items():
      print(f"{k}: {v['descripcion']}")

def imprimir_batalla(batalla):
   if batalla.turno_entrenador:
      stheader = f"{'V'*30+'|'+'-'*30 if batalla.turno_entrenador == batalla.e1 else '-'*30+'|'+'V'*30}"
      stfooter = f"{'Ʌ'*30+'|'+'-'*30 if batalla.turno_entrenador == batalla.e1 else '-'*30+'|'+'Ʌ'*30}"
   else:
      stheader = stfooter = f"{'-'*30+'|'+'-'*30}"
   e1nombre = e1vida = e1elemento = e1efectos = e2nombre = e2vida = e2elemento = e2efectos = ''
   if batalla.e1.poke_seleccionado:
      e1nombre = batalla.e1.poke_seleccionado.format_nombre()
      e1vida = batalla.e1.poke_seleccionado.format_vida()
      e1elemento = batalla.e1.poke_seleccionado.format_elemento()
      e1efectos = batalla.e1.poke_seleccionado.format_efectos()
   if batalla.e2.poke_seleccionado:
      e2nombre = batalla.e2.poke_seleccionado.format_nombre()
      e2vida = batalla.e2.poke_seleccionado.format_vida()
      e2elemento = batalla.e2.poke_seleccionado.format_elemento()
      e2efectos = batalla.e2.poke_seleccionado.format_efectos()
   
# {batalla.turno_batalla} {batalla.turno_duelo}
   print(f'''
{stheader}
{'': ^30}|{'': ^30}
{batalla.e1.nombre: ^30}|{batalla.e2.nombre: ^30}
{e1nombre: ^30}|{e2nombre: ^30}
{e1vida: ^30}|{e2vida: ^30}
{e1elemento: ^30}|{e2elemento: ^30}
{e1efectos: ^30}|{e2efectos: ^30}
{'': ^30}|{'': ^30}
{stfooter}
''')

def dado():
   v = random.randint(1,6)
   print(f"El dado salio con {v}")
   return v

def menu_seleccion_accion(entrenador):
   return desplegar_menu([
      {'descripcion': 'Usar habilidad', 'valor': entrenador.seleccion_habilidad, 'kwargs': {}},
      {'descripcion': 'Usar item', 'valor': entrenador.seleccion_item, 'kwargs': {}},
      {'descripcion': 'Cambiar de pokemon', 'valor': entrenador.seleccion_pokemon, 'kwargs': {'ninguna': True}},
   ])

def menu_seleccion_habilidad(batalla):
   # devuelve una habilidad
   print('Menu selección item:')
   habilidades = batalla.turno_entrenador.get_poke_seleccionado().habilidades_disponibles(primer_turno=batalla.es_primer_turno())
   return desplegar_menu([{'descripcion': f'{e!s}', 'valor': e} for e in habilidades], ninguna=True)['valor']

def menu_seleccion_item(entrenador):
   # devuelve un item/pocion
   print(f'Atención {entrenador.nombre}!\nSeleeciona un item:')
   return desplegar_menu([{'descripcion': f'{e!s}', 'valor': e} for e in entrenador.pociones], ninguna=True)['valor']

def menu_seleccion_pokemon(entrenador, ninguna=False):
   # devuelve un pokemon
   print(f'Atención {entrenador.nombre}!\nSelecciona un pokemon:')
   return desplegar_menu([{'descripcion': f'{e!s}', 'valor': e} for e in entrenador.get_poke_seleccionables()], ninguna=ninguna)['valor']

def print_inicio_duelo(batalla):
   print(f"\n{' ¡¡¡ INICIA DUELO !!! ':=^61}\n")

def desplegar_menu(opciones: list, ninguna=False):
   opciones_seleccion = dict(enumerate(opciones, start=1))
   if ninguna:
      opciones_seleccion[0] = {'descripcion': 'Volver', 'valor': None}
   while True:
      # print("Opciones disponibles")
      imprimir_menu(opciones_seleccion)
      n = input('Ingresa #: ')
      opcion_numero_seleccion = int(n) if n.isdigit() else None
      if opcion_numero_seleccion in list(opciones_seleccion.keys()):
            opcion_seleccionada = opciones_seleccion[opcion_numero_seleccion]
            # print(f"Opcion seleccionada: {opcion_seleccionada['descripcion']}")
            return opcion_seleccionada
      else:
            print(f"Numero incorrecto de opcion: {opcion_numero_seleccion}")
