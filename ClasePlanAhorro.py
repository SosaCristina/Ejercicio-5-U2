class PlanAhorro:
     __codigo=int
     __modelo=""
     __version=""
     __valor=float
     __cant_cuotas=int
     __cant_cuotas_licitar=int


     def __init__(self,cod,mod,ver,valor,cantC,cantCl):
          self.__codigo=cod
          self.__modelo=mod
          self.__version=ver
          self.__valor=valor
          self.__cant_cuotas=cantC
          self.__cant_cuotas_licitar=cantCl

     def calcular_cuota (self):
           v_cuota=float ((self.__valor/self.__cant_cuotas) + self.__valor * 0.10)
           return v_cuota
     
     def getCodigo(self):
          return self.__codigo
     
     def getModelo(self):
          return self.__modelo
     def getVersion (self):
          return self.__version
     def nuevo_Valor(self,nuevo):
          self.__valor=nuevo
     def getCuotas_Licitar(self):
          return self.__cant_cuotas_licitar
     def getValor(self):
          return self.__valor
     def getValor (self):
          return self.__valor
     def modificar_cuota(self,cuota):
          self.__cant_cuotas_licitar=cuota


     def __str__ (self):
          return 'CODIGO:{}-MODELO:{}-VERSION:{}-VALOR:{}-CANTIDAD CUOTAS:{}-CANTIDAD CUOTAS PARA LICITAR:{}'.format(self.__codigo,self.__modelo,self.__version,self.__valor,self.__cant_cuotas,self.__cant_cuotas_licitar)

     