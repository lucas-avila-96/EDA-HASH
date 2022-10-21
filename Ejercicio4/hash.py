

import numpy as np
from bucket import Bucket


class TablaHash:
    __tabla = None
    __total = 0
    __contadorOverflow = 0
    __almcPrimario = None

    def __init__(self, tamano):
        self.__almcPrimario = self.primoCercano(tamano // 10)
        self.__contadorOverflow = self.__almcPrimario
        self.__total = self.__almcPrimario + int((30 * self.__almcPrimario) // 100)
        self.__tabla = np.empty(self.__total, dtype=Bucket)
        for i in range(self.__total):
            self.__tabla[i] = Bucket(10)

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
    
    def extraccion(self, n):
        return int(str(n)[-2:])

    def modulo(self, valor):
        return valor % self.__almcPrimario

    def insertar(self, clave):
        ext = self.extraccion(clave)
        if ext < 10:
            pos = ext
        else:
            pos = self.modulo(ext)
        if not self.__tabla[pos].lleno():
            self.__tabla[pos].agregar(clave)
        else:
            if self.__tabla[self.__contadorOverflow].lleno():
                self.__contadorOverflow += 1
                self.__tabla[self.__contadorOverflow].agregar(clave)
            if self.__contadorOverflow == self.__total:
                print('tabla llena')


    
    def mostrar(self):
        for i in range(len(self.__tabla)):
            print(f'{i} --> {self.__tabla[i]}')


