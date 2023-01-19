

#input="01234567L;LuisGonzalez;luisgonzalez@mail.com;656343576;12.5\n71476342J;MacarenaRamirez;macarena@a.com;6943321;8"

def function(string:str):
    texto=string.split("\n") #Dividir el texto en personas (siempre separadas con un \n)
    dict_nif={}
    for persona in texto:       
        dict_persona={}
        datos=persona.split(";") #Dividir cada persona en sus diferentes datos(siempre separados con un ;)
        #Declaracion de variables para guardar los datos de la persona (salvo el nif que estará un nivel por encima)
        nif=None
        nombre=None
        email=None
        telefono=None
        descuento=None
        for idx,dato in enumerate(datos): 
            #Iteramos sobre cada uno de los datos y los guardamos en sus respectivas variables
            #Diferenciamos el dato a guardar en funcion del indice
            if idx == 0:
                nif=dato
            if idx == 1:
                nombre=dato
            if idx == 2:
                email=dato
            if idx == 3:
                telefono=dato
            if idx == 4:
                descuento=dato
        #Añadimos los datos al diccionario correspondiente a la persona con nif X
        dict_persona["nombre"] = nombre
        dict_persona["email"] = email
        dict_persona["telefono"] = telefono
        dict_persona["descuento"] = descuento
        #Añadimos el diccionario con los datos de la persona al diccionario de nifs
        dict_nif[nif] = dict_persona
    return dict_nif