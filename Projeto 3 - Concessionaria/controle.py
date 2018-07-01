from lista import *
from arvore import *

from carro import *
from utilitario import *
from van import *

from relogioTestes import *
from random import sample
class Controle:
    'Classe que faz o processamento e se comunica com o banco de dados'

    def __init__(self, arquivo, tipo, ordem, testar = False):
        '''Gera o banco de dados e inicia a leitura do arquivo
        Arquivo = Caminho para o arquivo desejado
        Tipo = "L2E" ou "AB"
        Ordem = "RAND", "CRES", "DECR", "PRIM" ou *'''
        self.arquivo = arquivo
        self.tipo = tipo
        self.ordem = ordem
        self.veiculos = None
        if tipo == "PYTHON":
            self.lista = self.lerListaPython()
        if not testar: self.lerArquivo(ordem)
        

    def lerArquivo(self, ordem):        
        '''Método que percorre todo o arquivo e, utilizando-se
        de outros métodos auxiliares, interpreta cada linha dele
        e insere o objeto final em uma lista de Veículos'''
        f = open(self.arquivo, "a+", newline='')        
        f.seek(0)
        
        #Gera o cabeçalho caso arquivo esteja vazio
        cabecalho = f.readline()
        if not cabecalho:
            f.seek(0)
            f.write("tipo\tfabricante\tmodelo\tportas/capacidade\t" +
                    "autonomia\tano\tplaca\trenavam\tchassi\treservado\n")
            
        if self.tipo == "L2E":
            self.veiculos = ListaEncadeada()
        elif self.tipo == "AB":
            self.veiculos = ArvoreBinaria()
        else:
            return None
        
        #Percorre o arquivo linha por linha
        linha = f.readline()
        while linha:
            linha = linha.split("\t")
            if len(linha) >= 9:
                #Insere no banco de dados o objeto criado pelo interpretar
                self.inserir(self.interpretar(linha))             
            linha = f.readline()
        f.close()
        
    
    def interpretar(self, palavras):
        'Método que faz a diferenciação entre os tipos de veículo'
        #Os tipos são objetos
        if palavras[0] == "carro": tipoVeiculo = Carro
        elif palavras[0] == "van": tipoVeiculo = Van
        elif palavras[0] == "ute": tipoVeiculo = Utilitario
        else: return None

        #Tipo aqui serve como um cast, gerando o objeto desejado
        return tipoVeiculo(palavras[1], palavras[2], palavras[3], 
                    palavras[4], palavras[5], palavras[6], 
                    palavras[7], palavras[8], bool(palavras[9].strip("False\nr")))
    
        
    def inserir(self, veiculo):
        '''Executa a inserção do veículo na ordem desejada
        Aleatório, Crescente, Decrescente, Primeiro e Último'''
        if self.ordem == "RAND":
            self.veiculos.inserirAleatorio(veiculo)
        elif self.ordem == "CRES":
            self.veiculos.inserirOrdenado(veiculo)
        elif self.ordem == "DECR":
            self.veiculos.inserirOrdenado(veiculo, True)
        elif self.ordem == "PRIM":
            self.veiculos.inserirPrimeiro(veiculo)
        else:
            self.veiculos.inserir(veiculo)
        

    def escreverArquivo(self, caminho):
        'O método escreve linha por linha no arquivo escolhido'
        #O atributo de newline faz com que a quebra de linha funcione como a do linux
        f = open(caminho, "w", newline='')
        f.write("tipo\tfabricante\tmodelo\tportas/capacidade\t" +
                    "autonomia\tano\tplaca\trenavam\tchassi\treservado\n")

        iteracao = iter(self.veiculos)
        item = next(iteracao)
        while item != None:
            #Utiliza a função repr customizada dos veículos
            f.write(repr(item) + "\n")
            item = next(iteracao) 
        f.close()


    def pesquisar(self, escolha, pesquisa, multiplo = False):
        '''Método que controla o método enviado para a pesquisa em Veículos
        Ex: Caso a pesquisa seja por Chassi, o método usado será getChassi'''
        def todos(ignorar = ""): return "*"

        if escolha == "Placa":
            atributo = Veiculo.getPlaca
        elif escolha == "RENAVAM":
            atributo = Veiculo.getRENAVAM
        elif escolha == "Chassi":
            atributo = Veiculo.getChassi
        elif escolha == "Categoria":
            #Caso seja qualquer tipo de veículo
            if pesquisa == "*":
                atributo = todos
            else:
                atributo = Veiculo.getTipo            
        #Caso não tenha um critério, todos os veículos serão mostrados
        else: atributo = todos
        
        #A pesquisa é então realizada com os dados escolhidos    
        if escolha == "Placa" and self.tipo == "AB":
            resultado = self.veiculos.buscar(pesquisa)
        else:
            resultado = self.veiculos.buscarAtributo(pesquisa, atributo, multiplo)
        return resultado

    def pesquisarAB(self, placa):
        return self.veiculos.buscar(placa, True)

    def pesquisarPlaca(self, placa):
        if self.tipo == "AB":
            return self.veiculos.buscar(placa)
        return self.veiculos.buscarAtributo(placa, Veiculo.getPlaca)


    def atualizarReserva(self, placa, reserva):
        '''Busca um veículo pela placa, recebendo-o e mudando sua reserva
        Então substitui o item do nó encontrado'''
        veiculo = self.buscar(placa)
        #Caso não encontre o veículo
        if not veiculo:
            return
        veiculo.setReservado(reserva)
        self.veiculos.substituirAtual(veiculo)
        return veiculo

    def atualizarAtual(self, veiculo):
        'Substitui o último item pesquisado'
        self.veiculos.substituirAtual(veiculo)
        

    def remover(self, placa):
        'Busca um veículo pela placa, então o remove'
        if self.tipo == "AB":
            return self.veiculos(popItem(placa))
        if self.pesquisarPlaca(placa):
            return self.veiculos.popAtual()
        return

    #
    def inverterLista(self):
        'Inverte todos nós da lista'
        self.veiculos.inverterLista()        

    def mostrarTodos(self):
        'Mostra todos os itens da lista'
        iteracao = iter(self.veiculos)
        i = next(iteracao)
        if i == None: print("Banco de dados vazio")
        while i:
            print(i)
            i = next(iteracao)


