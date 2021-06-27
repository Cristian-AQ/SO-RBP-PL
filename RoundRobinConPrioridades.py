from io import open # Del modulo io, importamos el metodo open para poder abrir un archivo externo

ArchivoText=open("DatosIngreso.txt","r") #Para leer los datos del archivo de texto
CantidadProcesos=ArchivoText.readlines()
ArchivoText.close()

NroProcesos=len(CantidadProcesos)

for i in range(NroProcesos):
    CantidadProcesos[i]=list(CantidadProcesos[i]) #Convertimos la cadena en una lista de caracteres

Tllegada=[] #Tiempo de llegada
for i in range(NroProcesos):
    Tllegada.append(int(CantidadProcesos[i][4]))

DuracionProceso=[] #Duracion del proceso
Duracion=[]
for i in range(NroProcesos):
    DuracionProceso.append(int(CantidadProcesos[i][6]))
    Duracion.append(int(CantidadProcesos[i][6]))
  
prioridad=[]
for i in range(NroProcesos):
    prioridad.append(int(CantidadProcesos[i][8]))


TTotal=0 #Tiempo Total
for i in range(NroProcesos):
    TTotal= TTotal + Duracion[i]

Secuencia=[]
TSalida=[] #Tiempo de salida
TPermanencia=[] #Tiempo de permanencia
p=0
for i in range(TTotal):
    for j in range(NroProcesos):
        if p>=Tllegada[j] and Duracion[j]>0 and p<=TTotal :
            for k in range(prioridad[j]):
                if Duracion[j]>0:
                    Duracion[j]=Duracion[j]-1
                    Secuencia.append(f"P{j+1}")
                    p=p+1
print("Secuencia:")                    
print(Secuencia)
Secuencia.reverse()
for i in range(NroProcesos):
    nro=Secuencia.index(f"P{i+1}")+1
    nro=TTotal+1-nro
    TSalida.append(nro)
    nro=nro-Tllegada[i]
    TPermanencia.append(nro)
    
for i in range(NroProcesos): 
    print(f"P{i+1}" , f"--> Tiempo de llegada: {Tllegada[i]}", f"-- Duracion: {DuracionProceso[i]}", f"-- Prioridad: {prioridad[i]}", f"-- Tiempo de Salida: {TSalida[i]}",f"-- Tiempo de Permanencia: {TPermanencia[i]}" ) #Lo que se imprimira