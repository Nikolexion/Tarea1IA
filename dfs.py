from laberintoSaltarin import laberintoSaltarin

class dfs():
    def __init__(self, laberinto: laberintoSaltarin):
        self.laberinto = laberinto
        self.visitados = set()
        self.padres = {}
        
    def resolver(self):
        pila = [(self.laberinto.inicio, 0)]

        while pila:
            (x, y), pasos = pila.pop()

            if (x, y) == self.laberinto.objetivo:
                return pasos, self.reconstruir_camino((x, y))
            
            if (x, y) in self.visitados:
                continue
            self.visitados.add((x, y))

            for nx, ny in self.laberinto.mover(x, y):
                if (nx, ny) not in self.visitados:
                    self.padres[(nx, ny)] = (x, y)
                    pila.append(((nx, ny), pasos + 1))


        return "no hay solución", []
                
    def reconstruir_camino(self, nodo):
        camino = []
        while nodo != self.laberinto.inicio:
            camino.append(nodo)
            nodo = self.padres[nodo]
        camino.append(self.laberinto.inicio)
        camino.reverse()
        return camino
    