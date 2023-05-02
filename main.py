from ClasePlanAhorro import PlanAhorro
from ManejadorPlanAhorro import Manejador
import csv

if __name__=="__main__":
    unPlan=Manejador()
    unPlan.CrearLista()
    print(unPlan)


    opcion=0
    def menu():
       opc=int(input("Menu Principal\n"+
       "1)Actualizar valor de vehiculo de cada plan\n"+
       "2)Mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.\n"+
       "3)Mostrar el monto que se debe haber pagado para licitar el vehículo\n"+
       "4)Modificar la cantidad cuotas que debe tener pagas para licitar.\n"+
       "5)Finalizar\n"+
       "Seleccione una opcion\n"))
       return opc
    while opcion!=5:
       opcion=menu()
       if opcion==1:
          unPlan.modificar_valor()
       if opcion==2:
          num=float(input("Ingresar valor:"))
          unPlan.opcion2(num)
       if opcion==3:
          cod=int(input("Ingresar codigo de plan que desee calcular el monto para licitarlo:"))
          i=unPlan.buscar(cod)
          unPlan.opcion3(i)
       if opcion==4:
          codigo=int(input("Ingresar codigo de plan para modificar la cantidad de cuotas para licitar:"))
          i=unPlan.buscar(codigo)
          unPlan.opcion4(i)   
        