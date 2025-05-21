from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos

    @abstractmethod
    def mostrar(self):
        pass


class mostrar(receta):
    def mostrar(self):
        print(f": {self.nombre}")
        print("Ingredientes:")
        for ing in self.ingredientes:
            print(f"- {ing}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase para recetas vegetarianas
class receta_vegetariana(receta):
    def mostrar(self):
        tipo_receta = "vegetariana"
        mostrar.mostrar(self, tipo_receta)


# Clase para recetas no vegetarianas
class receta_no_vegetariana(receta):
    def mostrar(self):
        tipo_receta = "no_vegetariana"
        mostrar.mostrar(self, tipo_receta)


# Clase con utilidades del restaurante
class utilidades:
    @staticmethod
    def imprimir_receta(receta_1):
        print("====================================")
        mostrar.mostrar(receta_1)
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for l in lista:
            print(f"* {l}")

def crear_receta_vegetariana(tipo_receta):

    
    nombre = input("nombre de la receta:")
    ingredientes = []
    print("introduce los ingredientes (fin para terminar): ")
    while True:
        ing = input("- ")
        if ing.lower() == "fin":
            break
        ingredientes.append(ing)
    pasos1 = []
    print("introduce los ingredientes (fin para terminar): ")
    while True:
        paso = input("- ")
        if paso.lower() == "fin":
            break
        pasos1.append(paso)
    
    return nombre, ingredientes, pasos1
    
# Función principal
def principal():


    tipo_receta = input("¿Que tipo de receta quieres crear?(vegetariana / no_vegetariana): ").lower()
    nombre, ingredientes, pasos = crear_receta_vegetariana(tipo_receta)
    if tipo_receta == "vegetariana":
        receta_1 = receta_vegetariana(nombre, ingredientes, pasos, )
        print("== Mostrar recetas ==")
        utilidades.imprimir_receta(receta_1)

    elif tipo_receta == "no_vegetariana":
        receta_2 = receta_no_vegetariana(nombre, ingredientes, pasos)
        print("== Mostrar recetas ==")
        utilidades.imprimir_receta(receta_2)

    




# Ejecutar el programa
if __name__ == "__main__":
    principal()
