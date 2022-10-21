

import numpy as np
from src.Lista import Lista


class TablaHash:
    __tabla = []
    __tamano = None
    def __init__(self, tamano):
        self.__tamano = self.primoCercano(int(tamano / 0.7))
        self.__tabla = np.empty(self.__tamano, dtype=Lista)
        for i in range(self.__tamano):
            self.__tabla[i] = Lista()
    
    def esPrimo(self, num):
        primo = False
        for n in range(2, num):
            if num % n == 0:
                primo = False
                break
            else:
                primo = True
        return primo
    
    def primoCercano(self, n):
        while not self.esPrimo(n + 1):
            n += 1
        return n + 1 

    def plegado(self, valor):
        pos = 0
        valor = list(str(valor))
        while len(valor) > 1:
            str_1 = str(valor.pop())
            str_2 = str(valor.pop())
            str_concat = str_2 + str_1
            int_concat = int(str_concat)
            pos += int_concat
        else:
            if len(valor) > 0:
                pos += int(valor.pop())
        return pos % self.__tamano

    def insertar(self, valor):
        pos = self.plegado(valor)
        self.__tabla[pos].insertarAlFinal(valor)

    def mostrar(self):
        for i in range(len(self.__tabla)):
            print(f'{i} --> {self.__tabla[i]}')

    def longitudClavesSinonimas(self):
        for i in range(len(self.__tabla)):
            if self.__tabla[i].getTamano() > 1:
                print(f'{i} --> {self.__tabla[i].getTamano()}')

    def variacionCantLongitudLista(self):
        exceso = 0
        defecto = 0
        for i in range(len(self.__tabla)):
            if self.__tabla[i].getTamano() > 3:
                exceso +=1
            else:
                defecto +=1
        return (exceso, defecto)

                
    def promedio(self):
        sum = 0
        cont = 0
        for i in range(len(self.__tabla)):
            if self.__tabla[i].getTamano() > 1:
                sum += self.__tabla[i].getTamano()
                cont += 1
        return sum/cont


