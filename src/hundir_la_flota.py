import string
import random
import os
import time
from src.support import support_hundir_la_flota as support

class HundirLaFlota:
    def __init__(self):
        self.mostrar_barcos = True if input("QUIERES QUE SE MUESTREN LOS BARCOS? (s/n)") == 's' else False
        self.caracter_mar = " "
        self.caracter_barco = "b"
        self.caracter_barco_tocado = "X"
        self.caracter_barco_hundido = "O"
        self.ataque_fallido = "-"

        self.longitud = 10
        self.barcos = [('Portaviones', 5), ('Acorazado', 4), ('Submarino', 3), ('Destructor', 3), ('Patrullero', 2)]

        self.tablero_maquina = list(map(lambda _: [self.caracter_mar] * self.longitud, range(self.longitud)))
        self.tablero_jugador = list(map(lambda _: [self.caracter_mar] * self.longitud, range(self.longitud)))

        self.numeros_columnas = [str(i) for i in range(1, self.longitud + 1)]
        letras = string.ascii_uppercase
        self.letras_filas = [letras[i] for i in range(0, self.longitud)]

        self.turno = "jugador"
        self.rondas = 0


    def jugar(self):
        print('Estás jugando a Hundir la Flota\n')

        self.colocar_barcos_random('maquina')
        self.colocar_barcos_random('jugador')

        self.pintar_tableros()

        while True:
            resultado = self.comenzar_juego()

            if resultado == 'terminar':
                break

        return self.terminar_juego()
    


    # PINTAR TABLEROS
    def pintar_tableros(self):
        print(support.texto_junto)

        tablero_jugador = self.tablero_jugador
        for i, fila_maquina in enumerate(self.tablero_maquina):

            contenido_fila_jugador = ""
            contenido_fila_maquina = ""

            if self.mostrar_barcos:
                contenido_fila_maquina = " | ".join(fila_maquina)
                contenido_fila_jugador = " | ".join(tablero_jugador[i])
            else:
                contenido_fila_maquina = " | ".join(fila_maquina).replace(self.caracter_barco,self.caracter_mar)
                contenido_fila_jugador = " | ".join(tablero_jugador[i]).replace(self.caracter_barco,self.caracter_mar)
            

            # Primera línea del tablero
            print(f"    {"+---" * self.longitud}" + "+\t\t",
                  f"    {"+---" * self.longitud}" + "+")
            
            # Contenido de cada línea
            print(f"  {self.letras_filas[i]} | {contenido_fila_jugador}" + " |\t\t",
                  f"  {self.letras_filas[i]} | {contenido_fila_maquina}" + " |")
        
        # Línea final del tablero
        print("    " + "+---" * self.longitud + "+\t\t",
              "    " + "+---" * self.longitud + "+")
        
        # Números de las columnas
        print("      " + "   ".join(self.numeros_columnas) + "\t\t",
              "      " + "   ".join(self.numeros_columnas)) 
        


    def colocar_barcos_random(self, jugador="maquina"):
        tablero_indicado = self.tablero_maquina if jugador == 'maquina' else self.tablero_jugador

        for barco in self.barcos:
            orientacion = ['horizontal', 'vertical']
            orientacion_elegida = orientacion[random.randint(0, 1)]  # elige entre vertical u horizontal

            while True:
                posicion = self.elegir_posicion_aleatoria()
                letra_fila = self.letras_filas.index(posicion['fila'])  # int
                n_columna = int(posicion['columna']) - 1  # -1 porque trabajamos con índices de listas
                fila = tablero_indicado[letra_fila]

                if orientacion_elegida == 'horizontal':
                    if n_columna + barco[1] <= len(fila):
                        espacio_libre = True
                        for i in range(n_columna, n_columna + barco[1]):
                            if tablero_indicado[letra_fila][i] == self.caracter_barco:
                                espacio_libre = False
                                break

                        if espacio_libre:
                            for i in range(n_columna, n_columna + barco[1]):
                                tablero_indicado[letra_fila][i] = self.caracter_barco
                            break  # Pasamos al siguiente barco

                # Orientación vertical
                else:
                    if letra_fila + barco[1] <= len(tablero_indicado):
                        espacio_libre = True
                        for i in range(letra_fila, letra_fila + barco[1]):
                            if tablero_indicado[i][n_columna] == self.caracter_barco:
                                espacio_libre = False
                                break

                        if espacio_libre:
                            for i in range(letra_fila, letra_fila + barco[1]):
                                tablero_indicado[i][n_columna] = self.caracter_barco
                            break  # Pasamos al siguiente barco



    def comenzar_juego(self):
        mensaje = "\nES TU TURNO DE ATACAR!\n" if self.turno == 'jugador' else "\nTURNO DE LA MAQUINA!\n"
        print(mensaje)

        fila = 0
        columna = 0
        tablero_indicado = self.tablero_maquina if self.turno == 'jugador' else self.tablero_jugador

        if self.turno == 'maquina':
            while True:
                posicion_aleatoria = self.elegir_posicion_aleatoria()
                columna = int(posicion_aleatoria['columna']) - 1
                fila = self.letras_filas.index(posicion_aleatoria['fila'])

                # Comprobamos que la posicion no haya sido seleccionada anteriormente
                if tablero_indicado[fila][columna] not in [self.caracter_barco_tocado, self.ataque_fallido]:
                    self.mostrar_cuenta_regresiva(fila,columna)
                    break
                else:
                    continue

            

        # Turno del jugador
        else:
            while True:
                fila_input = input(f"Introduce la LETRA de la fila --> ").upper()
                if fila_input in self.letras_filas:
                    fila = self.letras_filas.index(fila_input)
                    break
                else:
                    print("Fila inválida. Inténtalo de nuevo.")
            
            while True:
                columna_input = input(f"Introduce el NUMERO de columna --> ")
                if columna_input.isdigit() and 1 <= int(columna_input) <= self.longitud:
                    columna = int(columna_input) - 1

                    # Comprobamos que la posicion no haya sido seleccionada anteriormente
                    if tablero_indicado[fila][columna] not in [self.caracter_barco_tocado, self.ataque_fallido]:
                        break
                    else:
                        continue
                else:
                    print("Columna inválida. Inténtalo de nuevo.")

        # Caso Acierto
        if tablero_indicado[fila][columna] == self.caracter_barco:
            tablero_indicado[fila][columna] = self.caracter_barco_tocado
            self.pintar_tableros()
            print("\nYEAAH! barco golpeado.\n")

        # Caso Fallo
        else:
            tablero_indicado[fila][columna] = self.ataque_fallido
            self.pintar_tableros()
            print("\nFallo!. No había ningún barco.\n")
            print("CAMBIO DE TURNO\n")

            # Cambio de turno
            self.turno = 'maquina' if self.turno == 'jugador' else 'jugador'
        
        self.rondas += 1
        
        if self.rondas >= 17: # 17 porque son los disparos minimos que hay que hacer y asi no comprueba todo el rato
            return self.comprobar_ganador()


    
    def comprobar_ganador(self):

        jugador_gana = all(
            cell != self.caracter_barco for row in self.tablero_maquina for cell in row
        )

        if jugador_gana:
            print("\n¡Felicidades! Has hundido todos los barcos de la máquina. ¡Has ganado!\n")
            return 'terminar'


        maquina_gana = all(
            cell != self.caracter_barco for row in self.tablero_jugador for cell in row
        )

        if maquina_gana:
            print("\n¡La máquina ha hundido todos tus barcos! Has perdido.\n")
            return 'terminar'
        else:
            return None



    def elegir_posicion_aleatoria(self):
        fila = self.letras_filas[random.randint(0, len(self.letras_filas) - 1)]
        columna = self.numeros_columnas[random.randint(0, len(self.numeros_columnas) - 1)]

        return {
            'fila': fila,
            'columna': columna
        }
    


    def mostrar_cuenta_regresiva(self, fila, columna):
        time.sleep(1)
        print(f"La maquina ha elegido --> {self.letras_filas[fila]}{columna+1}!\n")
        time.sleep(1)
        print("....")
        time.sleep(1)

    def reiniciar_juego(self):
        self.mostrar_barcos = True if input("QUIERES QUE SE MUESTREN LOS BARCOS? (s/n)") == 's' else False
        self.rondas = 0
        self.tablero_maquina = list(map(lambda _: [self.caracter_mar] * self.longitud, range(self.longitud)))
        self.tablero_jugador = list(map(lambda _: [self.caracter_mar] * self.longitud, range(self.longitud)))



    def terminar_juego(self):
        while True:
            print("\n1. Volver a jugar")
            print("2. Volver al menú de juegos")
            print("3. Terminar el programa")
            choice = input("Selecciona una opción: ")
            if choice == '1':
                self.reiniciar_juego()
                return 'volver_jugar'
            elif choice == '2':
                return 'volver_menu'
            elif choice == '3':
                return 'salir'
            else:
                print("Opción no válida. Intenta de nuevo.")