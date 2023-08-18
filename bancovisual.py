import tkinter as tk
import banco

app = tk.Tk()
#Mantendremos el exto del usuario actualizado
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)

app.geometry('200x500')
app.config(background='black')
tk.Wm.wm_title(app,'Hola')
#def hola():
 #   palabra.set('Suscribete' + ' ' + entrada.get())
def saludar():
    print('hola crack' + ' ' + entrada.get())
def hablar():
    print('Hola mundo')

name1 = input('Cual es tu nombre ')
tk.Button(
    
    app,
    text = name1,
    font = ('Italic',25),
    bg='#C9533A',
    fg='#ECE4E2',
    

).pack(
    fill = tk.BOTH,
    
)
#El label es utilizado para bptones preestablecidos
tk.Label(
    app,
    text='I´m a etiket',
    textvariable=palabra,
    font = ('Arial',24),
    bg='#66B956',
    fg= '#050505',
).pack(
    fill = tk.BOTH,
)
#Poder insertar inputs para que las personas puedan escribir
tk.Entry(
    app,
    text='Mateo',
    font = ('Arial',24),
    justify= 'center',
    bg='#66B956',
    fg= '#050505',
    textvariable= palabra
).pack(
    fill = tk.BOTH,
)
app.mainloop()