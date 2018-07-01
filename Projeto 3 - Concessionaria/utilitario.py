from veiculo import *

class Utilitario(Veiculo):

    def __init__(self, fabricante, modelo, capacidade,
                 autonomia, ano, placa, renavam, chassi, reservado):
        Veiculo.__init__(self, fabricante, modelo, autonomia,
                 ano, placa, renavam, chassi, reservado)
        self.capacidade = capacidade
    
    def __repr__(self):
        'Texto simples para ser salvo no banco de dados'
        return ("ute\t" + self.fabricante + "\t" +
                str(self.modelo) + "\t" + str(self.capacidade) + "\t" + 
                str(self.autonomia) + "\t" + str(self.ano) + "\t" + 
                str(self.getPlaca()) + "\t" + str(self.getRENAVAM()) + "\t" + 
                str(self.getChassi()) + "\t" + str(self.getReservado()))

    def __str__(self):
        'Mostrar resumido para listagens'
        reserv = " | Livre"
        if self.getReservado():
            reserv = " | Reservado"
        return (self.getPlaca() + 
                " | " + self.fabricante + " - " + self.modelo + " - " + self.ano + 
                " | " + self.capacidade + " litros" + reserv)
        
    def mostrar(self):
        'Detalhamento de todos atributos do veículo'
        return ("Tipo:\t\tUtilitário" +
                "\nFabricante:\t" + str(self.fabricante) +
                "\nModelo:\t\t" + str(self.modelo) +
                "\nCapacidade:\t" + str(self.capacidade) +
                "\nAutonomia:\t" + str(self.autonomia) +
                "\nAno:\t\t" + str(self.ano) +
                "\nPlaca:\t\t" + str(self.getPlaca()) +
                "\nRENAVAM:\t" + str(self.getRENAVAM()) +
                "\nChassi:\t\t" + str(self.getChassi()) +
                "\nReservado:\t" + str(self.getReservado()))
