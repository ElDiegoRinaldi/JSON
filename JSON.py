import json

class Persona(object):
    nombre = None
    apellido = None
    edad = None

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


class Ciudad(object):
    def __init__(self):
        self.listaPersonas = []

    def agregarPersonas(self,unaPersona):
        self.listaPersonas.append(unaPersona)

    def crearDiccionarioPersonas(self):
        diccionario = {"personas":[]}

        for item in self.listaPersonas:
            diccionario["personas"].append({"nombre": item.nombre, "apellido": item.apellido, "edad": item.edad})

        return diccionario

Pers1 = Persona('Dario','Andreatini', 100)
Pers2 = Persona('Dari','Andreatin', 10)
Pers3 = Persona('Dar','Andreati', 1)

unaCiudad = Ciudad()
unaCiudad.agregarPersonas(Pers1)
unaCiudad.agregarPersonas(Pers2)
unaCiudad.agregarPersonas(Pers3)

elJson = json.dumps(unaCiudad.crearDiccionarioPersonas())
#f = open("archivo","w")
#f.write(elJson)
#f.close()

f = open("archivo","r")
json_archivo = f.read()
diccionario_archivo = json.loads(json_archivo)

for item in diccionario_archivo["personas"]:
    UnaPers = Persona(item["nombre"], item["apellido"], item["edad"])
    unaCiudad.agregarPersonas(UnaPers)

f.close()

