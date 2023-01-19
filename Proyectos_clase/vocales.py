def contarVocales(palabra:str):
    palabra=palabra.lower()
    palabra=normalize(palabra) 
    max=0
    vocal=None
    for letra in palabra:
        if palabra.count(letra) > max and letra in ("a","e","i","o","u"):
            max = palabra.count(letra)
            vocal=letra
    return vocal
        
def normalize(palabra:str):
    replacements = (
        ("á","a"),
        ("é","e"),
        ("í","i"),
        ("ó","o"),
        ("ú","u")
    )
    #recorrer los replacements
    for a,b in replacements:
        palabra.replace(a,b)
        print(a)
    
    return palabra