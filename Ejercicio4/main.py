
from random import randint

from hash import TablaHash


if __name__ == "__main__":
    t = TablaHash(1000)
    for i in range(1000):
        t.insertar(randint(10000, 20000))
    t.mostrar()