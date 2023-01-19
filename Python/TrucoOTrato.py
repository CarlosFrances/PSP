#Declaración de variables
import random
import string
from tokenize import Double
from xmlrpc.client import boolean


nombre=string
edad=int
altura=int
tt=string #truco o trato
trucos=["fantasma","araña","telaraña","calabaza"]
tratos=["cookie","caramelo","piruleta","helado"]
contador=0
rand=int


personas=[]

#Recoger datos de las personas
for i in range(2):
    nombre=input("Nombre: ")
    edad=input("Edad: ")
    altura=input("Altura: ")
    personas.append([nombre,edad,altura])
    
#truco o trato
tt=input("Truco o Trato? (t/tr):")

#método para sacar datos segun truco o trato
def sacarDatos(x:boolean):
    if x:
        for i in range(contador):
            rand=random.randint(0,3)
            print(trucos[rand])
    
    else:
        for i in range(contador):
            rand=random.randint(0,3)
            print(tratos[rand])        

#si queremos truco, haremos estos calculos
if tt=="t":
    for i in personas:
        contador+=(len(i[0]))//2#contador += tamaño de todos los nombres
        if int(i[1])%2==0:#contador+=1 si la edad es par
            contador+=1
        contador+=int(i[2])//100#contador+=1 por cada 100 cm
    sacarDatos(True)


#Si queremos trato, haremos estos
if tt=="tr":
    for i in personas:
        contador+=len(i[0])
        if int(i[1])//3 > 10:
            contador+=3
        else:
            contador+=int(i[1])//3
        if int(i[2])//50 > 3:
            contador+=6
        else:
            contador+=int(i[2]//50)*2
    sacarDatos(False)
            
        
    
    
        