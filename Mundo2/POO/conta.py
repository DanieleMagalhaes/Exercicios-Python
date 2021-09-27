class Conta: 
    #construtor
    def __init__(self, numConta, tipo, __dono, __saldo, __status):
        self.numConta = numConta
        self.tipo = tipo
        self.__dono = ''
        self.__saldo = 0
        self.__status = False
    
    #modificar
    def setNumConta(self, numConta):
        self.numConta = numConta
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def setDono(self, dono):
        self.dono = dono
    
    def setSaldo (self, saldo):
        self.saldo = saldo

    def setStatus (self, status):
        self.status = status
    
    #capturar
    def getNumConta(self):
        return self.numConta 
    
    def getTipo(self):
        return self.tipo
    
    def getDono(self):
        return self.__dono 
    
    def getSaldo (self):
        return self.__saldo

    def getStatus (self):
        return self.__status



