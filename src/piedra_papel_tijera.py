#EN UN FUTURO PONER CONTADOR GUAPO CON TEXTOS DE MI LIBRERIA PROPIA SEPARADA


import random
import time

class PiedraPapelTijera:

    def __init__(self) -> None:
        self.rondas = 1
        self.contador_rondas = 0
        self.marcador = [0,0] #humano i=0 - maquina i=1
        self.elementos = { #elemtos con los elementos a los que ganan
            'piedra': ['tijera', 'lagarto'],
            'papel': ['piedra', 'spock'],
            'tijera': ['papel', 'lagarto'],
            'lagarto': ['spock', 'papel'],
            'spock': ['tijera', 'piedra']
        }
        self.nombre_elementos = ['piedra', 'papel', 'tijera', 'lagarto', 'spock'] #elementos para que seleccione la maquina
        self.eleccion_maquina = ''
        self.eleccion_jugador = ''
        self.resultado_final = ''


    def jugar(self):
        print("Estás jugando a PIEDRA PAPEL TIJERA \n")
        
        print("¿Cuantas rondas vas a querer jugar?\n")
        self.rondas = int(input("--> "))

        while self.contador_rondas < self.rondas:
            self.mostrar_ronda()
            self.mostrar_marcador()
            print(f"""
        ELIGE ;0!  [PIEDRA | PAPEL | TIJERA | LAGARTO | SPOCK]
                      0        1        2        3        4\n
                """)

            #hacemos elegir al jugador
            _eleccion_jugador = int(input("Tu eleccion --> "))
            self.eleccion_jugador = self.nombre_elementos[_eleccion_jugador]

            #hacemos que la maquina elija
            self.hacer_elegir_maquina()
            print(f"Eleccion maquina --> {self.eleccion_maquina}")
            
            #cuenta regresiva
            self.mostrar_cuenta_regresiva()

            print(f"\nHas elegido '{self.eleccion_jugador}' y la maquina '{self.eleccion_maquina}'")
            
            #caso empate
            if self.eleccion_maquina == self.eleccion_jugador:
                self.marcador[0] += 1
                self.marcador[1] += 1

            elif self.eleccion_maquina in self.elementos[self.eleccion_jugador]:
                #caso ganador
                self.marcador[0] += 1
            else:
                self.marcador[1] += 1
            
            #pasamos de ronda
            self.contador_rondas += 1

        #vemos quien ha ganado
        self.comprobar_ganador()

        #reseteamos el marcador por si el usuario vuelve a jugar
        

        #mostramos el resultado de la partida
        print(self.resultado_final)

        #terminamos de jugar
        return self.terminar_juego()
    

    def mostrar_ronda(self):
        print(f"                 RONDA: {self.contador_rondas}\n")

    def mostrar_marcador(self):
        print(f"""
          HUMANO    VS   MAQUINA
        ---------------------------
            {self.marcador[0]}               {self.marcador[1]}
             """)
        

    def hacer_elegir_maquina(self):
        """_summary_: no devuelve nada. Solo asigna valor a la eleccion de la clase.
        """        
        self.eleccion_maquina = self.nombre_elementos[random.randint(0,(len(self.nombre_elementos)-1))]

    def mostrar_cuenta_regresiva(self):
        print("3...")
        time.sleep(0.5)
        print("2...")
        time.sleep(0.5)
        print("1...")
        time.sleep(0.5)

    def comprobar_ganador(self):
        if self.marcador[0] > self.marcador[1]:
            self.resultado_final = "VICTORIA!!!!!!"
        elif self.marcador[0] == self.marcador[1]:
            self.resultado_final = "EMPATE!!!!!!"
        else:
            self.resultado_final = "DERROTA :("

    def reiniciar_juego(self):
        self.marcador[0], self.marcador[1] = 0, 0
        self.rondas, self.contador_rondas = 0, 0

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