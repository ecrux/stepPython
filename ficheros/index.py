from io import open
import sys
# import io

text = "texto para imprirmir \nEsta es la otra linea "

fichero = open("files/fichero.txt" , "w")
fichero.write(text)
fichero.close()


# print(hex(id(fichero)))
print("Este es el peso del objeto fichero antes de ser eliminado: {}".format(sys.getsizeof(fichero)))
del(fichero)
fichero = open("files/fichero.txt", "r")
text1 = fichero.read()
fichero.close()
print("Este es el fichero despues de cerrado : {}".format(sys.getsizeof(fichero)))
print(text1)

print("Este es el peso de la viriable text1 : {}".format(sys.getsizeof(text1)))
print("Este es el peso del fichero en modo lectura : {}".format(sys.getsizeof(fichero)))


