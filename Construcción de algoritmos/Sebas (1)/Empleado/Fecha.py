__autor__="Sebastian Diaz"
__licence__="GPL"
__version__="1.0.0"
__email__="sebaslsdy123@gmial.com"

"""------------------------------------------------------
# Importaciones
------------------------------------------------------"""


class Fecha:
    # Aqui inicia mi clase

    """#-----------------------------------------------------------
    # Atributo
    ---------------------------------------------------------# """

    dia = 0
    mes = 0
    anio = 0
    """------------------------------------------------------------
    # Metodos
    ------------------------------------------------------------"""
    __method__="CambiarFecha"
    __params__="nuevaFecha"
    __returns__="Nada"
    __descriptions__="Este metodo permite cambiar la fecha por una nueva"
    def CambiarFecha(self, nuevaFecha):
        # Aqui inicia mi metodo 
        self.Fecha = nuevaFecha
    
    __method__="DarFecha"
    __params__="Ninguno"
    __returns__="Dar fecha"
    __descriptions__="Permite dar la fecha cambiada"   
    def DarFecha(self):
        # Aqui inicia el metodo
        return self.dia+'/'+self.mes+'/'+self.anio

   

    __method__= "DarDia"
    __params__="Ninguno"
    __returns__="Dia de la clase"
    __descriptions__="devuelve el dia de la clase"

    def Dardia(self):
        return self.dia 
    
   
    __method__= "DarMes"
    __params__="Ninguno"
    __returns__="Mes de la clase"
    __descriptions__="devuelve el mes de la clase"

    def Darmes(self):
        return self.mes 
   
   
    __method__= "DarAnio"
    __params__="Ninguno"
    __returns__="Año de la clase"
    __descriptions__="devuelve el año de la clase"

    def DarAnio(self):
        return self.anio
    

