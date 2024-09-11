__autor__= 'Sebastian Diaz'
__license__ ='gpl' 'codigolibre'
__version__ ='1.0.0'
__email__= 'sebaslsdy123@gmail.com'

'''------------------------------------------
#Importaciones
------------------------------------------'''

from Cuenta_corriente import Cuentacorriente
from Cuenta_de_ahorros import Cuentadeahorros
from  Cdt import cdt

class SimuladorBancario:
    # aqui inicia la declaracion de la clase 

    """-----------------------------------------
    # Atributos
    -----------------------------------------"""

    __nombre = ''
    __cedula = ''

    '''------------------------------------------
    #Asociaciones
    -------------------------------------------'''

    __cuentacorriente = Cuentacorriente()
    __Cuentadeahorros = Cuentadeahorros()
    __cdt = cdt()
    
    __mesActual = 0

    '''--------------------------------------------
    # Métodos
    ---------------------------------------------'''
    __method__ = "ConsignarCuentaCorriente"
    __params__ = "Monto"
    __returns__= "Nada"
    __descriptions__= "Este metodo permite consignar un monto a la cuenta corriente"
    
    def ConsignarCuentaCorriente(self, monto):
        # Aqui inicia mi metodo 
        #self.__cuentaCorriente.saldo = self.__cuentaCorriente.saldo+monto # modo no recomendable

        self.__cuentaCorriente.ConsignarValor(monto)
        
    __method__ = "CalcularSaldoTotal"
    __params__ = "Ninguno"
    __returns__= "Saldo Total"
    __descriptions__= "Este metodo suma el saldo de todas las cuentas"
    
    def CalcularSaldoTotal(self,):
        #Aqui inicia el metodo
        # forma 1
        total= self.__cuentacorriente.Darsaldo()+self.__Cuentadeahorros.DarSaldo()
        return total
    
    
    __method__ = "PasarAhorrosACorriente"
    __params__ = "Ninguno"
    __returns__= "Ninguno"
    __descriptions__= "Este metodo transfiere el saldo de ahorros a corriente"
    
    def PasarAhorrosACorriente(self):
        saldoTemporal= self.__Cuentadeahorros.DarSaldo()
        self.__Cuentadeahorros.RetirarValor(saldoTemporal)
        self.__cuentacorriente.ConsignarValor(saldoTemporal)
        
    __method__ = "Ahorrar"
    __params__ = "Monto"
    __returns__= "Ninguno"
    __descriptions__= "Este metodo permite pasar  el saldo de corriente a ahorros"
    
    def Ahorrar (self, monto):
        self.__cuentacorriente.DarSaldo()
        self.__cuentacorriente.Retirarvalor(monto)
        self.__Cuentadeahorros.ConsignarValor(monto)

    #Metodo del profe :
    __metho__ = "Ahorrar"
    __params__ = "Monto"
    __returns__= "Ninguno"
    __descriptions__= "Este metodo permite pasar  el saldo de corriente a ahorros"
    
    def Ahorrar (self, monto):
        self.__cuentacorriente.Retirarvalor(monto)
        self.__Cuentadeahorros.ConsignarValor(monto)

    _method_="RetirarTodo"
    _params_="Ninguno"
    _returns_="Cantidad retirada"
    _descriptions_="Rtira todo el dinero que hay en la cuenta corriente y em la cuenta de ahorro"   
    
    def RetirarTodo (self):
        total = self.__cuentacorriente.Darsaldo() + self.__Cuentadeahorros.DarSaldo
        self.__Cuentadeahorros.RetirarValor(self.__Cuentadeahorros.DarSaldo())
        self.__cuentacorriente.RetirarValor(self.__cuentacorriente.DarSaldo())
        return 'Usted acaba de retirar' +total


    _method_="DuplicarAhorro"
    _params_="Ninguno"
    _returns_="Ninguno"
    _descriptions_="Duplicar la cantidad de dinero que hay en la cuenta de ahorros"   
    
    def duplicarAhorro (self):
        self.__Cuentadeahorros.ConsignarValor(self.__Cuentadeahorros.DarSaldo())