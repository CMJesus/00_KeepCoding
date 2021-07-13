from funciones1nivel import sumaTodos 

#tengo acceso a normal, cuadrado, cubo y sumatodo. O puedo seleccionar funciones de dentro del archivo.


doble = lambda x: x*2

triple = lambda x: x*3


print(sumaTodos(3, doble))
print(sumaTodos(100, triple))