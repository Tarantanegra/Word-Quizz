import tkinter as tk
from constants import style
from screens import Home, Game

class Manager(tk.Tk):
    """Class to manage the interactions through the screens"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # titulo de la interfaz
        self.title("Vocabulary Review")

        # container 'parent' donde estara el resto  
        container = tk.Frame(self)
        self.mode = "Native"
        self.file = ""
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )

        # cambiamos el color 
        container.configure(background = style.BACKGROUND)

        # configurando el container como un cuadrado de 1x1
        # weight define el peso del container
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        # almacenamos los frames en un diccionario para tenerlos a mano
        self.frames = {}
        for F in (Home, Game):
            frame = F(container, self) # creamos el frame
            self.frames[F] = frame # guardamos el frame
            # pegamos el frame en nuestro container
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.show_frame(Home)

    def show_frame(self, container):
        """Put the 'container' frame at the top"""
        frame = self.frames[container]
        frame.tkraise()