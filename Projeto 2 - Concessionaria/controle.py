from veiculos import *

class Controle:
    'Classe que faz o processamento e se comunica com o banco de dados'

    def __init__(self, arquivo):
        #Arquivo é o caminho para o banco de dados
        #Única chance de ser False é quando a Interface é inicializada
        self.arquivo = arquivo
        if arquivo:
            self.veiculos = self.lerArquivo()
            
    def lerArquivo(self):
        '''Método que percorre todo o arquivo e, utilizando-se de
        outros métodos auxiliares, interpreta cada linha e
        insere o objeto final em uma lista de Veículos '''
        f = open(self.arquivo, "a+", newline='')
        f.seek(0)
        #Gera o cabeçalho caso arquivo esteja vazio
        cabecalho = f.readline()
        if not cabecalho:
            f.seek(0)
            f.write("tipo\tfabricante\tmodelo\tportas/capacidade\t" +
                    "autonomia\tano\tplaca\trenavam\tchassi\treservado\n")
        #Percorre o arquivo linha por linha
        veiculos = Veiculos()
        linha = f.readline()
        while linha:
            linha = linha.split("\t")
            if len(linha) >= 9:
                #Insere no banco de dados os objetos gerados pelo Interpretar
                veiculos.inserir(self.interpretar(linha))                
            linha = f.readline()
        f.close()
        #Devolve uma classe Veículos preenchida para evitar duplicamento
        return veiculos
    
    def interpretar(self, palavras):
        'Método que faz a diferenciação entre os tipos de veículo'
        if palavras[0] == "carro":
            tipo = Carro
        elif palavras[0] == "van":
            tipo = Van
        elif palavras[0] == "ute":
            tipo = Utilitario
        else:
            return None

        #Tipo aqui serve como um cast, gerando o objeto desejado
        return tipo(palavras[1], palavras[2], palavras[3], 
                    palavras[4], palavras[5], palavras[6], 
                    palavras[7], palavras[8], bool(palavras[9].strip("False\nr")))
        
    def inserir(self, tipo, dados):
        'Com os dados obtidos tanto da interface quanto da leitura, insere em Veículos'
        #Insere o tipo de veículo e o False para Reservado para o Interpretar
        dados.insert(0, tipo)
        dados.append("False")

        #Então o veículo é gerado e inserido no banco de dados
        veiculo = self.interpretar(dados)
        self.veiculos.inserir(veiculo)

    def escreverArquivo(self, caminho):
        'O método escreve linha por linha no arquivo escolhido'
        #O atributo de newline faz com que a quebra de linha funcione como a do linux
        f = open(caminho, "w", newline='')
        f.write("tipo\tfabricante\tmodelo\tportas/capacidade\t" +
                    "autonomia\tano\tplaca\trenavam\tchassi\treservado\n")        
        for i in range(self.veiculos.getTamanho()):
            #Utiliza a função repr customizada dos veículos
            f.write(repr(self.veiculos.getItem(i)) + "\n")
        f.close()


    def pesquisar(self, escolha, pesquisa, varios=False, reservados=False):
        '''Método que controla o método enviado para a pesquisa em Veículos
        Ex: Caso a pesquisa seja por Chassi, o método usado será getChassi'''
        def true(ignorar = ""):
            'Método simples para a pesquisa em Veículos sempre resultar True'
            return "*"

        tipo = true
        if escolha == "Placa":
            tipo = Veiculo.getPlaca
        elif escolha == "RENAVAM":
            tipo = Veiculo.getRENAVAM
        elif escolha == "Chassi":
            tipo = Veiculo.getChassi
        elif escolha == "Categoria":
            #Caso a pesquisa seja para todas as categorias
            #O método utilizado é o True, que fará com que o tipo seja ignorado
            if pesquisa == "*":
                tipo = true
            else:
                #getTipo devolverá o nome da classe, permitindo a comparação
                tipo = Veiculo.getTipo

        #A pesquisa é então realizada com os dados escolhidos    
        resultado = self.veiculos.buscar(tipo, pesquisa, varios, reservados)
        return resultado

    def atualizarReserva(self, indice, reserva):
        self.veiculos.atualizarReserva(indice, reserva)


        


