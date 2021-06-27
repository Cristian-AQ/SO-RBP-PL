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

def Desasignacion(PID,Tllegada,TTotal,duracion,prioridad,secuencia):
    p=0
    for i in range(TTotal):
        for j in range(PID):
            if p>=Tllegada[j] and duracion[j]>0 and p<=TTotal :
                for k in range(prioridad[j]):
                    if duracion[j]>0:
                        duracion[j]=duracion[j]-1
                        secuencia.append(f"P{j+1}")
                        p=p+1

def mostrar(PID,Secuencia,TTotal,TSalida,Tllegada,TPermanencia,DuracionProceso,prioridad):
    for i in range(PID):
        nro=Secuencia.index(f"P{i+1}")+1
        nro=TTotal+1-nro
        TSalida.append(nro)
        nro=nro-Tllegada[i]
        TPermanencia.append(nro)
    
    for i in range(PID): 
        print(f"P{i+1}" , f"--> Tiempo de llegada: {Tllegada[i]}", f"-- Duracion: {DuracionProceso[i]}", f"-- Prioridad: {prioridad[i]}", f"-- Tiempo de Salida: {TSalida[i]}",f"-- Tiempo de Permanencia: {TPermanencia[i]}" ) #Lo que se imprimira