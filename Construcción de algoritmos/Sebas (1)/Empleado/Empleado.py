__autor__="Sebastian Diaz"
__licence__="GPL"
__version__="1.0.0"
__email__="sebaslsdy123@gmail.com"

"""------------------------------------------------------
# Importaciones
------------------------------------------------------"""
from Fecha import Fecha

class Empleado:
    # Aqui inicia mi clase

    """#-----------------------------------------------------------
    # Atributo
    ---------------------------------------------------------# """

    nombre = ""
    apellido = ""
    salario = 0

    """#-----------------------------------------------------------
    # 1 Masculino y 2 Femenino
    ---------------------------------------------------------# """

    sexo = 0

    """#-----------------------------------------------------------
    # Asociaciones
    ------------------------------------------------------------#"""

    fechaNacimiento = Fecha()
    fechaIngreso =  Fecha()
    fechaCumpleaños = Fecha()
    """------------------------------------------------------------
    # Metodos
    ------------------------------------------------------------"""   
    __method__="CambiarSalario"
    __params__="nuevoSalario"
    __returns__="Nada"
    __descriptions__="Este metodo permite cambiar el salario del empleado por uno nuevo"
    def CambiarSalario(self, nuevoSalario):
        # Aqui inicia mi metodo 
        self.salario = nuevoSalario
    
    __method__="DarSalario"
    __params__="Ninguno"
    __returns__="Salario empleado"
    __descriptions__="Devuelve el salario del empleado"   
    def DarSalario(self):
        # Aqui inicia el metodo
        return self.salario
    
    __method__="AumentoSalarial"
    __params__="Aumento"
    __returns__="Ninguno"

    __descriptions__="Permite aumentar el salario en un valor ingresado por el usuario  "  

    def AumentoSalarial(self, aumento):
        #aqui inicia el metodo
        self.salario = self.salario+aumento 
  

    __method__="CalcularSalarioAnual"
    __params__="Ninguno"
    __returns__="Salario anual"
    __descriptions__="Permite calcular el salario anual del empleado"   

    def CalcularSalarioAnual(self):
        return self.salario*12
    
    __method__="CalcularImpuestoSalarioAnual"
    __params__="Ninguno"
    __returns__="Impuesto del salario anual"
    __descriptions__="Permite calcular el impuesto a el salario anual del empleado"  

    def CalcularImpuestoSalarioAnual(self):
       #Aqui inicia mi metodo
        salarioAnual = self.CalcularSalarioAnual()
        return salarioAnual*0.19
    
    
    __method__="CalcularImpuestoSalario"
    __params__="Ninguno"
    __returns__="Impuesto del salario"
    __descriptions__="Permite calcular el impuesto a el salario del empleado"  

    def CalcularImpuestoSalario(self):
        #Aqui inicia mi metodo
        # forma 1
        # return self.salario*0.19
        # forma 2
        return self.DarSalario()*0.19
    
    __method__="DarFechaIngreso"
    __params__="Ninguno"
    __returns__="Fecha de ingreso"
    __descriptions__="Muestra la fecha de ingreso del empleado"  

    def DarFechaIngreso(self):
        #Aqui inicia mi metodo
        return self.fechaIngreso.Darfecha()
    
    __method__="DarFechaNacimiento"
    __params__="Ninguno"
    __returns__="Fecha de Nacimiento"
    __descriptions__="Muestra la fecha de nacimiento del empleado"  

    def DarFechaNacimiento(self):
        #Aqui inicia mi metodo
        return 'Tu fecha de nacimiento es: '+self.fechaNacimiento.Darfecha()
    
    
    
    
