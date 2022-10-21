
from random import randint

from hash import TablaHash

if __name__ == "__main__":

    tabla = TablaHash(100)
    
    for i in range(100):
        tabla.insertar(randint(10000, 20000))
    tabla.mostrar()
    print('listas con claves sinonimas')
    tabla.longitudClavesSinonimas()
    tabla.variacionCantLongitudLista()

    