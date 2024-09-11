__autor__= 'Sebastian Diaz'
__license__ ='gpl'
__version__ ='1.0.0'
__email__= 'sebaslsdy123@gmail.com'
"""------------------------------------------------------
# Importaciones
------------------------------------------------------"""

class Cuentacorriente: 
    # Aqui inicia mi clase

    """-----------------------------------------------------------
    # Atributo
    ---------------------------------------------------------- """
    
    __saldo = 0
     
    """-----------------------------------------------------------
    # Métodos
    -----------------------------------------------------------"""
    
    __method__ = "ConsignarValor"
    __params__ = "Monto"
    __returns__ = "Nada"
    __descriptions__ = "Este método me permite consignar un monto a la cuenta."
    
    def ConsignarValor(self, monto):
        self.__saldo = self.__saldo+monto


    __method__ = "DarSaldo"
    __params__ = "Ninguno"
    __returns__ = "Saldo"
    __descriptions__ = "Este método retorna el saldo"
    
    def DarSaldo(self):
        return self.__saldo


    
    _method_="RetirarValor"
    _params_="Monto"
    _returns_="Nada"
    _descriptions_="Este metodo retira un monto de la cuenta"   
    
    def RetirarValor (self, monto):
        self._saldo = self._saldo-monto

    _method_="Ahorrar"
    _params_="Monto"
    _returns_="Ninguno"
    _descriptions_="Este metodo permite pasar el ahorro de la cuenta corriente a la cuenta de ahorros"  

    def Ahorrar (self, monto):
        saldoTemporal = self.__cuentaAhorros.DarAhorro()
        self.__cuentaAhorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.consignarValor(saldoTemporal)

    _method_="DarSaldoCorriente"
    _params_="Ninguno"
    _returns_="Saldo"
    _descriptions_="Este metodo retorna el saldo que hay en la cuenta corriente"   
    
    def DarSaldoCorriente (self):
        return self.__saldo

    _method_="RetirarTodo"
    _params_="Total"
    _returns_="Nada"
    _descriptions_="Este metodo permite retirar todo el saldo de la cuenta corriente"   
    
    def RetirarTodo (self, total):
        self._saldo = self._saldo-total


        
    
   


