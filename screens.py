import tkinter as tk
from constants import style, config

class Home(tk.Frame):
    """Class to manage Home screen"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.gameMode = tk.StringVar(self)
        self.file = tk.StringVar(self)
        self.gameMode.set(f"Game Mode: \nLives:\nFiles:")
        self.options_label = None  

        self.init_widgets()

    def move_to_game(self):
        """Method to move to the 'Game' screen"""
        self.controller.mode = self.gameMode.get()  # save game mode selected
        self.controller.file = self.file.get()  # save file selected
        self.controller.show_frame(Game)  # show 'Game' frame

    def update_configuration_label(self):
        """Method to update the configuration label text"""
        self.options_label.config(text=f"Game Mode: {self.gameMode.get()}\n" + 
                                  f"Lives:\n" + 
                                  f"Files: {self.file.get()}")

    def select_file(self):
        """Method to update the selected file"""
        config.SELECTED_CLASSES = self.file.get()
        self.update_configuration_label()


    def init_widgets(self):
        """Method to store the frame widgets"""

        leftFrame = tk.Frame(self)
        leftFrame.configure(background=style.BACKGROUND)
        leftFrame.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=20,
            pady=20
        )

        rightFrame = tk.Frame(self)
        rightFrame.configure(background=style.COMPONENT)
        rightFrame.pack(
            side=tk.RIGHT,
            fill=tk.Y,
            padx=20,
            pady=20
        )

        # Label with the title of the application
        tk.Label(
            leftFrame,
            text="Vocabulary Review",
            justify=tk.CENTER,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            padx=20,
            pady=20
        )

        # Label header configuration
        tk.Label(
            rightFrame,
            text="Configuration",
            justify=tk.LEFT,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=20,
            pady=10
        )

        # Label with the selected options
        self.options_label = tk.Label(  # Assign to self.options_label
            rightFrame,
            text=self.gameMode.get(),
            justify=tk.LEFT,
            **style.STYLE
        )
        self.options_label.pack(  # Using self.options_label
            side=tk.TOP,
            fill=tk.X,
            padx=20,
            pady=20
        )

        for file in config.CLASSES:
            tk.Button(
                rightFrame,
                text=file,
                command= lambda f=file: (self.file.set(f), self.select_file()),
                activebackground=style.BACKGROUND,
                activeforeground=style.TEXT,
                **style.STYLE,
            ).pack(
                side=tk.TOP,
                fill=tk.X,
                padx=20,
                pady=5
            )

        # Container of options (with a label and the game mode buttons)
        optionsFrame = tk.Frame(leftFrame)
        optionsFrame.configure(background=style.COMPONENT)
        optionsFrame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=20,
            pady=20
        )
        tk.Label(
            optionsFrame,
            text="Select the Game Mode:",
            justify=tk.LEFT,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=20,
            pady=10
        )

        # Buttons for game mode selection
        for (key, val) in config.MODES.items():
            tk.Button(
                optionsFrame,
                text=key,
                command=lambda v=val: (self.gameMode.set(v), self.update_configuration_label()),
                activebackground=style.BACKGROUND,
                activeforeground=style.TEXT,
                **style.STYLE,
            ).pack(
                side=tk.TOP,
                fill=tk.X,
                padx=20,
                pady=5
            )

        tk.Label(
            optionsFrame,
            text="Lives: \n\n NOT IMPLEMENTED YET",
            justify=tk.LEFT,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=20,
            pady=10
        )

        # Button to start the game
        tk.Button(
            leftFrame,
            text="Start!",
            command=self.move_to_game,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT,
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=20,
            pady=20
        )


class Game(tk.Frame):
    """Class to manage Game screen"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller
        self.currentQuestion = tk.StringVar(self, value="Ready... Steady... GOOO!!!")
        self.file=None
        self.init_widgets()

    def update_question(self):
        """Change the question of the game"""
        self.file = self.controller.file
        if (self.file == None) or (self.controller.file.lower() not in self.file.name.lower()):
            self.file = open(f"./files/{self.file}.txt", "r", encoding="utf-8")
        tmp = self.file.readline()
        if tmp != "":
            self.currentQuestion.set(tmp)
        else:
            self.currentQuestion.set("There is no more words here, we will start again.")
            self.fichero = None

    def init_widgets(self):
        """Method to store the frame widgets"""

        tk.Label(
            self,
            text=self.file,
            justify=tk.LEFT,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=20,
            pady=10
        )

        tk.Label(
            self,
            text = "",
            textvariable=self.currentQuestion,
            justify=tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22, 
            pady = 11 
        )

        tk.Button(
                self,
                text="Siguiente ->",
                command=self.update_question,
                **style.STYLE,
                relief=tk.FLAT,
                activebackground=style.BACKGROUND,
                activeforeground=style.TEXT,
            ).pack(
                side = tk.TOP,
                fill=tk.BOTH,
                expand=True,
                padx=22,
                pady=11
            )
        
        tk.Button(
                self,
                text="Volver",
                command=lambda: self.controller.show_frame(Home),
                **style.STYLE,
                relief=tk.FLAT,
                activebackground=style.BACKGROUND,
                activeforeground=style.TEXT,
            ).pack(
                side = tk.TOP,
                fill=tk.BOTH,
                expand=True,
                padx=22,
                pady=11
            )
    