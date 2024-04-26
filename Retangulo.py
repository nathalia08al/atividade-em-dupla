class Retangulo:
    def __init__(self, lado1, lado2, lado3, lado4):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3 + self.lado4

    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)* (s - self.lado4)) * 0.5
        return area
# Exemplo de uso:
retangulo = Retangulo(2, 4, 2, 6)
print("Perímetro do retangulo:", retangulo.calcular_perimetro())
print("Área do retangulo:", retangulo.calcular_area())