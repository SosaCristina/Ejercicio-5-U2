from ClasePlanAhorro import PlanAhorro
import csv

class Manejador:
    __listaPlan=[]
    def __init__(self):
        self.__listaPlan=[]

    def agregar (self, unPlan):
        self.__listaPlan.append(unPlan)    

    def  CrearLista (self):
        archivo=open('C:\\Users\\chili\\POO archivos\\planes.csv')
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
           cod=int(fila[0])
           modelo=fila[1]
           version=fila[2]
           valor=float(fila[3])
           cant_cuotas=int(fila[4])
           cantC_licitar=int(fila[5])
           unPlan=PlanAhorro(cod,modelo,version,valor,cant_cuotas,cantC_licitar)
           self.agregar(unPlan)
        archivo.close()

    def __str__(self):
        s=""
        for lista in self.__listaPlan:
            s += str(lista) + '\n'
        return s
    
    def modificar_valor (self):
        
        for lista in self.__listaPlan:
            print ("Codigo:{} - Modelo:{} - Version:{}".format(lista.getCodigo(),lista.getModelo(),lista.getVersion()))
            nuevo_valor=input("Ingresar nuevo valor:")
            lista.nuevo_Valor(nuevo_valor)
            print("Valor actualizado:{}".format(lista.getValor()))

    
    def opcion2 (self, num):
        for lista in self.__listaPlan:
            if (num>lista.calcular_cuota()):
                print("Codigo:{}-Modelo:{}-Version:{}".format(lista.getCodigo(),lista.getModelo(),lista.getVersion()))

    def buscar (self,cod):
        indice=0
        valorderetorno=None
        bandera=False
        while not bandera and indice<len(self.__listaPlan):
            if(self.__listaPlan[indice].getCodigo()==cod):
                bandera=True
                valorderetorno=indice
            else: 
                indice+=1
        return valorderetorno           

    def opcion3 (self, i):
        
        calcular= (self.__listaPlan[i].getCuotas_Licitar()* self.__listaPlan[i].getValor())
        print("El monto que se debe haber pagado es:",calcular)

    def opcion4(self,i):
        cuota=int(input("Ingresar nueva cantidadde cuotas para licitar"))
        self.__listaPlan[i].modificar_cuota(cuota)
        print("Cantidad de cuotas actualizada:{}".format(self.__listaPlan[i].getCuotas_Licitar()))