###################################################################


    def lerListaPython(self):
        f = open(self.arquivo, "a+", newline='')
        f.seek(0)
        cabecalho = f.readline()
        if not cabecalho:
            f.seek(0)
            f.write("tipo\tfabricante\tmodelo\tportas/capacidade\t" +
                    "autonomia\tano\tplaca\trenavam\tchassi\treservado\n")
        lista = []
        linha = f.readline()
        while linha:
            linha = linha.split("\t")
            if len(linha) >= 9:
                lista.append(self.interpretar(linha))                
            linha = f.readline()
        f.close()
        return lista
        


    def getSample(self):
        f = open(self.arquivo, "a+", newline='')        
        f.seek(0)

        placas = []
        
        #Percorre o arquivo linha por linha
        linha = f.readline()
        while linha:
            linha = linha.split("\t")
            if len(linha) >= 9:
                #Insere no banco de dados o objeto criado pelo interpretar
                placas.append(linha[6])             
            linha = f.readline()
        f.close()
        return sample(placas, 500)
        


    def testarLeitura(self, pontos):
        f = open(self.arquivo, "a+", newline='')        
        f.seek(0)        
        #Gera o cabeçalho caso arquivo esteja vazio
        cabecalho = f.readline()
        if not cabecalho:
            f.seek(0)
            f.write("tipo\tfabricante\tmodelo\tportas/capacidade\t" +
                    "autonomia\tano\tplaca\trenavam\tchassi\treservado\n")            
        if self.tipo == "L2E":
            self.veiculos = ListaEncadeada()
        elif self.tipo == "AB":
            self.veiculos = ArvoreBinaria()
        else:
            return None
        
        #Percorre o arquivo linha por linha
        linha = f.readline()
        i = 1
        rel = Relogio()
        tempos = []
        while linha:
            linha = linha.split("\t")
            if len(linha) >= 9:
                
                #Insere no banco de dados o objeto criado pelo interpretar
                self.inserir(self.interpretar(linha))                
                if i in pontos:
                    tempos.append(rel.getTempo())
                i += 1
            linha = f.readline()
        tempos.append(rel.getTempo())
        f.close()
        return tempos

    
        
    
        


        


