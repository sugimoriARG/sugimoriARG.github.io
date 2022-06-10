from pokemon import *
from entrenador import Entrenador
from batalla import Batalla

poke1 = Bulbasaur()
poke2 = Machop()
poke3 = Charmander()

poke4 = Squirtle()
poke5 = Machop()
poke6 = Bulbasaur()

entrenador1 = Entrenador("Entrenador1", [poke1,poke2,poke3])
entrenador2 = Entrenador("Entrenador2", [poke4,poke5,poke6])

batalla = Batalla(entrenador1, entrenador2)

batalla.iniciar()
