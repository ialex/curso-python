#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys
import math
import timeit
from time import time


def timed(f):
  def wrapper(*args, **kwargs):
    start = time()
    print "Iniciamos a ejecutar la funcion %s" % f.__name__
    result = f(*args, **kwargs)
    finish = time() - start
    print "%s tarda %d segundos" % (f.__name__, finish)
    return result
  return wrapper


@timed
def main(numero):

        # Generamos una lista con el 2 y todos los impares que hay entre 3
        # y el numero que pedimos arriba
        lista = [2] + range(3, numero, 2)
       
        # Iteramos la lista y vemos que cada numero sea primo, con los primos
        # formamos una nueva lista
        primos = [n for n in lista if all([n % p for p in xrange(2, int(math.sqrt(n)+1))])]

        #primos = []
        #for n in lista:
        #    pl = []
        #    for p in  xrange(2, int(math.sqrt(n)+1)):
        #        if n % p:
        #            pl.append(True)
        #        else:
        #            pl.append(False)
        #    if all(pl):
        #        primos.append(n)
                    

        # Sumamos la lista de primos
        suma = reduce(lambda x, y : x + y, primos)
     
        print '\nHay %d numeros primos de 0 a %d, la suma de los numeros primos es: %d' % (len(primos), numero, suma)


if __name__ == "__main__":


    # Obtenemos el numero (2 millones por ejemplo)
    try:
        numero = int(sys.argv[1])
    except IndexError:
        print '\nUsar: python %s <numero>' % sys.argv[0]
        sys.exit()


    main(numero)


