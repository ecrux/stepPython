from io import open
import pickle

lista = [1,5,74,4,5]
print(lista)

f = open("files/lista.pckl" , "wb")
pickle.dump(lista, f)
f.close()

del(f)

f = open("files/lista.pckl" , "rb")
lista = []
print(lista)
lista = pickle.load(f)
print('lista')
print(lista)