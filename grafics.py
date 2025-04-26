import pygame
from laberintoSaltarin import laberintoSaltarin
from ucs import ucs
from dfs import dfs
from ucs2 import ucs2
import ctypes
import time

BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)
VERDE = (100, 255, 100)
ROJO = (255, 100, 100)
NEGRO = (0, 0, 0)
AZUL = (100, 100, 255)
MORADO = (100, 100, 255)
AZUL_GRIS = (180, 180, 255)


def dibujar_laberinto(pantalla, laberinto, camino=[], paso_actual=None):
    for i in range (laberinto.m):
        for j in range (laberinto.n):
            x = j*Tam_celda
            y = i*Tam_celda

            rect = pygame.Rect(x, y, Tam_celda, Tam_celda)

            if (i, j) == laberinto.inicio:
                color = VERDE
            elif (i, j) == paso_actual and (i, j) == laberinto.objetivo:
                color = MORADO
            elif paso_actual and (i, j) == paso_actual:
                color = AZUL
            elif (i, j) == laberinto.objetivo:
                color = ROJO
            elif (i, j) in camino:
                color = AZUL_GRIS
            else:
                color = GRIS

            pygame.draw.rect(pantalla, color, rect)
            pygame.draw.rect(pantalla, NEGRO, rect, 2)
            fuente = pygame.font.SysFont(None, 24)
            num = laberinto.tablero[i, j]
            texto = fuente.render(str(num), True, NEGRO)
            pantalla.blit(texto, (x + Tam_celda // 3, y + Tam_celda // 3))

def main(laberinto, algoritmoInicial):
    
    pygame.init()
    global Tam_celda

    if laberinto.m > 25 or laberinto.n > 25:
        Tam_celda = 30
    else:
        Tam_celda = 60

    ancho = laberinto.n * Tam_celda
    alto = laberinto.m * Tam_celda + 150
    if ancho < 290:
        ancho = 290

    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(f"Laberinto Saltarín - Laberinto {laberinto.numeroLaberinto + 1} de {laberinto.numLabsTotal}")

    hayMasLabs = laberinto.numeroLaberinto < laberinto.numLabsTotal


    #Todo esto es para forzar que la ventana se ponga en primer plano
    pygame.display.iconify()
    time.sleep(0.2)
    hwnd = pygame.display.get_wm_info()['window']
    ctypes.windll.user32.ShowWindow(hwnd, 9) 
    ctypes.windll.user32.SetForegroundWindow(hwnd)

    algoritmo = algoritmoInicial
    solver = algoritmo(laberinto)
    pasos, camino = solver.resolver()
    numero_paso = 0

    reloj = pygame.time.Clock()
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botonReiniciar.collidepoint(evento.pos):
                    numero_paso = 0
                elif botonAlgoritmo.collidepoint(evento.pos):
                    #Boton para alternar entre DFS y UCS
                    if algoritmo.__name__ == "dfs":
                        algoritmo = ucs
                    elif algoritmo.__name__ == "ucs":
                        algoritmo = ucs2
                    else:
                        algoritmo =  dfs
                    solver = algoritmo(laberinto)
                    pasos, camino = solver.resolver()
                    numero_paso = 0
                elif botonSgteLaberinto.collidepoint(evento.pos) and hayMasLabs:
                    #Pasa al siguiente laberinto y reinicia el algoritmo
                    laberinto.siguiente_laberinto()
                    
                    if laberinto.m > 25 or laberinto.n > 25:
                        Tam_celda = 30
                    else:
                        Tam_celda = 60

                    ancho = laberinto.n * Tam_celda
                    alto = laberinto.m * Tam_celda + 150
                    if ancho < 290:
                        ancho = 290
                    pantalla = pygame.display.set_mode((ancho, alto))
                    pygame.display.set_caption(f"Laberinto Saltarín - Laberinto {laberinto.numeroLaberinto} de {laberinto.numLabsTotal}")


                    solver = algoritmo(laberinto)
                    pasos, camino = solver.resolver()
                    numero_paso = 0

        pantalla.fill(BLANCO)
        botonReiniciar = dibujar_boton(pantalla, "Reiniciar", 10, laberinto.m * Tam_celda + 10, 100, 40, True)
        botonAlgoritmo = dibujar_boton(pantalla, f"Algoritmo: {algoritmo.__name__.upper()}", 130, laberinto.m * Tam_celda + 10, 150, 40, True)
        botonSgteLaberinto = dibujar_boton(pantalla, "Siguiente" \
        " Laberinto", 10, laberinto.m * Tam_celda + 55, 170, 40, hayMasLabs)

        camino_pasado = camino[:numero_paso]
        paso_actual = camino[numero_paso] if numero_paso < len(camino) else None
        dibujar_laberinto(pantalla, laberinto,camino_pasado, paso_actual)


        fuente = pygame.font.SysFont(None, 28)
        if camino:
            if algoritmo.__name__ == "ucs" or algoritmo.__name__ == "ucs2":
                texto = fuente.render(f"Costo total: {pasos}", True, NEGRO)
            else:
                texto = fuente.render(f"Pasos necesarios {pasos}", True, NEGRO)
        else:
            texto = fuente.render("No hay solución", True, ROJO)

        pantalla.blit(texto, (10, alto -28))

        pygame.display.flip()
        reloj.tick(1)

        if numero_paso < len(camino):
            numero_paso+=1

    pygame.quit()


def dibujar_boton(pantalla, texto, x, y, ancho, alto, activo):
    color = (150, 200, 255) if activo else (200, 200, 200)
    rectBoton = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(pantalla, color, rectBoton)
    pygame.draw.rect(pantalla, NEGRO, rectBoton, 2)
    fuente = pygame.font.SysFont(None, 24)
    textoboton = fuente.render(texto, True, NEGRO)
    pantalla.blit(textoboton, (x + 10, y + 10))
    return rectBoton
