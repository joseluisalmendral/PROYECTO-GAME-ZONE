#temas --> cultura general, historia, entretenimiento, actualidad
#mejoras pendientes, controlar errores (hacer respuestas mas 'flexibles'), extrael trozos de codigo a otro archivo python

import random
import os

class Preguntados:
    def __init__(self) -> None:
        self.chuleta = {
            "Cultura General": {
                "preguntas": [
                    "¿Cuál es el idioma más hablado en el mundo?",
                    "¿Cuántos continentes hay en la Tierra?",
                    "¿En qué país se encuentra la Torre Eiffel?",
                    "¿Cuál es la capital de España?",
                    "¿Qué moneda se utiliza en Japón?",
                    "¿En qué continente se encuentra el desierto del Sahara?",
                    "¿Cuál es el océano más grande del mundo?",
                    "¿Qué país es famoso por el tango?",
                    "¿Qué color tienen las esmeraldas?",
                    "¿Cuál es el país más grande del mundo por superficie?"
                ],
                "respuestas": [
                    "Chino mandarín",
                    "7",
                    "Francia",
                    "Madrid",
                    "Yen",
                    "África",
                    "Océano Pacífico",
                    "Argentina",
                    "Verde",
                    "Rusia"
                ]
            },
            "Historia": {
                "preguntas": [
                    "¿Quién fue el primer presidente de los Estados Unidos?",
                    "¿En qué año comenzó la Segunda Guerra Mundial?",
                    "¿Qué civilización construyó las pirámides de Egipto?",
                    "¿Cómo se llamaba el famoso emperador romano asesinado en el 44 a.C.?",
                    "¿Qué país descubrió Cristóbal Colón en 1492?",
                    "¿En qué año cayó el Muro de Berlín?",
                    "¿Cómo se llamaba el explorador que dio la vuelta al mundo por primera vez?",
                    "¿En qué siglo ocurrió la Revolución Francesa?",
                    "¿Cuál era el nombre del barco que llevó a los peregrinos a América en 1620?",
                    "¿Quién fue el líder nazi durante la Segunda Guerra Mundial?"
                ],
                "respuestas": [
                    "George Washington",
                    "1939",
                    "Los egipcios",
                    "Julio César",
                    "América",
                    "1989",
                    "Fernando de Magallanes",
                    "Siglo XVIII",
                    "Mayflower",
                    "Adolf Hitler"
                ]
            },
            "Entretenimiento": {
                "preguntas": [
                    "¿Cómo se llama el ratón más famoso de Disney?",
                    "¿En qué año se estrenó la primera película de 'Harry Potter'?",
                    "¿Qué superhéroe es conocido como el 'Hombre de Acero'?",
                    "¿Cuál es la película animada de Disney donde los personajes son juguetes que cobran vida?",
                    "¿Qué cantante es conocida como 'La Reina del Pop'?",
                    "¿Cómo se llama la banda de música británica conocida por la canción 'Bohemian Rhapsody'?",
                    "¿En qué serie de televisión aparecen los personajes 'Monica' y 'Chandler'?",
                    "¿Qué película ganó el Oscar a la mejor película en 1997 y está ambientada en un famoso barco que se hunde?",
                    "¿Cómo se llama el famoso mago de una serie de libros y películas escrita por J.K. Rowling?",
                    "¿En qué película de Pixar conocemos a un pez llamado Nemo?"
                ],
                "respuestas": [
                    "Mickey Mouse",
                    "2001",
                    "Superman",
                    "Toy Story",
                    "Madonna",
                    "Queen",
                    "Friends",
                    "Titanic",
                    "Harry Potter",
                    "Buscando a Nemo"
                ]
            },
            "Ciencia": {
                "preguntas": [
                    "¿Cuántos planetas hay en el sistema solar?",
                    "¿Cuál es el planeta más cercano al Sol?",
                    "¿Qué gas respiran las plantas durante la fotosíntesis?",
                    "¿Cuántos sentidos tiene el ser humano?",
                    "¿Cómo se llama el proceso por el cual las plantas fabrican su alimento?",
                    "¿Qué elemento químico tiene el símbolo 'O' en la tabla periódica?",
                    "¿Qué órgano del cuerpo humano es responsable de bombear la sangre?",
                    "¿En qué estado de la materia se encuentra el agua cuando está a 100°C?",
                    "¿Qué fuerza mantiene a los planetas en órbita alrededor del Sol?",
                    "¿Qué científico es conocido por su teoría de la relatividad?"
                ],
                "respuestas": [
                    "8",
                    "Mercurio",
                    "Dióxido de carbono (CO2)",
                    "5",
                    "Fotosíntesis",
                    "Oxígeno",
                    "El corazón",
                    "En estado gaseoso",
                    "Gravedad",
                    "Albert Einstein"
                ]
            }
        }

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
            os.system('cls')
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