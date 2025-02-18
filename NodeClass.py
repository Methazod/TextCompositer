"""
Clase Nodo que crea sus metodos y atributos.

Jorge Manzano Anchelergues y Jaime Usero Aranda.
"""

class Node:

    # Constructor que crea un Nodo.
    def __init__(self, palabra: str, id: int):                
        if not isinstance(palabra, str):
            raise TypeError("La palabra debe ser de tipo 'string'.")        
        self.listEdge = []
        self.palabra = palabra
        self.id = id

    # Getter de una Arista de listEdge
    def getEdge(self, indice: int):
        return self.listEdge[indice]

    # Getter de la lista de Aristas
    def getListEdge(self):
        return self.listEdge
    
    # Devuelve la arista con mas peso de la lista
    def getMaxEdge(self):        
        import random
        if(len(self.listEdge) != 0):
            max = []
            for arista in self.listEdge:
                if(len(max) == 0):
                    max.append(arista)                    
                else:
                    if(arista.getWeight() == max[0].getWeight()):
                        max.append(arista)
                    elif(arista.getWeight() > max[0].getWeight()):
                        max.clear()
                        max.append(arista)        
        return max[random.randint(0, len(max)-1)]

    # Getter de la palabra
    def getPalabra(self):
        return self.palabra
    
    # Se añade un nodo a la listEdge
    def pushListEdge(self, nodo):
        from EdgeClass import Edge
        if not isinstance(nodo, Node):
            raise TypeError("El parametro debe ser un nodo")
        self.listEdge.append(Edge(nodo))    

    # Alteramos el resultado cuando se haga un print de nodo.
    def __str__(self):
        return self.palabra