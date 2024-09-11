__autor__= 'Sebastian Diaz'
__license__ ='gpl'
__version__ ='1.0.0'
__email__= 'sebaslsdy123@gmail.com'

"""------------------------------------------------------
# Importaciones
------------------------------------------------------"""
class cdt:
    # Aqui inicia mi clase

    """-----------------------------------------------------------
    # Atributo
    ---------------------------------------------------------- """
    
    inversion = 0
    interes= 0
    fecha= 0
    
    """------------------------------------------------------- 
    # Metodos
    --------------------------------------------------------"""
    
    __method__ = "Cambiarinteres"
    __params__ = "Nuevointeres"
    __returns__ = "Nada"
    __descriptions__ = "Este metodo permite establecer el valor del interes"
    
    def CambiarInteres(self, nuevoInteres): 
        #Aqui inicia mi metodo
        self.interes = nuevoInteres
        
        __method__="DarInteres"
        __params__="Nada"
        __returns__="El valor del interes"
        __descriptions__ = "Devuelve el valor actual del interés establecido para el CDT"

    def DarInteres(self):
        # Aquí inicia el método
        return self.interes
    