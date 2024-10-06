#preguntados, tres_en_raya, ahorcado, piedra_papel_tijera, hundir_la_flota

#en un futuro REFACTORIZAR los modulos de mecanicas de 'juego' como obtener juegos
#para quedar todo mucho mas limpio

import os
from pprint import pprint
from src.piedra_papel_tijera import PiedraPapelTijera
from src.preguntados import Preguntados
from src.hundir_la_flota import HundirLaFlota
from src.ahorcado import Ahorcado
from src.support import support_main as supp_main

class MenuJuego:
    def __init__(self):
        self.juegos = []#nombres de las clases de los juegos para despues declararlas dinamicamente
        self.nombres_juegos = []#nombre de juegos 'family friendly' para el usuario
        #obtenemos los juegos de nuestra carpeta src
        self.obtener_juegos()
        #mostramos los juegos que tenemos en un listado al jugador para que elija
        self.mostrarOpcionesMenu()


    def obtener_juegos(self):
        """_summary_: Obtiene los archivos de los juegos que tenemos en la carpeta 'src'
                      para que si añadimos más, se nos añadan de forma dinámica :)
        """        
        contenido = os.listdir('src')
        for juego in contenido:
            if (juego == "__pycache__" or juego == 'support'):
                continue

            #Formateo el nombre del archivo para mostrarlo al usuario
            juego = juego.replace('.py','')
            juego = juego.replace('_',' ')
            self.nombres_juegos.append(juego.upper())
        
        for juego in contenido:
            if (juego == "__pycache__" or juego == 'support'):
                continue

            print(juego)
            #Formateo el nombre del archivo para que tenga el mismo nombre que la clase que quiero
            #declarar dinamicamente
            juego = juego.replace('.py','')
            juego = juego.replace('_',' ')
            _ = juego.split()
            juego = list(map(lambda j: j.title(),_))
            juego = "".join(juego)

            self.juegos.append(juego)



    #imprimimos los juegos disponibles con la fantasia
    def mostrarOpcionesMenu(self):
        os.system('cls')
        print(supp_main.texto_bienvenida)
        print(supp_main.texto_a_que_quieres_jugar)
        
        for i,juego in enumerate(self.nombres_juegos):
            print(f"\t\t\t\t{i+1}. {juego}")
        
        print(f"\n\t\t\t\t{(len(self.nombres_juegos)+1)}. SALIR\n")

        try:
            eleccion = int(input(f"Numero del juego al que quieres jugar --> ")) -1 #quitamos uno ya que al mostrar los juegos se lo sumamos y asi no empezaba en 0
        except:
            print("El formato de entrada no es valido")
            eleccion = int(input(f"Numero del juego al que quieres jugar --> ")) -1

        while True:
            if eleccion < len(self.nombres_juegos):
                self.lanzar_juego(eleccion)
            elif eleccion == (len(self.nombres_juegos)):
                print("Saliendo del programa...")
                print("Hasta la próxima 👋")
                exit()
            else:
                print("Opción no válida, intenta de nuevo.")
                eleccion = int(input(f"Numero del juego al que quieres jugar --> ")) -1


    def lanzar_juego(self, eleccion):
        #game_class = self.juegos[eleccion]()#declaramos la clase de forma dinamica
        game_class = globals()[self.juegos[eleccion]]()
        while True:
            result = game_class.jugar()
            if result == 'volver_jugar':
                os.system('cls')
                continue
            elif result == 'volver_menu':
                self.mostrarOpcionesMenu()
                break
            elif result == 'salir':
                exit("Saliendo del programa...")

#INICIO DEL PROGRAMA
if __name__ == "__main__":
    menu = MenuJuego()




