import tkinter as tk 

app = tk.Tk()

app.geometry('200x500')
app.config(background='black')
tk.Wm.wm_title(app,'Hola')

def saludar():
    print('hola crack')
tk.Button(
    
    app,
    text = ('CLICK'),
    font = ('Italic',25),
    bg='#C9533A',
    fg='#ECE4E2',
    command = saludar,

).pack(
    fill = tk.BOTH,
    
)
tk.Label(
    app,
    text='I´m a etiket',
    font = ('Arial',24),
    bg='#66B956',
    fg= '#050505',

).pack(
    fill = tk.BOTH,
    expand= True
)
app.mainloop()