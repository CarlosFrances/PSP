#variables globales de posicion
x=0
y=0

def robot(direccion):
    numeroDirecciones=0
    global x
    global y
    for paso in direccion:
        #valoramos hacia donde está mirando el robot
        #y sumamos o restamos en consecuencia
        if numeroDirecciones % 4 == 0:
            y=y+paso
            numeroDirecciones+=1
        elif numeroDirecciones % 4 == 1:
            x=x-paso
            numeroDirecciones+=1
        elif numeroDirecciones % 4 == 2:
            y=y-paso
            numeroDirecciones+=1
        elif numeroDirecciones % 4 == 3:
            x=x+paso
            numeroDirecciones+=1
    
    #esta linea equivale a girar el robot 90º
    numeroDirecciones+=1
        
    return "[x:"+str(x)+",y:"+str(y)+"]" 