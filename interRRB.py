from tkinter import *
from tkinter import filedialog,ttk
import modulos1
import interPLL
raiz = Tk()

#frame = Frame(raiz,width=1250,height=480)  
#frame.pack()      

def abrirArchivo():
    archivo=filedialog.askopenfile(title='abrir')
    ArchivoText=archivo
    CantidadProcesos=ArchivoText.readlines()
    ArchivoText.close()

    NroProcesos=len(CantidadProcesos)

    Tllegada=[] #Tiempo de llegada
    Duracion=[]
    DuracionProceso=[] #Duracion del proceso
    prioridad=[]

    modulos1.CrearProceso(NroProcesos,CantidadProcesos,Tllegada,DuracionProceso,Duracion,prioridad)
    TTotal = modulos1.Asignacion(NroProcesos,Duracion)

    Secuencia=[]
    TSalida=[] #Tiempo de salida
    TPermanencia=[] #Tiempo de permanencia

    modulos1.DesasignacionRRB(NroProcesos,Tllegada,TTotal,Duracion,prioridad,Secuencia)
    #modulos1.DesasignacionPLL(NroProcesos,Tllegada,TTotal,Duracion,Secuencia)

    print("Secuencia:")                    
    print(Secuencia)
    Secuencia.reverse()

    modulos1.mostrarRRB(NroProcesos,Secuencia,TTotal,TSalida,Tllegada,TPermanencia,DuracionProceso,prioridad)
    #modulos1.mostrarPLL(NroProcesos,Secuencia,TTotal,TSalida,Tllegada,TPermanencia,DuracionProceso)

Button(raiz,text='ROUNDROBIN CON PRIORIDAD',command=abrirArchivo).pack()
Button(raiz,text='PRIMERO EN LLEGAR',command=interPLL.abrirArchivo).pack()
raiz.mainloop()