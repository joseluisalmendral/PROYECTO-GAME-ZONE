class PiedraPapelTijera:
    def play(self):
        print("Estás jugando a Piedra Papel Tijera \n")
        # Aquí va la lógica del juego






        #terminamos de jugar
        return self.terminar_juego()

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