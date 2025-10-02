"""
Practica #1 Implementar Paradigma Estructurados VS OO.
Crear un programa que obtenga el area de un rectangulo.
"""
import os
os.system("cls")

#1.- Estructurado
def areaRectangulo(base,altura):
    area=base*altura
    return area

base=5
altura=6
print(f"El area del rectangulo es: {areaRectangulo(base,altura)}")

#2.- OO
class AreaRectangulo:
    def __init__(self,base,altura):
        area=self.base*self.altura
        return area
    
rectangulo=AreaRectangulo()

print(f"El area del rectangulo es:{rectangulo.areaRectangulo(5,6)}")