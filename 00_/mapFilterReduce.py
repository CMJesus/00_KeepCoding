from functools import reduce

def doble(x):
    return x+x

#operadores. Operador map, opera sobre cada uno de los items de la lista.

#Si quisiera una función para que me devolviera en número romano, pues la función de primer nivel a ser llamada, en este caso no sería lambda, sería roman noumber por ejemplo.


lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)

#Partes de la programación funcional que podemos operar en python. map y filter. Y también reduce.

def esPar(x):
    return x % 2 == 0


#Operador filter. Me vas a filtrar de todos los que entran, me devolveras aquellos que cumplan la siguiente función. Lo que creo con firlter es un proceso de resultado true o false.
#comprueba, y si es true lo guarda.

listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 = filter(esPar, lista)


#Reduce, transforma los valores procesados en un único valor.
# reduce (lambda x, y : x+ y, l)

sumatorio = reduce(lambda x, y: + y, lista)

suma100 = reduce(lambda x, y : x+y, range(101))



print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(suma100)




