#Carlos Francés Sánchez
romanos = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def convertir(letras):
    anterior=0
    total=0
    reserva=0
    for i,letra in enumerate(letras)-1:
        if romanos[letra] < romanos[letras[i+1]]:
            total-=romanos[letra]
        else:
            total+=romanos[letra]
        
print(convertir("IIX"))