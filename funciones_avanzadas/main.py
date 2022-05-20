import sys
# condicionales avanzados ,

# ************************************************************************
# operaciones encadenadas ************************************************
# ************************************************************************

# 1 < 2 and 2 < 3
if ( 1 < 2 < 3):
    print( 1 < 2 < 3 )

num = 25

if(num >= 0 and num <= 100):
    print("Se encuentra entre 0 y 100")

if 0 <= num <= 100 :
    print("Se encuentra entre 0 y 100")

# Comprensión de listas

# ejercicio 1 ************************
lista = []
for letra in 'casa':
    lista.append(letra)
print(lista)

lista2 = [ letra for letra in 'casa']
print(lista2)

# erjercio 2 ************************
listaNumPotencia = []
for num in range(0,11):
    listaNumPotencia.append(num**2)
print(listaNumPotencia)

listaNumPotencia2 = [num**2 for num in range(0,11)]
print(listaNumPotencia2)

listaNumMultDos = []
for num in range(0,11):
    if num%2 == 0:
        listaNumMultDos.append(num)
print(listaNumMultDos)

listaNumMultDos = [num for num in range(0,11) if num % 2 == 0 ]
print(listaNumMultDos)

# ejercicio 3 ************************

listaNumPotencia = []
for num in range(0,11):
    listaNumPotencia.append(num**2)

pares = []
for num in listaNumPotencia : 
    if( num % 2 == 0):
        pares.append(num)
print(pares)

# lisa de pares => las potencias de rango 0 - 11
listaNumPotenciaPares = [num ** 2 for num in range(0,11) if (num ** 2) % 2 == 0]
print(listaNumPotenciaPares)
listaNumPotenciaPares2 = [num for num in [ num ** 2 for num in range(0,11) ] if num % 2 == 0]

print(listaNumPotenciaPares2)
print("El peso de listaNumPotenciaPares2 es : {}".format(sys.getsizeof(listaNumPotenciaPares2)))
print("El peso de listaNumPotenciaPares es : {}".format(sys.getsizeof(listaNumPotenciaPares)))

# ejercicio 4 ************************
# multiplos de 2,3,4 y 8 del rango 0, 501
multipliplos = [ num for num in range(0,501) if num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 8 == 0 ]
print(multipliplos)
multipliplos = [ num for num in range(0,501) if num % 2 == 0 == num % 3  and num % 4 == 0 == num % 8 ]
print(multipliplos)

# if num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 8 == 0 :
#     if num % 2 == 0 == num % 3  and num % 4 == 0 == num % 8 :
        # print("HOla")