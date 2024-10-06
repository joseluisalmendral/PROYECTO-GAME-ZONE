#temas --> cultura general, historia, entretenimiento, actualidad
#mejoras pendientes, controlar errores (hacer respuestas mas 'flexibles'), extrael trozos de codigo a otro archivo python

import random
import os
from src.support import support_preguntados

class Preguntados:
    def __init__(self) -> None:
        self.chuleta = support_preguntados.preguntas_respuestas

        #preguntas y respuestas que seran elegidas aleatoriamente
        self.preguntas_respuestas = []
        
        self.preguntas_acertadas = 0


    def jugar(self):
        print("Estas jugando a PREGUNTADOS")

        #obtenemos categorias
        categorias = self.obtener_categorias()

        #hacemos que la maquina elija las 10 preguntas y respuestas
        self.elegir_preguntas_respuestas(categorias)

        #descomentar en caso de querer saber las respuestas o debugear
        self.mostrar_preguntas_respuestas()

        self.comenzar_partida()



        #terminamos el juego
        return self.terminar_juego()#importante el return


    #obtejemos las categorias que tengamos en nuestra chuleta
    def obtener_categorias(self):
        resultado = []
        for categoria in self.chuleta:
            resultado.append(categoria)

        return resultado
    

    def elegir_preguntas_respuestas(self, categorias):

        cantidad_categorias = len(categorias)
        for _ in range(0,10):
            eleccion_aleatoria = random.randint(0,9)
            categoria_elegida_random = categorias[random.randint(0,cantidad_categorias-1)]
            self.preguntas_respuestas.append((#esto es una tupla
                self.chuleta[categoria_elegida_random]['preguntas'][eleccion_aleatoria],
                self.chuleta[categoria_elegida_random]['respuestas'][eleccion_aleatoria]
            ))

    def comenzar_partida(self):
        while self.preguntas_acertadas <= 9: #self.preguntas_acertadas lo utilizare como guia ya que ira incrementando si el usuario acirta
            
            pregunta, respuesta = self.preguntas_respuestas[self.preguntas_acertadas]
            
            print(f"\nPREGUNTA {self.preguntas_acertadas+1}\n")
            print(f"{pregunta}\n")
            respuesta_usuario = input("--> ")

            #caso respuesta correcta
            if respuesta_usuario.lower() == respuesta.lower():
                self.preguntas_acertadas += 1
            else:
                print("Perdiste :(")
                print(f"Total aciertos: '{self.preguntas_acertadas}'\n")
                break
        
        #caso completar las 10 preguntas
        if self.preguntas_acertadas == 10:
            self.limpiar_pantalla()
            print("FELICITACIONES!!!! LO HAS CONSEGUIDO\n")
            print(f"Preguntas acertadas --> {self.preguntas_acertadas}\n")


    def reinicar_juego(self):
        self.preguntas_respuestas = []
        self.preguntas_acertadas = 0

    #esto es para si queremos debugear
    def mostrar_preguntas_respuestas(self):
        for tupla in self.preguntas_respuestas:
            print(tupla)
        print("\n")

    def limpiar_pantalla(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def terminar_juego(self):
        while True:
            print("\n1. Volver a jugar")
            print("2. Volver al menú de juegos")
            print("3. Terminar el programa")
            choice = input("Selecciona una opción: ")
            if choice == '1':
                self.reinicar_juego()
                return 'volver_jugar'
            elif choice == '2':
                return 'volver_menu'
            elif choice == '3':
                return 'salir'
            else:
                print("Opción no válida. Intenta de nuevo.")