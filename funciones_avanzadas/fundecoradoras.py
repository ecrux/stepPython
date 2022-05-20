

def monitorizar( funcion  ) :

    def decorar() :
        print("Se esta iniciando la funcion '{}' ...".format(funcion.__name__))
        funcion()
        print("Se ha finalizado la funcion '{}'".format(funcion.__name__))

    return decorar

def monitorizar_with_params( funcion  ) :

    def decorar(*args, **kwargs):
        print("Se esta iniciando la funcion '{}' ...".format(funcion.__name__))
        funcion(*args, **kwargs)
        print("Se ha finalizado la funcion '{}'".format(funcion.__name__))

    return decorar

@monitorizar
def saludar():
    print("Saludos a todos los que han llegado bienvenidos")

@monitorizar
def despedir():
    print("Esta es mi canción de despedida")

@monitorizar_with_params
def entre_charla(name):
    print("Hola a todos, especialmente para {}".format(name))



# print(globals())
# monitorizar(saludar)
# monitorizar(despedir)()
# saludar()
entre_charla("Alexa")
