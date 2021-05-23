import random
import time

class Pokemon:

    def __init__(self, nombre, clase, vida, habilidades):
        self.nombre = nombre
        self.clase = clase
        self.vida = vida
        self.habiliddes = habilidades
 

class Habilidad:
    
    def __init__(self, nombre, costes, probabilidad, descripcion, efectos):
        self.nombre = nombre
        self.costes = costes
        self.probabilidad = probabilidad
        self.descripcion = descripcion
        self.efectos = efectos

class EfectoDanio:

    def __init__(self, danio):
        self.danio = danio

class EfectoAumentoDanio:

    def __init__(self, danio, probabilidad):
        self.danio = danio
        self.probabilidad = probabilidad

class Energia:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase
        

energia_fuego = Energia("fuego","fuego")

coste_golpe_fuego = ["fuego"]
prob_golpe_fuego = [1,2,3]
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
prob_h2 = [1,2,3,4]
ed2 = [EfectoDanio(20)]
h2 = Habilidad("golpe agua",coste_h2,prob_h2, "desc2",ed2)
habilidades_agua = [h2]
poke2 = Pokemon("poke_agua", "agua", 50, habilidades_agua)

while poke1.vida > 0 and poke2.vida > 0:

    if poke1.vida > 0:
        print("Turno de {}".format(poke1.nombre))
        time.sleep(2)



        dado = random.randint(1,6)
        print("El dado salio con {}".format(dado))
        time.sleep(2)
        
        if dado in poke1.habiliddes[1].probabilidad:
            danio = poke1.habiliddes[1].efectos[0].danio
            print("{} lanza {} por {} de danio".format(poke1.nombre, poke1.habiliddes[1].nombre, danio))
            time.sleep(2)
            
            if hasattr(poke1.habiliddes[1], 'probabilidad'):
                dado = random.randint(1,6)
                print("El dado salio con {}".format(dado))
                time.sleep(2)
                
                if dado in poke1.habiliddes[1].probabilidad:
                    danio = poke1.habiliddes[1].efectos[1].danio
                    print("{} lanza {} por {} de danio".format(poke1.nombre, poke1.habiliddes[1].nombre, danio))
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

        if dado in poke2.habiliddes[0].probabilidad:
            danio = poke2.habiliddes[0].efectos[0].danio

            print("{} lanza {} por {} de danio".format(poke2.nombre, poke2.habiliddes[0].nombre, danio))
            time.sleep(2)

            poke1.vida = poke1.vida - danio
            print("{} es dañado con {} y le queda {} de vida".format(poke1.nombre, danio, poke1.vida))
            time.sleep(2)

if poke1.vida > 0:
    print("{} gana el duelo con {} de vida".format(poke1.nombre, poke1.vida))
else:
    print("{} gana el duelo con {} de vida".format(poke2.nombre, poke2.vida))
