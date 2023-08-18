import tkinter as tk 
import banco
import otherfunc
import functools

app = tk.Tk()
app.geometry('700x500')
app.config(background='white')
tk.Wm.wm_title(app,'Banco DataNova')

palabra = tk.StringVar(app)
entrada = tk.StringVar(app)

def cambiar_word():
    palabra.set('Bienvenido' + ' ' +entrada.get())

cuenta = 0

def consultar():
    global cuenta
    print(f'Su saldo es {cuenta}')


def poner_dinero():
    global cuenta
    cuenta += otherfunc.ingresar_dinero(cuenta)
    print(f'Tu saldo es ${cuenta}')

def sacar_dinero():
    global cuenta
    cuenta += otherfunc.sacar_dinero(cuenta)




tk.Label(
    
    app,
    text='Bienvenido al Banco DataNova',
    font = ('Times New Roman',59),
    bg='black',
    fg= 'white',

).pack(
    fill = tk.BOTH,
    expand=True)
tk.Label(
    
    app,
    text='¿Cúal es tu nombre?',
    font = ('Times New Roman',19),
    bg='black',
    fg= 'white',

).pack(
    fill = tk.BOTH,)

tk.Entry(
    app,
    
    font = ('Times New Roman',30),
    justify= 'center',
    bg='gray',
    fg= 'white',
    textvariable = entrada
    
).pack(
    fill = tk.BOTH,
)

tk.Label(
    app,
    text='',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    textvariable= palabra,
).pack(
    fill = tk.BOTH,
    )

tk.Button(
    app,
    text='START',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command= cambiar_word
).pack(
    fill = tk.BOTH,)
tk.Label(
    app,
    text='',
    font=('Times New Roman',30),
    bg='black',
    fg='black',
    textvariable= palabra,
).pack(
    fill = tk.BOTH,
    )
tk.Button(
    app,
    text='Consultar saldo',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command= consultar
).pack(
    fill = tk.BOTH,
    expand=True
)
tk.Button(
    app,
    text='Agregar Dinero',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command= poner_dinero
).pack(
    fill = tk.BOTH,
    expand=True
)
tk.Button(
    app,
    text='Sacar dinero',
    font=('Times New Roman',30),
    bg='white',
    fg='black',
    command=sacar_dinero
).pack(
    fill = tk.BOTH,
    expand=True
)
tk.Button(
    app,
    text='Salir',
    font=('Times New Roman',30),
    bg='white',
    fg='black'
).pack(
    fill = tk.BOTH,
    expand=True
)
    
 
tk.mainloop()



