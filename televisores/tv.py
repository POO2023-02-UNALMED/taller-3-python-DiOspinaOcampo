class TV:
    _estado: bool
    _canal: int = 1
    _volumen: int = 1
    _precio: int = 500
    numTV: int = 0
    
    def __init__(self, marca, estado: bool):
        self._marca = marca
        self._estado = estado
        TV.numTV += 1
        
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca
        
    def getCanal(self):
        return self._canal
    
    def setCanal(self, canal: int):
        if(self._estado and canal <= 120 and canal >= 1):
            self._canal = canal
        
    def getPrecio(self):
        return self._precio
        
    def setPrecio(self, precio: int):
        self._precio = precio
        
    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen: int):
        if(self._estado and volumen >=0 and volumen <=7):
            self._volumen = volumen
    
    def getControl(self):
        return self._control
    
    def setControl(self, control):
        self._control = control
        
    def getNumTV():
        return TV.numTV
       
    def setNumTV(numTV: int):
        TV.numTV = numTV
        
    def getEstado(self):
        return self._estado
        
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        if(self._estado and self._canal < 120):
            self._canal += 1

    def canalDown(self):
        if(self._estado and self._canal > 1):
            self._canal -= 1

    def volumenUp(self):
        if(self._estado and self._volumen < 7):
            self._volumen += 1

    def volumenDown(self):
        if(self._estado and self._volumen > 0):
            self._volumen -= 1