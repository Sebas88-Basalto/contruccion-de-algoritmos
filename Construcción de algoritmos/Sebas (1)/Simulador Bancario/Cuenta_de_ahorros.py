__autor__= 'Sebastian Diaz'
__license__ ='gpl'
__version__ ='1.0.0'
__email__= 'sebaslsdy123@gmail.com'

"""----------------------------------------------------------------
# Importaciones
----------------------------------------------------------------"""
class Cuentadeahorros : 
    # Aqui inicia mi clase

    """#-----------------------------------------------------------
    # Atributo
    ---------------------------------------------------------# """
    
    saldo = 0
    interes= 0
    
    """------------------------------------------------------------
    #Metodos
    ------------------------------------------------------------"""
    
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


    __method__ = "RetirarValor"
    __params__ = "Monto"
    __returns__ = "Nada"
    __descriptions__ = "Este método retira un monto a la cuenta"
    
    def RetirarValor(self, monto):
        self.__saldo = self.__saldo-monto

    
    _method_="RetirarAhorro"
    _params_="Monto"
    _returns_="Nada"
    _descriptions_="Este metodo retira un monto del ahorro de la cuenta"   
    
    def RetirarAhorro (self, monto):
        self._ahorro = self._ahorro-monto

    _method_="RetirarTodo"
    _params_="Total"
    _returns_="Nada"
    _descriptions_="Este metodo permite retirar el saldo de la cuenta de ahorros"   
    
    def RetirarTodo (self, total):
      self._saldo = self._saldo-total 

    _method_='DuplicarAhorro'
    _params_='Ninguno'
    _returns_='Ninguno'
    _descriptions_='Permite duplicar el ahorro de la cuenta de ahorrros'

    def DuplicarAhorro(self):
      #Aqui inicia el metodo
      CuentaAhorros = self.DuplicarAhorro()
      return CuentaAhorros*2
    