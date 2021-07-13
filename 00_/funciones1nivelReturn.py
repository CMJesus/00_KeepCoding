#Funciones de primer nivel, función es un bloque de código con nombre (anónimas lambda)
#que se ejecutan sobre funciones. Función es de nivel superior si admite como parámetros opciones (entrada o salida), o su resultado es una función, o, cumple ambas.

def maxi(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
    return m



def mini(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
    return m


def media(*l):
    if len(l) == 0:
        return 0
     
    suma = 0
    for valor in l:
        suma += valor
        
    return suma / len(l)


funciones = {
    'max' : maxi,
    'min' : mini,
    'med' : media
}



def returnF(nombre):
    if nombre.lower()in funciones.keys():
        return funciones[nombre]
    
    return None


    



