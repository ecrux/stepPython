

def pares(n):
    for num in range(n+1):
        if num % 2 == 0:
            yield num

def tupla_potencia(n):
    for num in range(1 , n + 1):
        yield (num , num**2)

lista = [num for num in pares(10)]
print(lista)

lista2 = [num for num in tupla_potencia(10)]
print(lista2)