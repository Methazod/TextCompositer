"""
Clase que crea una arista.

Jorge Manzano Anchelergues y Jaime Usero Aranda.
"""

class Edge:

    # Construye una arista
    def __init__(self, next):
        from NodeClass import Node         
        if not isinstance(next, Node):
            raise TypeError("next debe ser de la clase Node.")        
        self.weight = 1
        self.next = next

    # Getter del peso
    def getWeight(self):
        return self.weight
    
    #Getter del siguiente nodo
    def getNext(self):
        return self.next

    # Incrementa el peso de la arista en uno
    def incrementarPeso(self):
        self.weight += 1