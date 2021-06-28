#from tkinter import *
from tkinter import filedialog,ttk
import modulos1

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

    modulos1.DesasignacionPLL(NroProcesos,Tllegada,TTotal,Duracion,Secuencia)

    print("Secuencia:")                    
    print(Secuencia)
    Secuencia.reverse()

    modulos1.mostrarPLL(NroProcesos,Secuencia,TTotal,TSalida,Tllegada,TPermanencia,DuracionProceso)