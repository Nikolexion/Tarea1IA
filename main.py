from dfs import dfs
from laberintoSaltarin import laberintoSaltarin
from grafics import main

if __name__ == "__main__":

    #Creamos un laberinto vacio que se sobreescribirá
    laberintos = laberintoSaltarin(1, 1, 0, 0, 0, 0)
    #Leemos los laberintos desde el .txt
    laberintos.ingresarDatos(ruta="laberintos.txt")
    #Pasamos al primer laberinto
    laberintos.siguiente_laberinto()
            
    main(laberintos, dfs)

