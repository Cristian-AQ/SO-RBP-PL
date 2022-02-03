from tkinter import *
from tkinter import filedialog,ttk
raiz = Tk()
raiz.geometry('900x600+0+0')
Label(raiz,text='NO CERRAR ESTA VENTANA, EL BOTON PUEDE ESTAR DETRAS DE ESTA VENTANA',bg='red',font='arial',fg='white').pack()
def CrearProceso(PID,CantidadProcesos,llegada,duracionProceso,duracion,prioridad):
    for i in range(PID):
        CantidadProcesos[i]=list(CantidadProcesos[i].split(','))
    
    for i in range(PID):
        llegada.append(int(CantidadProcesos[i][1]))

    for i in range(PID):
        duracionProceso.append(int(CantidadProcesos[i][2]))
        duracion.append(int(CantidadProcesos[i][2]))
    
    for i in range(PID):
        prioridad.append(int(CantidadProcesos[i][3]))

def Asignacion(PID,duracion):
    TTotal=0
    for i in range(PID):
        TTotal= TTotal + duracion[i]
    return TTotal

def DesasignacionRRB(PID,Tllegada,TTotal,duracion,prioridad,secuencia):
    p=0
    for i in range(TTotal):
        for j in range(PID):
            if p>=Tllegada[j] and duracion[j]>0 and p<=TTotal :
                for k in range(prioridad[j]):
                    if duracion[j]>0:
                        duracion[j]=duracion[j]-1
                        secuencia.append(f"P{j+1}")
                        p=p+1

def mostrarRRB(PID,Secuencia,TTotal,TSalida,Tllegada,TPermanencia,DuracionProceso,prioridad):
    Label(raiz,text='PROCESOS ROUND ROBIN CON PRIORIDADES',bg='blue',font='arial',fg='white').pack()
    material = Listbox(raiz,width=150)
    for i in range(PID):
        nro=Secuencia.index(f"P{i+1}")+1
        nro=TTotal+1-nro
        TSalida.append(nro)
        nro=nro-Tllegada[i]
        TPermanencia.append(nro)
    
    for i in range(PID): 
        material.insert(i,f"P{i+1}--> Tiempo de llegada: {Tllegada[i]}--> Duracion: {DuracionProceso[i]}--> Prioridad: {prioridad[i]}--> Tiempo de Salida: {TSalida[i]}--> Tiempo de Permanencia: {TPermanencia[i]}")
    material.place(x=10,y=150)

def DesasignacionPLL(PID,Tllegada,TTotal,duracion,secuencia):
    p=0
    for i in range(TTotal):
        for j in range(PID):
            if p>=Tllegada[j] and duracion[j]>0 and p<=TTotal :
                for h in range(duracion[j]):
                    if duracion[j]>0:
                        duracion[j]=duracion[j]-1
                        secuencia.append(f"P{j+1}")
                        p=p+1

def mostrarPLL(PID,Secuencia,TTotal,TSalida,Tllegada,TPermanencia,DuracionProceso):
    Label(raiz,text='PRIMERO EN LLEGAR, PRIMERO EN ATENDERCE',bg='yellow',font='arial').pack()
    material = Listbox(raiz,width=150)
    for i in range(PID):
        nro=Secuencia.index(f"P{i+1}")
        nro=TTotal-nro
        TSalida.append(nro)
        nro=nro-Tllegada[i]
        TPermanencia.append(nro)
        
    for i in range(PID):
        material.insert(i,f"P{i+1}--> Tiempo de llegada: {Tllegada[i]}--> Duracion: {DuracionProceso[i]}--> Tiempo de Salida: {TSalida[i]}--> Tiempo de Permanencia: {TPermanencia[i]}")
    material.place(x=10,y=150)