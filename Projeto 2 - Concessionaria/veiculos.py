from carro import *
from van import *
from utilitario import *

class Veiculos:
    'Classe que faz as operações no banco de dados gerado'

    def __init__(self):
        self.__lista = []

    def inserir(self, item):
        'Pega um veiculo já pronto e simplesmente insere-o na lista'
        if item:
            self.__lista.append(item)

    def buscar(self, atributo, alvo, varios = False, reservado = False):
        '''Método que procura um item específico, devolvendo-o com seu índice
        Varios: Pesquisar todos itens de certo tipo, devolvendo uma lista de itens
        Reservado: Incluir os veículos já reservados na pesquisa'''
        todos = []
        for i in range(len(self.__lista)):
            #Caso 3
            if reservado or (not self.__lista[i].getReservado()):
                if atributo(self.__lista[i]) == alvo:
                    if not varios:
                        #Caso 1
                        return self.__lista[i], i
                    #Caso 2
                    todos.append(self.__lista[i])
        return todos

    def getItem(self, indice):
        'Devolve um item de acordo com seu índice, obtido pelo Buscar'
        return self.__lista[indice]
    
    def atualizarReserva(self, indice, reserva):
        'Altera a reserva de um item específico'
        self.__lista[indice].setReservado(reserva)

    def getTamanho(self):
        return len(self.__lista)


