## Diagonal doble en // para redondear para abajo


x=11
y=2

#print(x%y) #Division de residuo
#print(x**y) #elevar

# Si la funcion no devuelve un valor es un metodo
# Las tuplas son inmutables

tupla = (27,12,13,14,15,16,1,2,3,4,5)
tupla2 = tupla[:5] #cuando no va nada toma por defecto el cero
tupla2 = tupla[5:] #cuando no va nada a la derecha toma por defecto el final

# Indice inicial es cero aunque se puede cambiar
print(tupla2)

dic1 = {"adry": 35, "otro": 36 , "otr mas": 38}

class Persona:
    cabello = True
    cCabello = "defecto"
    hambre = 0

    # Constructor (inicializador)
    def __init__(self, nBrazos, nPiernas):
        self.nBrazos = nBrazos
        self.nPiernas = nPiernas

    def nadar(self): #Metodo de instancia, se necesita colocar el self
        print("Estoy nadando")


    def dormir ():
        pass
    def comer(self):
        self.hambre = 5

class Hombre(Persona):
    nombre = "defecto"
    sexo = "M"

    def cambiarNombre(self, nombre):
        self.nombre = nombre

class Mujer(Persona):
    nombre = "defecto"
    sexo = "F"



Adry = Mujer(2,3)

print(Adry.cabello)
Adry.nadar() # Se puede usar en un objeto ya creado


print("------------------")

class Persona1:
    def __init__(self) -> None:
        pass

    def despedir(self):
        print("adios")

    def brincar(self):
        print("brinco")

    @classmethod
    def correr(cls):
        print("corro")

    @staticmethod
    def nadar():
        print("nado")

    @classmethod #Decorador
    def saludar(cls, nombre): #metodo de clase cls
        print("Estoy saludando, soy" , nombre)

Persona1.saludar("Adriana") #Se usa el metodo sin instanciar un objeto

Adriana = Persona1()
Adriana.nadar() # Es como una funcion, pero cambia en que esta relacionado con la clase

print("------------------")
#Metodos especiales

class Clase:

    def __new__(cls): #Sirve para personalizar las instancias a las clases
        print("New")
        return super().__new__(cls) #Hace que imprima tambien el init

    def __init__(self): #Instancia inicial a una clase
        print("Init")

c = Clase()

print("------------------")

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @property
    def area(self):
        return 3.1416 * (self.radio**2)
    
c = Circulo(10)
print(c.area)

print("------------------")

class Perro:
    def avanzar(self):
        print("Cuatro patas")

class Perico:
    def avanzar(self):
        print("Volar")


def mover(animal):
    animal.avanzar()

perro = Perro()
perico = Perico()


#perro.avanzar()
#perico.avanzar()

mover(perro)