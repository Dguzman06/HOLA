import math

class Punto:
    def __init__(self,x:int,y:int):
        self.x: int = x
        self.y: int = y


    def mostrar(self,x:int, y:int):
        print("coordenadas:", Punto.x,  "," , Punto.y)

    def mover(self,n_x:int,n_y:int):
        self.x: int = n_x
        self.y: int = n_y
        print("el punto se movio a las cordenadas ",self.x,self.y)


    def cal_distancia(self,azar_punto: int):
        distancia:math.sqrt((self.x-azar_punto.x)**2 + (self.y-azar_punto.y)*+2)
        return distancia

if __name__ == "__main__":
    pun1 =  Punto(4, 7)
    pun2 =  Punto(5, 9)

    print("coordenadas",    Punto.x,",",    Punto.y)

    pun2.mover(11, 13)

    distancia = pun1.calcular_distancia(pun2)
    print("distancia entre los puntos:", distancia)













