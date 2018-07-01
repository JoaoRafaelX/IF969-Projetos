###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:	João Rafael Santos Camelo
# Email:	jrsc2@cin.ufpe.br
# Data:	        01/11/2017
#
# Descricao:  A descricao deve fornecer uma explicacao sucinta do algoritmo (problema)
#				que esta sendo implementado neste arquivo.
#
###############################################################################
   
from relogio import *
from controle import *
class Interface:
    'Classe que interage com o usuário'

    def __init__(self):
        self.arquivoAtual = "veiculos.txt"
        self.tipoAtual = "L2E"
        self.ordemAtual = ""
        self.controle = None

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
                  "7. Carregar arquivo / Mudar ordem ou tipo de banco\n"+
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
        '''Método que permite a leitura do arquivo, seja padrão ou escolhido pelo usuário
        Chamado tanto pelo menu, quanto no método inicial da Interface'''
        print("Digite o nome do arquivo de banco de dados desejado")
        print("Caso deseje usar o arquivo padrão ou atual, pressione Enter")        
        #Comando é true quando o método foi chamado pelo menu
        #Quando chamado pelo menu, a operação é cancelada
        #Mas quando é chamada no método inicial, o arquivo padrão é lido, "veiculos.txt"
        arquivo = input()
        self.escolherTipo()
        if self.tipoAtual == "L2E":
            self.escolherOrdem()
        print("\n\n")
        if arquivo:
            self.arquivoAtual = arquivo
        rel = Relogio()
        self.controle = Controle(self.arquivoAtual, self.tipoAtual, self.ordemAtual)
        del rel        
        input("Banco de dados alterado com sucesso.") 

    def escolherTipo(self, comando = ""):
        '''Método que define o tipo do banco de dados
        Pode ser "L2E", para lista duplamente encadeada
        Ou "AB", para árvore binária'''
        print("Pressione Enter para usar uma Lista Duplamente Encadeada")
        print("Ou insira algo para usar uma Árvore Binária")
        if input():
            self.tipoAtual = "AB"
            self.ordemAtual = ""
        else: self.tipoAtual = "L2E"

    def escolherOrdem(self, comando = ""):
        '''Método que define a ordem de inserção do banco de dados
        Pode ser "RAND", "CRES", "DECR", "PRIM" ou padrão'''
        print("Insira um dos números para escolher o tipo da inserção" )
        print("1. Ordenada Crescente\n2. Ordenada Decrescente")
        print("3. Inserção por pilha\n4. Inserção Aleatória")
        print("Pressione Enter para usar a Inserção por Fila")
        switch = {"1": "CRES", "2": "DECR",
                  "3": "PRIM", "4": "RAND"}

        self.ordemAtual = switch.get(input("Escolha: "), "")
            

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
            lista = [tipo[0]]
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
                #Reservado
                lista.append("False")
                print("\n")
                rel = Relogio()
                #Manda os dados do veiculo em uma lista para o Controle interpretar
                self.controle.inserir(self.controle.interpretar(lista))
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
                rel = Relogio()
                #Mostra o veículo encontrado
                self.mostrarVeiculos(self.controle.pesquisar(tipo, dado))
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
            rel = Relogio()
            resultado = self.controle.pesquisar("Categoria", dado, True)
            del rel
            #Comando de contar quantos veículos de algum tipo existem no banco de dados
            if comando == 3:
                print(len(resultado), "veículos encontrados\n")
            
            input("Pesquisa realizada com sucesso.\n")
            
            #Comando de listar veículos
            if comando == 4:                
                tamanho = len(resultado)
                #Resolvi deixar isso opcional, pois demora alguns segundos
                print("\nDeseja visualizar todos os", str(tamanho), "resultados?")
                if not input("Deixe vazio para [Sim]\n"):
                    #Mostra os veículos encontrados
                    indice = 1
                    while indice and tamanho/20 > indice-1:
                        print("\n\n\n\n\n\n")
                        self.mostrarVeiculos(resultado[(indice-1)*20:(indice)*20])
                        print("\nÍndice atual:", str(indice))
                        print("Veículos de " + str((indice-1)*20) + " a " +
                              str(indice*20) +" de", str(tamanho), "veículos")
                        print("Pressione Enter para os próximos 20 itens")
                        print("Digite 0 para encerrar a visualização")
                        indiceEntrada = input("")
                        if not indiceEntrada: indice += 1
                        elif indiceEntrada == "0": break
                        elif indiceEntrada.isdigit(): indice = int(indiceEntrada)
                    

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
            if self.tipoAtual == "AB":
                veiculo = self.controle.pesquisarAB(placa)
            else:
                veiculo = self.controle.pesquisar("Placa", placa)
            print("\n")
            del rel
            input("Pesquisa realizada com sucesso.\n")
        else:
            return
        if not veiculo:
            print("Veículo não encontrado.")
            return
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
            veiculo.setReservado(status)
            rel = Relogio()
            #Finalmente a reserva do item é alterada para Status e o arquivo é salvo
            self.controle.atualizarAtual(veiculo)
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

        
    
