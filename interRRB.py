from tkinter import *
from tkinter import filedialog,ttk
import modulos1
import interPLL
raiz = Tk()

def abrirArchivo():
    archivo=filedialog.askopenfile(title='abrir')
    ArchivoText=archivo
    CantidadProcesos=ArchivoText.readlines()
    ArchivoText.close()

    NroProcesos=len(CantidadProcesos)

    Tllegada=[]
    Duracion=[]
    DuracionProceso=[]
    prioridad=[]

    modulos1.CrearProceso(NroProcesos,CantidadProcesos,Tllegada,DuracionProceso,Duracion,prioridad)
    TTotal = modulos1.Asignacion(NroProcesos,Duracion)

    Secuencia=[]
    TSalida=[]
    TPermanencia=[]

    modulos1.DesasignacionRRB(NroProcesos,Tllegada,TTotal,Duracion,prioridad,Secuencia)

    print("Secuencia:")                    
    print(Secuencia)
    Secuencia.reverse()

    modulos1.mostrarRRB(NroProcesos,Secuencia,TTotal,TSalida,Tllegada,TPermanencia,DuracionProceso,prioridad)

Button(raiz,text='ROUNDROBIN CON PRIORIDAD',command=abrirArchivo).pack()
Button(raiz,text='PRIMERO EN LLEGAR',command=interPLL.abrirArchivo).pack()
raiz.mainloop()