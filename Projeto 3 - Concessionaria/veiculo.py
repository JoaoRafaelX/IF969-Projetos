
class Veiculo:
    'Classe que serve de base para Carros, Vans e Utilitários'

    def __init__(self, fabricante, modelo, autonomia,
                 ano, placa, renavam, chassi, reservado):
        self.fabricante = fabricante
        self.modelo = modelo
        self.autonomia = autonomia
        self.ano = ano
        self.__placa = placa
        self.__renavam = renavam
        self.__chassi = chassi
        self.__reservado = reservado

    def __eq__(self, outro):
        return (self.getPlaca() == outro)
    def __lt__(self, outro):
        return (self.getPlaca() < outro)    
    def __gt__(self, outro):
        return (self.getPlaca() > outro)

    def __repr__(self):        
        raise NotImplementedError("Não implementado")
    def __str__(self):
        raise NotImplementedError("Não implementado")
    def mostrar(self):
        raise NotImplementedError("Não implementado")

    #Itens privados
    def getTipo(self):
        return type(self).__name__
    def getPlaca(self):
        return self.__placa
    def getRENAVAM(self):
        return self.__renavam
    def getChassi(self):
        return self.__chassi
    def getReservado(self):
        return self.__reservado
    def setReservado(self, reservado):
        self.__reservado = reservado
