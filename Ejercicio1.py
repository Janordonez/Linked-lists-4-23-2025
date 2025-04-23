class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def insertarInicio(self, dato):
            nodo = Nodo(dato)
            nodo.siguiente = self.cabeza
            self.cabeza = nodo

    def imprimirPrimero(self):
        if self.cabeza is not None:
            return print(self.cabeza.valor)
            
    def cantidadNodos(self):
        Contador = 0
        Temporal = self.cabeza
        if self.cabeza is not None:
            while Temporal:
                Temporal = Temporal.siguiente
                Contador += 1
        return Contador

    def sumarEnteros(self):
        acumulador = 0
        Temporal = self.cabeza
        if self.cabeza is not None:
            while Temporal:
                acumulador += Temporal.valor
                Temporal = Temporal.siguiente
            return acumulador
    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
"""Esta línea asegura que el siguiente bloque solo se ejecuta si el archivo se corre directamente, y no cuando es importado como módulo en otro archivo"""
if __name__ == "__main__":
    lista = ListaEnlazada()  #Creando el objeto lista
    
    
    while True:
        lista.insertar(int(input("Digite un numero a insertar:")))
        opc = input("Digite si desea ingresar otro numero (Y/N):")
        if opc == "n" or opc == "N":
            break;

    
    lista.insertarInicio(100)
    lista.insertar(10)
    lista.insertar(20)
    lista.insertar(30)
    lista.insertar(40)
    lista.imprimir()  # Lista: 10 -> 20 -> 30 -> 40 -> None
    print("Buscando el valor 20", lista.buscar(20))  # True
    print("Buscar el número 50?", lista.buscar(50))  # False
    lista.eliminar(30)
    lista.imprimir()  # Lista: 10 -> 20 -> 40 -> None
    lista.eliminar(10)
    lista.imprimir()  # Lista: 20 -> 40 -> None
    lista.imprimir()  # Lista: 20 -> 40 -> None


    print(lista.cantidadNodos())
    print(lista.sumarEnteros())
    lista.imprimirPrimero()

"""
-	Modifica el programa para que realice:

o	Leer los datos que se insertarán en la lista.
o	Implementar inserción al inicio.
o	Agregar método cantidadNodos() que cuente los nodos de la lista.
o	Método que sume los valores enteros de la lista.
o	Agregar método que imprima el primer valor de la lista.

-	Investiga: Listas doblemente enlazadas
o	Proporciona un ejemplo
"""