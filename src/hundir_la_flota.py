import string
import random
from src.support import support_hundir_la_flota as support

class HundirLaFlota:
    def __init__(self):
        self.caracter_mar = " "
        self.caracter_barco = "b"
        self.longitud = 10
        self.barcos = [('Portaviones',5), ('Acorazado',4), ('Submarino',3), ('Destructor',3), ('Patrullero',2)]
        self.tablero_maquina = list(map(lambda _: [self.caracter_mar] * self.longitud, range(self.longitud)))
        self.tablero_jugador = list(map(lambda _: [self.caracter_mar] * self.longitud, range(self.longitud)))

        self.numeros_columnas = [str(i) for i in range(1, self.longitud + 1)]
        letras = string.ascii_uppercase
        self.letras_filas = [letras[i] for i in range(0,self.longitud)]



    def jugar(self):
        print('estas jugando a hundir la flota \n')

        #hacemos la colocacion aleatoria de los barcos para la maquina
        self.colocar_barcos_maquina()

        self.pintar_tableros()

        return self.terminar_juego()





    #PINTAR TABLEROS
    def pintar_tableros(self):
        #print(f"\n\t{support.texto_maquina}\t{support.texto_vs}\t{support.texto_jugador}")
        # print(support.texto_maquina,end="")
        # print(support.texto_vs,end="")
        # print(support.texto_jugador)
        print(support.texto_junto)


        tablero_jugador = self.tablero_jugador
        for i, fila_maquina in enumerate(self.tablero_maquina):
            #comentar .replace() para no mostrar donde estan los barcos
            contenido_fila_maquina = " | ".join(fila_maquina) #.replace(caracter_barco,caracter_mar)
            contenido_fila_jugador = " | ".join(tablero_jugador[i]) #.replace(caracter_barco,caracter_mar)

            #primera linea del tablero
            print(f"    {"+---" * self.longitud}" + "+\t\t",
                  f"    {"+---" * self.longitud}" + "+")
            
            #contenido de cada linea
            print(f"  {self.letras_filas[i]} | {contenido_fila_maquina}" + " |\t\t",
                  f"  {self.letras_filas[i]} | {contenido_fila_jugador}" + " |")
            
        #linea final del tablero
        print("    " + "+---" * self.longitud + "+\t\t",
              "    " + "+---" * self.longitud + "+")
        
        #numeros de las columnas
        print("      " + "   ".join(self.numeros_columnas) + "\t\t",
              "      " + "   ".join(self.numeros_columnas)) 



    def colocar_barcos_maquina(self):
        for barco in self.barcos:
            orientacion = ['horizontal', 'vertical']
            orientacion_elegida = orientacion[random.randint(0, 1)] #elige entre vertical u horizontal

            while True:
                posicion = self.elegir_posicion_aleatoria()
                letra_fila = self.letras_filas.index(posicion['fila'])#int
                n_columna = int(posicion['columna']) - 1 # -1 porque trabajamos con indices de listas
                fila = self.tablero_maquina[letra_fila]

                if orientacion_elegida == 'horizontal':
                    if n_columna + barco[1] <= len(fila):
                        espacio_libre = True
                        for i in range(n_columna, n_columna + barco[1]):
                            if self.tablero_maquina[letra_fila][i] == self.caracter_barco:
                                espacio_libre = False
                                break

                        if espacio_libre:
                            for i in range(n_columna, n_columna + barco[1]):
                                self.tablero_maquina[letra_fila][i] = self.caracter_barco
                            break  # Pasamos al siguiente barco

                # Orientación vertical
                else:
                    if letra_fila + barco[1] <= len(self.tablero_maquina):
                        espacio_libre = True
                        for i in range(letra_fila, letra_fila + barco[1]):
                            if self.tablero_maquina[i][n_columna] == self.caracter_barco:
                                espacio_libre = False
                                break 

                        if espacio_libre:
                            for i in range(letra_fila, letra_fila + barco[1]):
                                self.tablero_maquina[i][n_columna] = self.caracter_barco
                            break # Pasamos al siguiente barco



    def elegir_posicion_aleatoria(self):
        fila = self.letras_filas[random.randint(0,len(self.letras_filas)-1)]
        columna = self.numeros_columnas[random.randint(0,len(self.numeros_columnas)-1)]

        return {
            'fila': fila,
            'columna': columna
        }


    def terminar_juego(self):
        while True:
            print("\n1. Volver a jugar")
            print("2. Volver al menú de juegos")
            print("3. Terminar el programa")
            choice = input("Selecciona una opción: ")
            if choice == '1':
                return 'volver_jugar'
            elif choice == '2':
                return 'volver_menu'
            elif choice == '3':
                return 'salir'
            else:
                print("Opción no válida. Intenta de nuevo.")