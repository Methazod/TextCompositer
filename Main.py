from GraphClass import Graph
import os

"""
Clase ejecutable que creara un objeto de la clase
Graph y utilizara sus metodos para crear una cancion.
"""
os.system("cls")

# Creamos el objeto de la calse Graph.
grafo = Graph("D:/Clases/2º año/sistemasGestion/practicas/Text Compositer (Songs)/songs")

# Creamos la cancion
grafo.crearCancion()