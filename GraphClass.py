from NodeClass import Node
import os, random

"""
Clase que crea un grafo.

Jorge Manzano Anchelergues y Jaime Usero Aranda.
"""

class Graph:

    # Construye un grafo
    def __init__(self, path: str):
        if not isinstance(path, str):
            raise TypeError("La ruta debe ser de tipo 'string'.")

        self.listNode = self.construirGrafo(self.getPalabrasCanciones(path))  
        
    # Metodo que carga la lista de nodos.
    def construirGrafo(self, palabras: list[str]):        
        listNode = []        
        # Recorremos la lista que guarda todas las palabras de las canciones.
        for palabra in palabras:
            # Si la lista de nodos esta vacia             
            if(len(listNode) == 0):
                listNode.append(Node(palabra, len(listNode)))
            # Si la lista de nodos no esta vacia
            else:
                existe = False
                # Recorremos la lista de Nodos
                for nodo in listNode:
                    # Si el nodo ya existe
                    if(nodo.getPalabra() == palabra):
                        nodoActual, nodoAnterior, existe = nodo, listNode[-1], True                    
                        break       
                # Si el nodo existe
                if(existe):              
                    # Si la lista de aristas del ultimo nodo de la lista esta vacia   
                    if(len(nodoAnterior.getListEdge()) == 0): 
                        nodoAnterior.pushListEdge(nodoActual)
                    # Si la lista de aristas del ultimo nodo de la lista no esta vacia
                    else:
                        existeArista = False                        
                        # Recorremos la lista de aristas
                        for arista in nodoAnterior.getListEdge(): 
                            # Si la arista ya existe
                            if(arista.getNext().getPalabra() == nodoActual.getPalabra()):                              
                                existeArista = True                                
                                break
                        # Si la arista existe                                                                     
                        if(existeArista):
                            arista.incrementarPeso()
                        # Si la arista no existe
                        else:
                            nodoAnterior.pushListEdge(nodoActual)
                # Si el nodo no existe                
                else:
                    listNode.append(Node(palabra, len(listNode)))
                    # Recorremos la lista de nodos
                    for nodo in listNode: 
                        # Buscamos el nodo que guarda la palabra anterior al nodo actual
                        if(nodo.getPalabra() == palabraAnterior):
                            nodo.pushListEdge(listNode[-1])
                            break            
            palabraAnterior = palabra
        return listNode

    """
    Metodo que se mete en una ruta que guarda canciones
    en una lista, cada elemento es una palabra de la
    cancion
    """    
    def getPalabrasCanciones(self, path: str):
        palabras = []
        for archivo in os.listdir(path):
            cancion = open(path + "/" + archivo, "r", encoding='utf-8')
            for palabra in cancion.read().split():
                palabras.append(self.normalToPlano(palabra))                
            cancion.close()                  
        return palabras
    
    """
    Metodo que coge una palabra y la pone en minuscula,
    le quita acentos, signos de exclamacion, duda, comas
    puntos y cualquier otra cosa que pueda contener.
    """
    def normalToPlano(self, palabra: str):
        palabra = palabra.upper()
        borrarSignos = "!¡?¿,.'`;/\|[]}{()€%&$·#@¬=*+-_:<>~^ "
        vocalesAcentos = "ÁÉÍÓÚÄËÏÖÜÂÊÎÔÛ"
        vocales = "AEIOU"
        palabra = palabra.replace('"', "")
        for signo in borrarSignos:
            palabra = palabra.replace(signo, "")
        iterador = 0
        for letra in vocalesAcentos:
            palabra = palabra.replace(letra, vocales[iterador])
            iterador = (iterador+1) % len(vocales)
        return palabra.lower()
    
    """
    Metodo que recorre el grafo, situandose primero de 
    manera aleatoria en un nodo, despues va recorriendo 
    los nodos pasando a la arista que contenga mas peso.
    Si no hay aristas vuelve a sacar una posicion aleatoria.
    Si la posicion es mayor a la lista de nodos vuelve a
    sacar una posicion aleatoria.
    """
    def crearCancion(self):
        contador, cancion = 1, ""
        posicion = random.randint(0, len(self.listNode)-1)
        while (contador != 91):  
            cancion += self.listNode[posicion].getPalabra() + " "
            if(contador % 10 == 0):
                cancion += "\n"
            if(self.listNode[posicion].getMaxEdge() is not None):
                posicion = self.listNode[posicion].getMaxEdge().getNext().id
            else:                            
                posicion = random.randint(0, len(self.listNode)-1)            
            contador += 1
        print(cancion)