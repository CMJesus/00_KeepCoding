#Bloque de código que tiene un nombré, y debe de tener un parámetro aparejado para ejecutarse (La Función). Funciones como parámetro de entrada. También puede haber funciones que devuelven
#funciones.

def normal(i):
    return i

def cuadrado(x):
    return x * x

def cubo(x):
    return x**3


def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)

    return resultado

if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cuadrado))
else:
    print(__name__)