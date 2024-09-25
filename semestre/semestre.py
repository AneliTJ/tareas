from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint


class Semestre:
    id_semestre: str
    numero: int
    id_carrera: str 
    materias: List [Materia]
    grupos: List [Grupo]

    def __init__(self, numero:int, id_carrera:str):
        self.id_semestre= self.generar_id_semestre(numero)
        self.id_carrera = id_carrera


    def generar_id_semestre(self, numero_semestre:int)-> str:
        return f"{numero_semestre}-{randint(0,100000)}-{randint(0, 100000)}"
