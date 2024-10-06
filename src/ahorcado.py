from src.support import support_ahorcado as support
import os

class Ahorcado:
    def __init__(self):
        self.trozos_stickman = support.stickman_dibujos
        self.intentos_restantes = 6
        self.palabra_secreta = ""
        self.letras_adivinadas = []
        self.letras_intentadas = []

    def elegir_palabra(self):
        palabras = support.palabras_a_elegir
        import random
        self.palabra_secreta = random.choice(palabras).lower()
        self.letras_adivinadas = ['_'] * len(self.palabra_secreta)
        self.letras_intentadas = []
        self.intentos_restantes = 6

    def mostrar_stickman(self):
        # Mostramos el estado del ahorcado según los intentos restantes
        print(self.trozos_stickman[6 - self.intentos_restantes])

    def mostrar_estado(self):
        # Mostrar la palabra oculta con los espacios y las letras adivinadas
        print(' '.join(self.letras_adivinadas))

    def jugar(self):

        os.system('cls')
        self.elegir_palabra()
        while self.intentos_restantes > 0 and '_' in self.letras_adivinadas:

            self.mostrar_stickman()
            print(f"\nTe quedan {self.intentos_restantes} intentos.")
            self.mostrar_estado()
            print("\nLetras intentadas:", ', '.join(self.letras_intentadas))

            intento = input("\nAdivina una letra: ").lower()

            if len(intento) != 1 or not intento.isalpha():
                print("Por favor, ingresa una sola letra.")
                continue

            if intento in self.letras_intentadas:
                print(f"Ya has intentado la letra '{intento}'.")
                continue

            self.letras_intentadas.append(intento)

            if intento in self.palabra_secreta:
                print(f"¡Bien hecho! La letra '{intento}' está en la palabra.")
                for i in range(len(self.palabra_secreta)):
                    if self.palabra_secreta[i] == intento:
                        self.letras_adivinadas[i] = intento
            else:
                print(f"La letra '{intento}' no está en la palabra.")
                self.intentos_restantes -= 1

        # Verificación final de victoria o derrota
        if '_' not in self.letras_adivinadas:
            print("\n¡Felicidades! Has adivinado la palabra:", self.palabra_secreta)
        else:
            self.mostrar_stickman()
            print("\n¡Lo siento! Has perdido. La palabra era:", self.palabra_secreta)

        self.terminar_juego()

    def limpiar_pantalla():
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
                self.jugar()
            elif choice == '2':
                return 'volver_menu'
            elif choice == '3':
                return 'salir'
            else:
                print("Opción no válida. Intenta de nuevo.")
