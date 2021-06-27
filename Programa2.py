from io import open # Del modulo io, importamos el metodo open para poder abrir un archivo externo

ArchivoText=open("DatosIngreso.txt","r") #Para leer los datos del archivo de texto
CantidadProcesos=ArchivoText.readlines()
ArchivoText.close()

NroProcesos=len(CantidadProcesos)

for i in range(NroProcesos):
    CantidadProcesos[i]=list(CantidadProcesos[i].split(',')) #Convertimos la cadena en una lista de caracteres
print(CantidadProcesos)

Tllegada=[] #Tiempo de llegada
for i in range(NroProcesos):
    Tllegada.append(int(CantidadProcesos[i][1]))
print(Tllegada)

DuracionProceso=[] #Duracion del proceso
Duracion=[]
for i in range(NroProcesos):
    DuracionProceso.append(int(CantidadProcesos[i][2]))
    Duracion.append(int(CantidadProcesos[i][2]))
print(Duracion)
print(DuracionProceso)
D1 = Duracion.copy()
print(D1)

TTotal=0 #Tiempo Total
for i in range(NroProcesos):
    TTotal= TTotal + Duracion[i]
print(TTotal)

Secuencia=[]
TSalida=[] #Tiempo de salida
TPermanencia=[] #Tiempo de permanencia
p=0
for i in range(TTotal):
    for j in range(NroProcesos):
        if p>=Tllegada[j] and Duracion[j]>0 and p<=TTotal :
            for h in range(Duracion[j]):
                if Duracion[j]>0:
                    Duracion[j]=Duracion[j]-1
                    Secuencia.append(f"P{j+1}")
                    p=p+1
print("Secuencia:")                    
print(Secuencia)
print(TSalida)
print(TPermanencia)

tiempo = []

a=1
while(a<TTotal):
    p=0
    for i in Secuencia:
        if f'{a}' in i:
            p = p+1
    tiempo.append(p)
    a = a+1

t1 = 0
tiempoSalida = []
for i in tiempo:
    t1 = t1 + i
    if i == 0:
        break
    else:
        tiempoSalida.append(t1)
        print(t1)
print(Tllegada)

for i in range(5):
    b = 0
    b = tiempoSalida[i]-Tllegada[i]
    print(b) 