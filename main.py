#preguntados, tres_en_raya, ahorcado, piedra_papel_tijera, hundir_la_flota

import os

class MenuJuego:
    def __init__(self) -> None:
        print("""
██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗ ██╗  ██╗██╗
██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗╚██╗██╔╝██║
██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║ ╚███╔╝ ██║
██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║ ██╔██╗ ╚═╝
██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝██╔╝ ██╗██╗
╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝
              

""")
        self.mostrarOpcionesMenu()

    
    def mostrarOpcionesMenu(self):
        contenido = os.listdir('src')

        print("Archivos encontrados:")
        for arhivo in contenido:
            print(arhivo)

if __name__ == "__main__":
    menu = MenuJuego()




