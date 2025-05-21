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
    def mostrar(self, tipo_receta):
        if tipo_receta == "vegetariana":
            print(f"Receta vegetariana: {self.nombre}")
            print("Ingredientes:")
            for ing in self.ingredientes:
                print(f"- {ing}")
            print("Pasos:")
            for paso in self.pasos:
                print(f"{paso}")
        elif tipo_receta == "no_vegetariana":
            print(f"Receta NO vegetariana: {self.nombre}")
            print("Ingredientes:")
            for ingrediente in self.ingredientes:
                print(f"- {ingrediente}")
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
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for l in lista:
            print(f"* {l}")

# Función principal
def principal():
    receta_1 = receta_vegetariana("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta_2 = receta_no_vegetariana("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    utilidades.imprimir_receta(receta_1)
    utilidades.imprimir_receta(receta_2)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ingrediente in receta_1.ingredientes:
        print(f"* {ingrediente}")
    
    print("Ingredientes de Pollo al horno:")
    for ingrediente in receta_2.ingredientes:
        print(f"* {ingrediente}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
