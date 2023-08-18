#Ventana principal de nuestra aplicación
import tkinter as tk 
from constantes import style
from screens import Home,Game

class Manager(tk.Tk):
    def __init__(self,*args,**kwars):
        super().__init__(*args,**kwars)
        self.title('Yo nunca: Game')
        container = tk.Frame(self)
        container.pack(
            side= tk.TOP,
            fill = tk.BOTH,
            expand= True
        )
        container.configure(background= style.BACKGROUND)
        container.grid_columnconfigure(0,weight=1)
        container.grid_rowconfigure(0,weight=1)

        self.frames = {}
        for F in (Home,Game):
            frame = F(container,self)
            #Guardando el diccionario de clases
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky=tk.NSEW)
        self.show_frame(Home)

    def show_frame(self,container):
        frame = self.frames[container]
    #Nos ayuda a poner panatallas
        frame.tkraise()