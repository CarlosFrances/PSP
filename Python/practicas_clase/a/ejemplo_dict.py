input_param ="roberto;martinez\ngonzalo;gonzalez\nteodoro;fernandez"

def function(param:str):
    #Definimos el diccionario resultado
    result = {} #dict()
    #separar cada linea
    personas = param.split("\n")
    for persona in personas:
        nombre=persona.split(";")[0]
        apellido=persona.split(";")[1]
        
        result[nombre] = apellido #añadir clave y valor al diccionario
    return result
    
"""def function(param:str):
    #Definimos el diccionario resultado
    result = {} #dict()
    #separar cada linea
    personas = param.split("\n")
    for persona in range(len(personas)):
        nombre=persona.split(";")[0]
        apellido=persona.split(";")[1]
        
        result[nombre] = apellido #añadir clave y valor al diccionario
    return result"""
    
    
"""def function(param:str):
    #Definimos el diccionario resultado
    result = {} #dict()
    #separar cada linea
    personas = param.split("\n")
    for idxin in enumerate(personas):
        nombre=persona.split(";")[0]
        apellido=persona.split(";")[1]
        
        result[nombre] = apellido #añadir clave y valor al diccionario
    return result"""
        
print(function(input_param))