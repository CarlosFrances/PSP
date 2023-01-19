import math #importar la libreria que necesitamos para pi

class Circulo: #Declaración de la clase
    def __init__(self,radio): #Constructor dela clase (solo contiene el parámetro radio)
        self.radio=radio
    def get_area(self): #Método para obtener el área del círculo
        return math.pi * self.radio**2
    def get_perimeter(self): #Método para obtener el perímetro del círculo
        return 2 * math.pi * self.radio