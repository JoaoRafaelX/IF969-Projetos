from veiculo import *

class Carro(Veiculo):

    def __init__(self, fabricante, modelo, portas,
                 autonomia, ano, placa, renavam, chassi, reservado):
        Veiculo.__init__(self, fabricante, modelo, autonomia,
                 ano, placa, renavam, chassi, reservado)
        self.portas = portas
    
    def __repr__(self):
        'Texto simples para ser salvo no banco de dados'
        return ("carro\t" + self.fabricante + "\t" +
                self.modelo + "\t" + self.portas + "\t" +
                self.autonomia + "\t" + self.ano + "\t" +
                self.getPlaca() + "\t" + self.getRENAVAM() + "\t" +
                self.getChassi() + "\t" + str(self.getReservado()))

    def __str__(self):
        'Mostrar resumido para listagens'
        reserv = " | Livre"
        if self.getReservado():
            reserv = " | Reservado"            
        return (self.getPlaca() + 
                " | " + self.fabricante + " - " + self.modelo + " - " + self.ano + 
                " | " + self.portas + " portas" + reserv)
    
    def mostrar(self):
        'Detalhamento de todos atributos do veículo'
        return ("Tipo:\t\tCarro" +
                "\nFabricante:\t" + str(self.fabricante) +
                "\nModelo:\t\t" + str(self.modelo) +
                "\nPortas:\t\t" + str(self.portas) +
                "\nAutonomia:\t" + str(self.autonomia) +
                "\nAno:\t\t" + str(self.ano) +
                "\nPlaca:\t\t" + str(self.getPlaca()) +
                "\nRENAVAM:\t" + str(self.getRENAVAM()) +
                "\nChassi:\t\t" + str(self.getChassi()) +
                "\nReservado:\t" + str(self.getReservado()))



    
