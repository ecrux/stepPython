
# Funciones anónimas, funcion sin nombre
#


def doblar1(num) : 
    res = num * 2
    return res

# resumida un poco 
def doblar2(num) : return num * 2

# de esta manera sería lamdba
doblar3 = lambda num : num * 2

print(doblar1(10))
print(doblar2(10))
print(doblar3(10))

# reviertir una cadena en una función lambda
revertir = lambda string : string[::-1]

print(revertir("alexa"))


# map + lambda

class Persona :

    def __init__(self, name, age) : 
        self.name = name
        self.age = age

    def __str__(self) : 
        return "{} de {} años".format(self.name, self.age)


personas = [ 
    Persona("Edwar", 22),
    Persona("Alexa", 20),
    Persona("Nala", 5),
    Persona("Tiago", 2)
]

def add_age(persona):
    persona.age += 1
    return persona

# personas = map(add_age, personas)

# for persona in personas:
#     print(persona)

# personas_map = map(lambda persona : Persona(persona.name, persona.age + 1) , personas)

# for persona in personas_map:
#     print(persona)

# filter + lambda

personas_filter = filter(lambda persona : persona.age < 10 , personas)

for persona in personas_filter:
    print(persona)
