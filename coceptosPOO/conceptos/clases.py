import random


class materia:

    def __init__(self,nombre: str,creditos: int):
    self.nombre:str = nombre
    self.creditos: int = creditos






class Estudiante:

    def __init__(self,nombre: str,edad: int,nota_prom: float):
        self.nombre: str = nombre
        self.edad:int = edad
        self.nota_prom:float = nota_prom
        self.materia: list[materia] = []

        def matricular_materia(self, nombre_materia: str, creditos: int):
            materia:materia = materia(nombre_materia, creditos)
            self.materias.append(materia)


    def cambiar_nota(self) -> float:
        n = random.randint(1, 10)
        if n > 5:
            self.nota_prom += 0.5
        else:
            self.nota_prom -= 0.5

        return self.nota_prom





if __name__ == "__main__":
    e1:Estudiante = Estudiante("juan", 18, 3.5)
    e2:Estudiante = Estudiante("juan", 18, 3.5)
    e3:Estudiante = Estudiante("maria", 18, 4.0)

   # print(e1 == e2)
    # print(e1.nombre == e2.nombre and e1.edad == e2.edad and e1.nota_prom == e2.nota_prom)
    # print(e1)
    # print(e2)



    print(e2.nota_prom)
    e2.cambiar_nota()
    print(e2.nota_prom)



    print(e3.nota_prom)
    e3.cambiar_nota()
    print(e3.nota_prom)

    e1.matricular_materia("apoo", 3)
    e1.matricular_materia("procesos de negocios", 3)

    print(len(e1.materias))
     print(e1.materia[1].nombre)













