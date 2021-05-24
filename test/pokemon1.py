import random
import time

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
        
        return "Habilidad {} con coste {}, probabilidad {} y efectos {}".format(self.nombre, self.costes, self.probabilidad, descripcion_efectos) 

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
coste_h2 = ["agua"]
prob_h2 = 0
ed2 = [EfectoDanio(20)]
h2 = Habilidad("golpe agua",coste_h2,prob_h2, "desc2",ed2)
habilidades_agua = [h2]
poke2 = Pokemon("poke_agua", "agua", 50, habilidades_agua)


def seleccion_habilidad(poke):
    habilidades_disponibles = [str(habilidad) for habilidad in poke.habilidades]            
    my_dict1 = dict(zip(habilidades_disponibles,range(len(habilidades_disponibles))))
    habilidades_seleccion = {y:x for x,y in my_dict1.items()}
    
    ok = False
    while not ok:

        print(habilidades_seleccion)
        habilidad_numero_seleccion=int(input('Seleccione una habilidad:'))
        if habilidad_numero_seleccion in list(habilidades_seleccion.keys()):
            habilidades_seleccionada=habilidades_seleccion[habilidad_numero_seleccion]
            print("Habilidad seleccionada: ".format(habilidades_seleccionada))
            ok = True
            return habilidades_seleccionada
        else:
            print("Numero incorrecto de habilidad: {}".format(habilidad_numero_seleccion))
            

def aplicar_efectos(habilidad):
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
                else:
                    print("Se va a aplicar {}".format(efecto))
    else:
        for efecto in habilidad.efectos:
            if hasattr(efecto, 'probabilidad'):
                dado = random.randint(1,6)
                print("El dado salio con {}".format(dado))
                time.sleep(2)
                if dado in efecto.probabilidad:
                        print("Se va a aplicar {}".format(efecto))
            else:
                print("Se va a aplicar {}".format(efecto))


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
            print("EFECTO FINAL: ".format(efecto))
            
            '''
            if dado in poke1.habilidades[1].probabilidad:
                danio = poke1.habilidades[1].efectos[0].danio
                print("{} lanza {} por {} de danio".format(poke1.nombre, poke1.habilidades[1].nombre, danio))
                time.sleep(2)
                
                if hasattr(poke1.habilidades[1], 'probabilidad'):
                    dado = random.randint(1,6)
                    print("El dado salio con {}".format(dado))
                    time.sleep(2)
                    
                    if dado in poke1.habilidades[1].probabilidad:
                        danio = poke1.habilidades[1].efectos[1].danio
                        print("{} lanza {} por {} de danio".format(poke1.nombre, poke1.habilidades[1].nombre, danio))
                        time.sleep(2)


                poke2.vida = poke2.vida - danio
                print("{} es dañado con {} y le queda {} de vida".format(poke2.nombre, danio, poke2.vida))
                time.sleep(2)


        if poke2.vida > 0:
            
            print("Turno de {}".format(poke2.nombre))
            time.sleep(2)
            dado = random.randint(1,6)    
            print("El dado salio con {}".format(dado))
            time.sleep(2)

            if dado in poke2.habilidades[0].probabilidad:
                danio = poke2.habilidades[0].efectos[0].danio

                print("{} lanza {} por {} de danio".format(poke2.nombre, poke2.habilidades[0].nombre, danio))
                time.sleep(2)

                poke1.vida = poke1.vida - danio
                print("{} es dañado con {} y le queda {} de vida".format(poke1.nombre, danio, poke1.vida))
                time.sleep(2)
        '''
        turno+=1

    if poke1.vida > 0:
        print("{} gana el duelo con {} de vida".format(poke1.nombre, poke1.vida))
    else:
        print("{} gana el duelo con {} de vida".format(poke2.nombre, poke2.vida))


duelo(poke1, poke2)