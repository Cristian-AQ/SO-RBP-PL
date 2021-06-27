from tkinter import *
from tkinter import filedialog,ttk

raiz = Tk()

frame = Frame(raiz,width=1250,height=480)  
frame.pack()      

def abrirArchivo():
    archivo=filedialog.askopenfile(title='abrir')
    ArchivoText=archivo
    CantidadProcesos=ArchivoText.readlines()
    ArchivoText.close()


    NroProcesos=len(CantidadProcesos)

    for i in range(NroProcesos):
        CantidadProcesos[i]=list(CantidadProcesos[i]) #Convertimos la cadena en una lista de caracteres
        Label(raiz,text=CantidadProcesos[i]).pack()

    Tllegada=[] #Tiempo de llegada
    for i in range(NroProcesos):
        Tllegada.append(int(CantidadProcesos[i][4]))
        Label(raiz,text=Tllegada[i]).pack()
    #print(archivo)

Label(raiz,text='ROUNDROBIN').pack()
Button(raiz,text='Abrir Archivo',command=abrirArchivo).pack()

arbol = ttk.Treeview(raiz,columns=('a','b','c','d','e'))
arbol.heading('#0',text='Proceso')
arbol.heading('a',text='Tllegada')
arbol.heading('b',text='Duracion')
arbol.heading('c',text='Prioridad')
arbol.heading('d',text='Tsalida')
arbol.heading('e',text='TPermanencia')
arbol.place(x=10,y=10)

raiz.mainloop()