from laberintoSaltarin import laberintoSaltarin
from queue import PriorityQueue

class ucs():
    def __init__(self, laberinto: laberintoSaltarin):
        self.laberinto = laberinto
        self.visitados = set()
        self.padres = {}
        self.costos = {laberinto.inicio: 0}
        self.pila = PriorityQueue()
        self.pila.put((0, laberinto.inicio))

    def resolver(self):
        while not self.pila.empty():
            costo_actual, (x,y) = self.pila.get()

            if (x,y) == self.laberinto.objetivo:
                return costo_actual, self.reconstruir_camino((x,y))
            if (x,y) in self.visitados:
                continue
            self.visitados.add((x,y))
            
            for nx, ny in self.laberinto.mover(x,y):
                if (nx, ny) not in self.visitados and (nx, ny) not in self.costos:
                    nuevo_costo = costo_actual + 1
                    self.padres[(nx, ny)] = (x, y)
                    self.pila.put((nuevo_costo, (nx, ny)))
                    


    def reconstruir_camino(self, nodoFinal):
        camino = []
        nodoActual = nodoFinal
        while nodoActual in self.padres:
            camino.append(nodoActual)
            nodoActual = self.padres[nodoActual]
        camino.append(nodoActual)

        camino.reverse()
        return camino