'''Escribe una clase llamada Poligono() que genera objetos de polígono de 3 o más lados.
Al crear un objeto, en el constructor __init__ ( ), se indica el número de lados que va a tener y
se crea una lista que va a tener ese número de elementos cuyos valores iniciales serán 0.
• La clase Poligono() tendrá un método llamado darlados( ) que le pedirá al usuario que
introduzca uno a uno los valores de todos los lados.
• La clase Polígono() tendrá otro método llamado verlados( ) que mostrará uno a uno los
valores introducidos de todos los lados.'''
class Poligono:
    def __init__(self, lados):
        self.lados = lados
        self.lista = [0] * lados

    def darlados(self):
        for i in range(self.lados):
            self.lista[i] = int(input("Introduce el valor del lado " + str(i + 1) + ": "))

    def verlados(self):
        for i in range(self.lados):
            print("Valor del lado ", i + 1, ":", self.lista[i])

'''Se va a crear una clase llamada Triangulo() que hereda de la clase Poligono(). 
Al crear un objeto triangulo, se invoca al constructor de la clase Poligono() al que se indica el 
número de lados = 3.
• La clase Triangulo() tendrá un método area( ) que calcule y muestre el área del triángulo. 
Puede ser cualquier tipo de triángulo. Puedes usar la fórmula de Herón.
• La clase Triangulo() tendrá un método perimetro( ) que calcule y muestre el perímetro del 
triángulo (suma de sus lados).'''

class Triangulo(Poligono):
    def __init__(self):
        super().__init__(3)

    def area(self):
        a, b, c = self.lista
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("El área del triángulo es:", area)

    def perimetro(self):
        a, b, c = self.lista
        perimetro = a + b + c
        print("El perímetro del triángulo es:", perimetro)

'''Crea dos objetos de la clase Triangulo() y muestra el resultado de ejecutar todos los 
métodos tanto de la clase Polígono() como de la clase Triangulo().'''

triangulo1 = Triangulo()
triangulo1.darlados()
triangulo1.verlados()
triangulo1.area()
triangulo1.perimetro()

triangulo2 = Triangulo()
triangulo2.darlados()
triangulo2.verlados()
triangulo2.area()
triangulo2.perimetro()

