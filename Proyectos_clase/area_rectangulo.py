class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura

rectangulo = Rectangulo(8,3)
print(rectangulo.area())