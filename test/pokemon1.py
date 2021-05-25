import random
import time
import ast

class Pokemon:

    def __init__(self, nombre, clase, vida, habilidades):
        self.nombre = nombre
        self.clase = clase
        self.vida = vida
        self.habilidades = habilidades
 

class Habilidad:
    
    def __init__(self, nombre, costes, probabilidad, descripcion, efectos):
        self.nombre = nombre
        self.costes = costes
        self.probabilidad = probabilidad
        self.descripcion = descripcion
        self.efectos = efectos

    def __str__(self):
        descripcion_efectos=""
        for efecto in self.efectos:
            descripcion_efectos += str(efecto)
        
        return "{} con coste {}, probabilidad {} y efectos {}".format(self.nombre, self.costes, self.probabilidad, descripcion_efectos) 

class EfectoDanio:

    def __init__(self, danio):
        self.danio = danio

    def __str__(self):
        return str(self.__dict__)

class EfectoAumentoDanio(EfectoDanio):

    def __init__(self, danio, probabilidad):
        self.danio = danio
        self.probabilidad = probabilidad

    def __str__(self):
        return str(self.__dict__)


class EfectoDisminucionDanio(EfectoDanio):

    def __init__(self, dimuninucion_danio, probabilidad):
        self.dimuninucion_danio = dimuninucion_danio
        self.probabilidad = probabilidad
        self.accion = "disminucion"
        self.objetivo = "enemigo"

    def __str__(self):
        return str(self.__dict__)

class Energia:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase

    def __str__(self):
        return str(self.__dict__) 

energia_fuego = Energia("fuego","fuego")

coste_golpe_fuego = ["fuego"]
prob_golpe_fuego = 0
ed_golpe_fuego = [EfectoDanio(30)]
habilidad_golpe_fuego = Habilidad("golpe fuego",coste_golpe_fuego,prob_golpe_fuego, "un golpe de fuego",ed_golpe_fuego)

coste_llamarada = ["fuego"]
prob_llamarada = [1,2,3,4]
ed_llamarada = [EfectoDanio(10), EfectoAumentoDanio(40,[2,3,4])]
habilidad_llamarada = Habilidad("llamarada",coste_llamarada,prob_llamarada, "una llamarada",ed_llamarada)

habilidades_fuego = [habilidad_golpe_fuego, habilidad_llamarada]
poke1 = Pokemon("poke_fuego", "fuego", 50, habilidades_fuego)

energia_agua = Energia("agua","agua")

coste_golpe_agua = ["agua"]
prob_golpe_agua = 0
ed_golpe_agua = [EfectoDanio(20)]
golpe_agua = Habilidad("golpe agua",coste_h2,prob_h2, "desc2",ed2)

coste_burbujas = ["agua"]
prob_burbujas = [1,2,3]
ed_burbujas = [EfectoDanio(30), EfectoDisminucionDanio(30,[1,2,3,4])]
burbujas = Habilidad("burbujas",coste_burbujas,prob_burbujas, "desc2",ed_burbujas)

habilidades_agua = [golpe_agua,burbujas]
poke2 = Pokemon("poke_agua", "agua", 50, habilidades_agua)


def seleccion_habilidad(poke):
    habilidades_disponibles_imprimir = [str(habilidad) for habilidad in poke.habilidades]            
    habilidades_disponibles = [habilidad for habilidad in poke.habilidades]            
    dict_habilidades_disponibles_imprimir = dict(zip(habilidades_disponibles_imprimir,range(len(habilidades_disponibles_imprimir))))
    dict_habilidades_disponibles = dict(zip(habilidades_disponibles,range(len(habilidades_disponibles))))
    habilidades_seleccion_imprimir = {y:x for x,y in dict_habilidades_disponibles_imprimir.items()}
    habilidades_seleccion = {y:x for x,y in dict_habilidades_disponibles.items()}
    
    ok = False
    while not ok:
        print("Habilidades disponibles")
        print(habilidades_seleccion_imprimir)
        habilidad_numero_seleccion=int(input('Seleccione una habilidad:'))
        if habilidad_numero_seleccion in list(habilidades_seleccion.keys()):
            habilidades_seleccionada=habilidades_seleccion[habilidad_numero_seleccion]
            print("Habilidad seleccionada: {}".format(str(habilidades_seleccionada)))
            ok = True
            return habilidades_seleccionada
        else:
            print("Numero incorrecto de habilidad: {}".format(habilidad_numero_seleccion))
            

def aplicar_efectos(habilidad):
    efectos = ""
    if habilidad.probabilidad != 0:
        dado = random.randint(1,6)
        print("El dado salio con {}".format(dado))
        time.sleep(2)
        
        if dado in habilidad.probabilidad:
            for efecto in habilidad.efectos:
                if hasattr(efecto, 'probabilidad'):
                    dado = random.randint(1,6)
                    print("El dado salio con {}".format(dado))
                    time.sleep(2)
                    if dado in efecto.probabilidad:
                        print("Se va a aplicar {}".format(efecto))
                        efectos = str(efecto)
                else:
                    print("Se va a aplicar {}".format(efecto))
                    efectos = str(efecto)
    else:
        for efecto in habilidad.efectos:
            if hasattr(efecto, 'probabilidad'):
                dado = random.randint(1,6)
                print("El dado salio con {}".format(dado))
                time.sleep(2)
                if dado in efecto.probabilidad:
                        print("Se va a aplicar {}".format(efecto))
                        efectos = str(efecto)
            else:
                print("Se va a aplicar {}".format(efecto))
                efectos = str(efecto)

    return efectos


def duelo(poke1, poke2):
    turno=1

    while poke1.vida > 0 and poke2.vida > 0:
        
        if poke1.vida > 0:
            print("Turno de {}".format(poke1.nombre))
            time.sleep(2)

            if turno == 1:
                habilidad_seleccionada=poke1.habilidades[0]
                print("Es el turno {} de {} la habilidad es {}".format(turno, poke1.nombre, habilidad_seleccionada))
            else:
                habilidad_seleccionada=seleccion_habilidad(poke1)
                        
            efecto=aplicar_efectos(habilidad_seleccionada)
            time.sleep(2)
            print("EFECTO FINAL: {}".format(str(efecto)))

            poke2.vida = poke2.vida - int(ast.literal_eval(efecto)["danio"])
            print("{} queda con {} de vida".format(poke2.nombre, poke2.vida))

        if poke2.vida > 0:
            print("Turno de {}".format(poke2.nombre))
            time.sleep(2)

            if turno == 1:
                habilidad_seleccionada=poke2.habilidades[0]
                print("Es el turno {} de {} la habilidad es {}".format(turno, poke2.nombre, habilidad_seleccionada))
            else:
                habilidad_seleccionada=seleccion_habilidad(poke2)
                        
            efecto=aplicar_efectos(habilidad_seleccionada)
            time.sleep(2)
            print("EFECTO FINAL: {}".format(str(efecto)))

            poke1.vida = poke1.vida - int(ast.literal_eval(efecto)["danio"])
            print("{} queda con {} de vida".format(poke1.nombre, poke1.vida))
            
        turno+=1

    if poke1.vida > 0:
        print("{} gana el duelo con {} de vida".format(poke1.nombre, poke1.vida))
    else:
        print("{} gana el duelo con {} de vida".format(poke2.nombre, poke2.vida))


duelo(poke1, poke2)