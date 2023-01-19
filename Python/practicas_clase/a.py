"""input:str="GUadAlUPéüáá"

def getVocal(param:str):
    dict={"á":"a",
      "é":"e",
      "í":"i",
      "ó":"o",
      "ú":"u",
      "ü":"u"}
    vocales=["a","e","i","o","u"]
    resultado=0
    letramax=""
    param=param.lower()
    for letra in dict:
        if letra in param:
            param=param.replace(letra,dict[letra])
    for letra in vocales:
        if param.count(letra) > resultado:
            resultado=param.count(letra)
            letramax=letra
            
    if resultado==0:
        resultado=None
    return [resultado,letramax]

print(getVocal(input))"""
print(1<2)
