def obtenerUsuarios(texto:str):
    users=[]
    usuarios = texto.split("\n")
    for idx, dato in enumerate(usuarios):
        for idx, dato2 in enumerate(dato):
            if idx == 0 or idx % 5 == 0:
                user = {"dni": "", "nombre": "", "email": "", "telefono": 0, "experiencia": 0.0}
                user["dni"]=dato
            if idx % 1==0:
                user["nombre"] = dato
            if idx % 2==0:
                user["email"] = dato
            if idx % 3==0:
                user["telefono"] = dato
            if idx % 4==0:
                user["experiencia"] = dato.split("\n")[0]
                users.append(user)
    return users

input="01234567L;LuisGonzalez;luisgonzalez@mail.com;656343576;12.5\n71476342J;MacarenaRamirez;macarena@a.com;6943321;8"

print(obtenerUsuarios(input))