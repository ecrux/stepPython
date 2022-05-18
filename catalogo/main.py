
from io import open
import pickle


class Movie:

    def __init__(self, title, description, premiere, created_at):
        self.title = title,
        self.description = description
        self.premiere = premiere,
        self.created_at = created_at
        print("Created movie: {}".format(self.title))

    def __str__(self):
        return "{} ({})".format(self.title, self.premiere)


class Catalogo:

    __movies = []

    def __init__(self):
        self.loadMovies()
    
    def addMovie(self , movie):
        self.movies.append(movie)
        self.saveInFile()

    def viewMovies(self) : 
        for m in self.movies:
            print(m)
    
    def loadMovies(self):
        fileCatalogo = open("files/catalogo.pckl" , "ab+")
        fileCatalogo.seek(0)

        try:
            self.movies = pickle.load(fileCatalogo)
        except :
            print("Empty file")
        finally:
            fileCatalogo.close()
            del(fileCatalogo)
            print("Se han cargado {} peliculas".format(5))

    def saveInFile(self):
        fileCatalogo = open("files/catalogo.pckl" , "wb")
        pickle.dump(self.movies, fileCatalogo)
        fileCatalogo.close()
        # del(fileCatalogo)


    def __del__(self):
        self.saveInFile()

c = Catalogo()

# c.viewMovies()