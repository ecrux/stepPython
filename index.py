from saluda import modulo

saluda()


class Pelicula :
    def __init__(self , title , duration , created_at) : 
        self.title = title
        self.duration = duration 
        self.created_at = created_at
        print("Se ha creado la pelicula" , self.title)
    
    def __str__(self):
        return '{} ({})'.format(self.title , self.created_at)


class Catalogo : 
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def add_pelicula(self, p):
        self.peliculas.append(p)

    def mostrar_peliculas(self):
        for p in self.peliculas:
            print(p)

p = Pelicula("John Wick", 120, 2014)
c = Catalogo([p])

c.add_pelicula(Pelicula("John Wick 2", 125, 2019))

c.mostrar_peliculas()