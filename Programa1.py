from io import open # Del modulo io, importamos el metodo open para poder abrir un archivo externo
import modulos1

ArchivoText=open("DatosIngreso.txt","r") #Para leer los datos del archivo de texto
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

modulos1.Desasignacion(NroProcesos,Tllegada,TTotal,Duracion,prioridad,Secuencia)

print("Secuencia:")                    
print(Secuencia)
Secuencia.reverse()

modulos1.mostrar(NroProcesos,Secuencia,TTotal,TSalida,Tllegada,TPermanencia,DuracionProceso,prioridad)