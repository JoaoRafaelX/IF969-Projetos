'''
Universidade Federal de Pernambuco
Discente: João Rafael
Disciplina: Algoritmos e Estruturas de Dados
Data: 10/09/2017
Atividade: Projeto 2
'''

from controle import *
from relogio import *

class Interface:
    'Classe que interage com o usuário'

    def __init__(self):
        self.arquivoAtual = "veiculos.txt"
        self.controle = Controle(None)

    def run(self):    
        self.escolherArquivo()
        self.menu()

    def menu(self):
        'Método principal da classe Interface'
        while True:    
            print("\n"*20)        
            print("Bem vindo ao sistema de aluguel de veículos da Empresa Inter e-Sada!\n"+
                  "O que deseja fazer?\n\n"+
                  "1. Registrar um novo veículo\n"+
                  "2. Procurar por um veículo específico\n"+
                  "3. Recuperar quantidade de veículos\n"+
                  "4. Listar veículos de um certo tipo\n"+
                  "5. Reservar um veículo\n"+
                  "6. Cancelar uma reserva\n"+
                  "7. Carregar um arquivo de banco de dados\n"+
                  "8. Salvar arquivo de banco de dados\n"+
                  "9. Sair\n")

            switch = {"1": self.registrar,
                      "2": self.procurar,
                      "3": self.listar,
                      "4": self.listar,
                      "5": self.reservar,
                      "6": self.reservar,
                      "7": self.escolherArquivo,
                      "8": self.escreverArquivo,
                      "9": self.sair}
            
            comando = input("Escolha: ")
            print("\n"*15)

            #Executa a operação do dicionário com o número do comando no construtor
            operacao = switch.get(comando, None)
            #Caso não exista, simplemente recomeçará o loop
            if operacao:
                if operacao(int(comando)):
                    #Caso o método devolva True, o programa encerra
                    #Único caso é o método Sair
                    break
                
            
    def escolherArquivo(self, comando = ""):
        '''Método que permite a leitura do arquivo, seja ele padrão ou um novo escolhido pelo usuário
        Chamado tanto pelo menu, quanto no método inicial da Interface'''
        print("Digite o nome do arquivo de banco de dados desejado")
        print("Caso deseje cancelar ou usar o arquivo padrão, pressione Enter")
        arquivo = input()        
        if arquivo:
            rel = Relogio()
            self.controle = Controle(arquivo)
            del rel
            self.arquivoAtual = arquivo
            input("Banco de dados alterado com sucesso.")
        #Comando é true quando o método foi chamado pelo menu
        #Quando chamado pelo menu, a operação é cancelada
        elif not comando:
            rel = Relogio()
            #Mas quando é chamada no método inicial, o arquivo padrão é lido, "veiculos.txt"
            self.controle = Controle(self.arquivoAtual)
            del rel
            input("Banco de dados lido com sucesso.")
            

    def escreverArquivo(self, comando = ""):
        '''Método usado para salvar a lista em um arquivo, seja o atual ou um novo
        Somente chamado pelo menu'''
        print("Digite o nome (com extensão) do arquivo que deseja criar")
        print("Note que isso irá substituir o arquivo caso ele já exista")
        print("Deixe em branco para cancelar")
        arquivo = input()
        print("\n")
        if arquivo:
            rel = Relogio()
            self.controle.escreverArquivo(arquivo)
            del rel
            #Muda o arquivo do objeto Controle utilizado
            self.controle.arquivo = arquivo
            input("Arquivo salvo com sucesso.")
            

    def registrar(self, comando = ""):
        'Método que recebe os dados para inserção de um veículo no banco de dados'
        #A maior parte desse método é simplesmente cosmética
        print("Para cancelar, deixe algum campo com * em branco\n")
        switch = {"1": ["carro", "Portas"],
                  "2": ["van", "Capacidade"],
                  "3": ["ute", "Capacidade"]}
        print("Qual o Tipo* do veículo?")
        print("1. Carro \n2. Van \n3. Utilitário")
        tipo = switch.get(input("Escolha: "), None)
        if tipo:
            atributos = ["Fabricante", "Modelo", tipo[1], "Autonomia", "Ano",
                         "Placa*", "RENAVAM*", "Chassi*"]
            lista = []
            dado = "."
            i = 0
            while dado and not i == 8:
                dado = input("\n" + atributos[i] + "\n")
                #Caso não seja um dado crucial e esteja em branco...
                #Transforma-o em um . para melhorar a visibilidade no arquivo
                if not dado:
                    if i > 4:
                        break
                    dado = "."
                lista.append(dado)
                i += 1
            if i == 8:
                print("\n")                
                rel = Relogio()
                #Vai mandar o tipo do veículo e seus dados em uma lista para o Controle
                self.controle.inserir(tipo[0], lista)
                #Então salvar o banco de dados no arquivo atual
                self.controle.escreverArquivo(self.arquivoAtual)
                del rel
                input("Veículo registrado com sucesso.")
                
                
    def procurar(self, comando):
        'Método que pesquisa um veículo de acordo com um dos dados'
        print("Para cancelar, pressione Enter\n")
        switch = {"1": "Placa", "2": "RENAVAM", "3": "Chassi"}
        print("Por qual dado deseja pesquisar?")
        print("1. Placa \n2. Renavam \n3. Chassi")
        #Escolha do dado usado na pesquisa
        tipo = switch.get(input("Escolha: "), "")
        if tipo:            
            dado = input("\n"+tipo+":\n")
            if dado:
                print("\nDeseja incluir os reservados na pesquisa?")
                reservados = bool(input("Deixe vazio para [Não]\n"))                
                rel = Relogio()
                #Mostra o veículo encontrado
                self.mostrarVeiculos(self.controle.pesquisar(tipo, dado, False, reservados)[0])
                print("\n")
                del rel
                input("Pesquisa realizada com sucesso.")
                
                
    def listar(self, comando):
        '''Método que age similarmente ao procurar()
        Mas utilizado para pesquisar vários veículos de uma vez
        Seja só uma contagem ou listagem'''
        print("Para cancelar, pressione Enter\n")        
        switch = {"0": "*", "1": "Carro", "2": "Van", "3": "Utilitario"}
        print("Que categoria deseja utilizar?")
        print("0. Todos\n1. Carros\n2. Vans\n3. Utilitários")
        dado = switch.get(input("Escolha: "), "")        
        if dado:
            print("\nDeseja incluir os reservados na pesquisa?")
            reservados = bool(input("Deixe vazio para [Não]\n"))
            print("\n\n")
                
            rel = Relogio()
            resultado = self.controle.pesquisar("Categoria", dado, True, reservados)            
            #Comando de contar quantos veículos de algum tipo existem no banco de dados
            if comando == 3:
                print(len(resultado), "veículos encontrados\n")
            del rel
            input("Pesquisa realizada com sucesso.\n")
            
            #Comando de listar veículos
            if comando == 4:
                #Resolvi deixar isso opcional, pois demora alguns segundos
                print("\nDeseja visualizar todos os", str(len(resultado)), "resultados?")
                if input("Deixe vazio para [Não]\n"):
                    rel = Relogio()
                    #Mostra os veículos encontrados
                    self.mostrarVeiculos(resultado)
                    print("\n")
                    del rel
                    input("Listagem realizada com sucesso.")
                    

    def mostrarVeiculos(self, veiculos):
        'Método que mostra os dados dos veículos'
        if veiculos:
            #Caso seja uma lista de veículos
            if type(veiculos) == type([]):
                for v in veiculos:
                    print(str(v))
            #Caso seja somente um veiculo
            else:
                print(veiculos.mostrar())
        #Caso não receba um veículo
        else:
            print("\nVeículo não encontrado no Banco de Dados.")

            
    def reservar(self, comando):
        'Método que controla as reservas, de acordo com o comando vindo do Menu'
        #Status é o booleano desejado
        #Por padrão é True, para reservar um veículo
        status = True
        estado = "Reservado", "cancelar a reserva", "reservar ", "cancelar a reserva d"
        #Cancelar reserva, que torna Status falso
        if comando == 6:
            status = False
            estado = "Livre", "reservar", "cancelar a reserva d", "reservar "

        print("Para cancelar, pressione Enter\n")            
        placa = input("Digite a placa do veículo\n")
        if placa:
            rel = Relogio()
            #Pega o veículo e seu índice
            veiculo, indice = self.controle.pesquisar("Placa", placa, False, True)
            print("\n")
            del rel
            input("Pesquisa realizada com sucesso.\n")
        #Mostra os dados do veículo
        self.mostrarVeiculos(veiculo)
        #Caso o veículo já esteja no estado desejado, por exemplo, já reservado...
        x = 2
        if veiculo.getReservado() == status:
            print("\nO veículo já está", estado[0],"\nDeseja", estado[1] + "?")
            if not input("Deixe vazio para [Não]\n"):
                  return
            #O Status é trocado e o texto muda
            status = not status
            x += 1
        print("\nDeseja", estado[x] + "o veículo?")
        if not input("Deixe vazio para [Sim]\n"):
            rel = Relogio()
            #Finalmente a reserva do item é alterada para Status e o arquivo é salvo
            self.controle.atualizarReserva(indice, status)
            self.controle.escreverArquivo(self.arquivoAtual)
            del rel
            input("Operação realizada com sucesso.")

    def sair(self, comando=""):
        '...Adeus'
        if input("Deseja salvar o banco de dados?\nVazio para [Não]\n"):
            print("\n"*5)
            self.escreverArquivo()
        return True

#---
app = Interface()
app.run()

        
    
