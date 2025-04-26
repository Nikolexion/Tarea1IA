import numpy as np

class laberintoSaltarin():
    def __init__(self, m:int, n:int, xi:int, yi:int, xf:int, yf:int):
        self.m = m
        self.n = n
        self.inicio = (xi, yi)
        self.objetivo = (xf, yf)
        self.laberintos = []
        self.numeroLaberinto = 0
        self.numLabsTotal = 0
        self.tablero = np.zeros((m, n), dtype=int)

    def dentro(self, x:int, y:int) -> bool:
        return 0 <= x < self.m and 0 <= y < self.n
    
    def mover(self, x:int, y:int) -> list:
        movimientos =[]
        paso = (self.tablero[x,y])

        for dx, dy in [(paso, 0), (-1*paso, 0), (0, paso), (0, -1*paso)]:
            x1 = x + dx
            y1 = y + dy
            if self.dentro(x1, y1):
                movimientos.append((x1, y1))
                
        
        return movimientos
    
    def objetivo(self, x:int, y:int) -> bool:
        return (x, y) == self.objetivo

    def siguiente_laberinto(self):
        if self.numeroLaberinto >= len(self.laberintos):
            self.numeroLaberinto = 0
            
        #Seteamos todos los datos del laberinto actual
        self.tablero = self.laberintos[self.numeroLaberinto][6]
        self.m = self.laberintos[self.numeroLaberinto][0]
        self.n = self.laberintos[self.numeroLaberinto][1]
        self.inicio = (self.laberintos[self.numeroLaberinto][2], self.laberintos[self.numeroLaberinto][3])
        self.objetivo = (self.laberintos[self.numeroLaberinto][4], self.laberintos[self.numeroLaberinto][5])
        self.numeroLaberinto += 1
        

    def ingresarDatos(self, ruta = None):
        file = open(ruta, 'r') if ruta else None

        while True:
            lab = file.readline()
            if not lab:
                break
            lab = lab.strip()
            if lab == 0:
                break
            if lab == "":
                continue
            if len(lab) < 6:
                continue

            lab = lab.split()
            m = int(lab[0])
            n = int(lab[1])
            xi = int(lab[2])
            yi = int(lab[3])
            xf = int(lab[4])
            yf = int(lab[5])
            matriz = np.zeros((m, n), dtype=int)
            for i in range(m):
                fila = file.readline()
                fila = fila.split()
                for j in range(n):
                    matriz[i][j] = int(fila[j])
            self.numLabsTotal += 1
            self.laberintos.append((m, n, xi, yi, xf, yf, matriz))
