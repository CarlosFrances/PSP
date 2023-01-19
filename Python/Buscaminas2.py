
import random
import os

#Generamos un campo cuadrado aleatorio de entre 5 y 9 casillas
rand = random.randint(5,9)

#Declaramos los diferentes contadores que vamos a necesitar para contabilizar datos
contadorMinas=0
contadorMinasEncontradas=0
contadorMinasExcavadas=0

#Creación de la matriz de booleanos que marcará donde hay o no minas 
matriz = [[False for i in range(rand)] for j in range(rand)]

for i in range(rand**2//6): #Fórmula para escalar las minas (si se desea implementar diferentes dificultades, hay que cambiarla)
    while True: 
        #Mediante este bucle nos aseguramos de que no aparezcan minas en lugares repetidos
        x=random.randint(0,rand-1)
        y=random.randint(0,rand-1)
        if matriz[x][y] == False:
            matriz[x][y]=True
            contadorMinas+=1
            break
        else:
            continue


#Generamos una matriz visual que represente nuestro progreso en el juego
matrizVis = [['- ' for i in range(rand)] for j in range(rand)]

#Método para printear la matriz visual con números que sirvan para localizar las coordenadas
def printMatrizVis():
    con=0
    for i in range(rand):
        for j in range(rand):
            if j == 0:
                print(con,end="  ")
            print(matrizVis[i][j], end=" ")
        con+=1
        print()
    for i in range(0,rand):
        if i == 0:
            print("   "+str(i),end="")
        else: 
            print("  "+str(i),end="")
    print()
        

#Método para determinar si la casilla que elegimos tiene o no una mina
def buscarMina(x,y,z):
    for i in matriz:
        if matriz[int(x)][int(y)] == False:
            matrizVis[int(x)][int(y)] = str(z)+" "
        else:
            matrizVis[int(x)][int(y)] = 'X '
        
#Método para determinar si la casilla existe o no dentro de la cuadrícula 
#(util a la hora de buscar las minas para evitar errores de índice)
def isValido(x,y):
    if x >= 0 and x < rand and  y >= 0 and y < rand:
        return True
    else:
        return False

#Método para representar cuantas bombas rodean a la casilla elegida
def numerarCasillas(x,y):
    contador=0
    if isValido(x-1,y):
        contador+=matriz[x-1][y]
    if isValido(x+1,y):
        contador+=matriz[x+1][y]
    if isValido(x,y+1):
        contador+=matriz[x][y+1]
    if isValido(x,y-1):
        contador+=matriz[x][y-1]
    if isValido(x-1,y+1):
        contador+=matriz[x-1][y+1]
    if isValido(x-1,y-1):
        contador+=matriz[x-1][y-1]
    if isValido(x+1,y+1):
        contador+=matriz[x+1][y+1]
    if isValido(x+1,y-1):
        contador+=matriz[x+1][y-1]
    return contador

#Bucle de juego
while True:
    #Siempre se borra la pantalla al principio
    os.system("cls")
    
    #Contador de minas, minas encontradas y printeo de la matriz visual
    print("Minas: "+str(contadorMinas))
    print("Encontradas: "+str(contadorMinasEncontradas))
    printMatrizVis()
    
    #Recogemos las coordenadas en las que quiere buscar el usuario
    x = int(input("posicion en x: "))
    y = int(input("posicion en y: "))
    
    #Con este código podemos marcar una coordenada donde creamos que hay una mina 
    # (y de paso nos aseguramos de que esta marca se puede quitar)
    if matrizVis[int(x)][int(y)] == "P ":
        quitarBandera=input("¿Deseas quitar la bandera?: (t/f)")
        if quitarBandera == "t":
           matrizVis[int(x)][int(y)] = '- ' 
           contadorMinasEncontradas-=1
           continue
        else:
            continue
    #Aquí es donde le preguntamos al usuario si quiere colocar la banderita o cavar en la coordenada
    m = input("¿mina? (t/f): ")
    if m=="t":
        matrizVis[int(x)][int(y)] = 'P ' # "P" simboliza una banderita (no se me ha ocurrido nada mejor :))
        contadorMinasEncontradas+=1
        continue
    #Esta es la parte del código en la que determinamos si hemos cavado una mina o no 
    # (y de paso informamos de que la coordenada ya ha sido excavada o no. Esto es útil para el contador de minas excavadas)
    else:
        if matrizVis[x][y] == '- ':
            buscarMina(x,y,numerarCasillas(x,y))
            contadorMinasExcavadas+=1
        else:
            print("casilla ya excavada")
            input()
            continue
    
    #Si hemos cavado en las coordenadas de una mina, el juego termina con una estrepitosa explosión
    if matriz[int(x)][int(y)] == True:
        os.system("cls")
        printMatrizVis()
        print("BUUUM")
        break
    
    #Si hemos desenterrado todas las coordenadas que no son mina, habremos ganado con un tremendo aplauso
    if ((rand**2) - contadorMinasExcavadas) == contadorMinas:
        os.system("cls")
        printMatrizVis()
        print("ENHORABUENA!!")
        break