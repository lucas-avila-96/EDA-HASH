
from random import randint


class TablaHash:
    __tabla = []
    __tamano = None

    def __init__(self, tamano):
        self.__tamano =  self.primoCercano(int(tamano // 0.7))
        self.__tabla = [None] * self.__tamano
        self.__incremento = randint(2, 3)
    
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
    

    def hash(self, valor):
        return valor % self.__tamano

    def insertar(self, valor):
        pos = self.hash(valor)
        if self.__tabla[pos] == None:
            self.__tabla[pos] = valor
        else:
            while self.__tabla[pos] != None:
                pos = pos + self.__incremento
            self.__tabla[pos] == valor

    def mostrar(self):
        for i in self.__tabla:
            print(i)
                