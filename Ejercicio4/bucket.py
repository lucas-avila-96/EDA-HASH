import numpy as np
from sqlalchemy import BigInteger

class Bucket:
    __contador = 0
    __arreglo = None

    def __init__(self, n):
        self.__contador = 0
        self.__arreglo = np.empty(n, dtype=int)
        for i in range(len(self.__arreglo)):
            self.__arreglo[i] = 0
        
    def agregar(self, valor):
        self.__arreglo[self.__contador] = valor
        self.__contador += 1

    def lleno(self):
        if self.__contador == len(self.__arreglo):
            return True
        else:
            return False

    def __str__(self):
        out = ''
        for i in range(len(self.__arreglo)):
            out += str(self.__arreglo[i]) + '-->'
        return out
