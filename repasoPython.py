## listas
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
my_other_list = [35, 1.77, "Brais", "Moure"]
my_other_list.insert(1,"Azul")
print(my_other_list)
my_other_list.append("MoureDev")
print(my_other_list)
my_list.remove(30)
print(my_other_list)
my_other_list[1] = "azul"
my_list.clear()
my_other_list = my_list.copy
my_list.reverse()
my_list.sort()

## TUPLAS inmutables
my_tuple = tuple()
my_other_tuple = ()
my_tuple = (35,1.77,"Brais", "Moure")
my_tuple.count(35)
## DICCIONARIOS
my_dict = dict()
my_other_dict = {}

my_other_dict = {
    "Nombre": "kike",
    "Apellido": "Gar",
    "Lenguajes":{"Python","Kotlin"},
    1:"Python"
}

print(my_other_dict["Nombre"])
my_other_dict["Nombre"] = "Pedro"
print(my_other_dict["Nombre"])
my_other_dict["Calle"] = "Calle Kike"
print(my_other_dict)
del my_other_dict["Calle"]
print(my_other_dict.items())
print(my_other_dict.keys())
print(my_other_dict.values())
#print(my_other_dict.fromkeys())

my_other_dict = dict.fromkeys(("Nombre",1))

##bucles



mi_numero = 0
while mi_numero < 10:
    print(mi_numero)
    mi_numero+=1

for element in my_list:
    print(element)
    if element == "Edad":
        break
    elif element == 1:
        print("elemento vale uno")
    else:
        "Ha finalizado"
##FUNCIONES
def my_function():
    print("esta es mi funcion")

my_function()

##CLASES
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def walk (self):
        print(self.name + " esta caminando")

my_person = Person("Kike","Garcia")
print(my_person.name)
my_person.walk()


