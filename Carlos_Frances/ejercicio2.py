input=[2,1,2,1,3,3,4,2,4]
def function(array):
    cantidad=0 #variable a devolver que contiene la cantidad de boomerangs encontrados
    for idx,numero in enumerate(array): #Recorremos el array desde el inicio hasta su longitud -2 (para evitar errores de index out of range)
        if idx < len(array)-2:
            if array[idx+1] != numero and array[idx+2] == numero: # Si el numero actual no coincide con el siguiente pero si con el de despues, el contador de bumerangs suma
                cantidad+=1
    return cantidad
    
print(function(input))