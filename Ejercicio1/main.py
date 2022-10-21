
from random import randint, random
from hash import TablaHash


if __name__ == "__main__":

    tabla = TablaHash(1000)
    for i in range(1000):
        tabla.insertar(randint(10000, 20000))
    tabla.mostrar()
    #print(f'Longitud de pruebas {tabla.busqueda()}')



