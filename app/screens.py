import tkinter as tk
from constantes import style

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background= style.BACKGROUND)
        self.controller = controller
        self.gameMode = tk.StringVar(self,value = 'Normal')
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text = 'Yo nunca : The game',
            justify= 'center',
            #* Desempaquetar un diccionario
            **style.STYLE

#EL PACK ES NECESARIO PARA MOSTRAR
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand=True,
            padx = 22,
            pady = 11
        )

class Game(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background= style.BACKGROUND)
        self.controller = controller
    