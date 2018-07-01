
class Grafo(list):
    '''O Grafo funciona como uma lista de conjuntos ou dicionários
    O grafo em si é uma lista com |v| elementos, que são os seus vértices
    Cada vértice é uma coleção de outros vértices que o mesmo tem ligação, arestas
    Essa aresta pode ou não ser Direcional e Ponderada, alterando sua funcionalidade'''
    def __init__(self, tamanho=0, direcional=False, pesado=False):
        self.direcional = direcional
        self.pesado = pesado
        #Inicializa a lista de dicionários ou conjuntos
        if pesado:
            for i in range(tamanho):
                self.append({})
        else:
            for i in range(tamanho):
                #Conjuntos são bem úteis pois não aceitam itens duplicados
                self.append([])

    #Não vi necessidade de colocar como privado
    def getPesado(self):
        return self.pesado
    def getDirecional(self):
        return self.direcional
    def getTamanho(self):
        return len(self)
    
    def addAresta(self, aresta):
        'Adiciona uma aresta à lista'
        if (aresta[0] > self.getTamanho() or
            aresta[1] > self.getTamanho()):
            return -1
        u = self[aresta[0]-1]
        v = self[aresta[1]-1]
        if self.pesado:
            u[aresta[1]] = aresta[2]
            if not self.direcional:
                v[aresta[0]] = aresta[2]
        else:
            u.append(aresta[1])
            if not self.direcional and aresta[0] != aresta[1]:
                v.append(aresta[0])

    def alterarTamanho(self, n):
        '''Aumenta ou diminui o tamanho do Grafo
        Caso esteja diminuindo, remove as arestas que apontam aos vértices removidos'''
        tamanho = self.getTamanho()
        if n > tamanho:            
            for i in range(n - tamanho):
                self.addVertice()
        elif n < tamanho:
            for i in range(tamanho, n, -1):
                self.removerArestas(i)
                self.pop()
                
    def addVertice(self):
        'Adiciona um vértice vazio ao grafo, devolvendo seu número'
        if self.pesado:
            self.append({})
        else:
            self.append([])
        return self.getTamanho()

    def removerArestas(self, vertice):
        'Apaga todas arestas relacionadas a um vértice'
        if vertice > self.getTamanho():
            return "Vértice não existe"
        if not self.direcional:
            for i in range(self[vertice]):
                if self.pesado:
                    del self[i][vertice]
                else:
                    self[i].remove(vertice)
        else:
            for i in range(self.getTamanho()):
                if vertice in self[i]:
                    if self.pesado:
                        del self[i][vertice]
                    else:
                        self[i].remove(vertice)
                        
    def getArestas(self):
        '''Percorre todo o grafo contando a quantidade de adjacentes de cada vértice,
        caso o vértice seja não direcional, devolve metade do resultado encontrado'''
        total = 0
        for vertice in range(len(self)):
            total += len(self[vertice])
        if not self.direcional:
            return int(total/2)
        else:
            return total
        
    def getAdjacentes(self, vertice):
        'Devolve uma lista dos vértices vizinhos ao vértice desejado'
        if vertice > self.getTamanho():
            return -1
        if self.pesado:
            return [chave for chave in self[vertice-1]]
        return list(self[vertice-1])
    
    def getGrau(self, vertice):
        '''Caso seja um grafo não direcional,
        devolve o tamanho da lista dos adjacentes do vértice
        Caso o grafo seja direcional,
        percorre todo o grafo em busca de arestas com aquele vértice
        Então devolve o grau de saída e de entrada do vértice'''
        if vertice > self.getTamanho():
            return -1
        v = self[vertice-1]
        saida = len(v)            
        if not self.direcional:
            return saida
        entrada = 0
        for v in self:
            if vertice in v:                    
                entrada += 1        
        return saida, entrada

    def buscarLarguraCaminho(self, u=1, v=-1):
        '''Faz uma busca em largura começando do U em busca do V
        Caso o V seja 0, a busca checará todos os caminhos possíveis saindo de U
        Caso ela seja V seja -1, buscará pelo último vértice do Grafo
        Devolve uma lista dos vértices que percorreu'''
        if v == -1:
            v = self.getTamanho()
        visitados = [u]
        i = 0
        while i < len(visitados):
            atual = visitados[i]
            for vizinho in self[atual-1]:
                if not vizinho in visitados:
                    if vizinho == v:
                        return visitados[:i+1] + [vizinho]
                    visitados.append(vizinho)      
            i += 1
        return visitados

    def buscarLarguraAntecessores(self):
        '''Faz uma busca em largura começando do 1
        Percorre todo o vértice, independente de estar desconectado ou não
        Enquanto isso, marca os antecessores dos vértices em uma lista
        Por fim, devolve essa lista'''
        tamanho = self.getTamanho()
        antecessores = [-1]*tamanho
        antecessores[0] = 0
        visitar = [1]
        for t in range(tamanho):
            if antecessores[t] == -1:
                while visitar:
                    atual = visitar.pop(0)
                    for vizinho in self[atual-1]:
                        if antecessores[vizinho-1] == -1:
                            antecessores[vizinho-1] = atual
                            visitar.append(vizinho)
        return antecessores
    
                              
        
from random import randint
class Controle():
    '''Classe com os métodos do grafo, supostamente a ligação entre Interface e Modelo(Grafo)    
    Na sua inicialização, caso seja passado algum nome de arquivo, ele será lido
    Como não há uma classe interface, alguns prints foram usados'''

    def __init__(self, arquivo=""):
        self.grafo = None
        if arquivo:
            self.lerArquivo(arquivo)

    def lerArquivo(self, arquivo, teste=False):
        '''Lê linha por linha do arquivo, adicionando as arestas numa lista
        Checa qual é o maior vértice citado no arquivo para ser o tamanho do grafo
        Então, caso teste, retorna esses valores separados, se não, gera o grafo'''
        
        f = open(arquivo, "r")        
        linha = f.readline()
        linha = linha.split()
        
        direcional = False
        pesado = True
        if "asym" in linha:
            direcional = True
        if "unweighted" in linha:
            pesado = False

        tamanhoLido = False
        maior = 0
        arestas = []
        linha = f.readline()
        #Alguns arquivos tem um segundo comentário com o tamanho do grafo
        if linha[0] == "%":
            linha = linha.split()
            tamanhoLido = True
            maior = int(linha[2])
            linha = f.readline()
            
        while linha:
            linha = linha.split()
            for i in range(len(linha)):
                linha[i] = int(linha[i])
            #Procura o maior vértice, obtendo o tamanho do Grafo
            if not tamanhoLido:
                if linha[0] > linha[1]:
                    n = linha[0]
                else:
                    n = linha[1]
                if n > maior:
                    maior = n
            arestas.append(linha)                
            linha = f.readline()            
        f.close()
        if teste:
            return arestas, maior, direcional, pesado
        else:
            self.grafo = Grafo(maior, direcional, pesado)                
            while arestas:
                self.grafo.addAresta(arestas.pop(0))
                
    def gerarGrafo(self, arestas, maior, direcional, pesado):
        'Cria o grafo de acordo com os dados obtidos no LerArquivo'
        self.grafo = Grafo(maior, direcional, pesado)
        for a in arestas:
            self.grafo.addAresta(a)
    
    def adicionarAresta(self, u, v, peso=0):
        'Adiciona uma aresta no grafo'
        if self.grafo.getPesado():
            return self.grafo.addAresta((u, v, peso))
        return self.grafo.addAresta((u, v))

    def imprimirGrafo(self):
        'Imprime os vértices e seus vizinhos na tela, de 20 em 20'
        tamanho = self.quantidadeVertices()
        indice = 1
        for i in range(self.quantidadeVertices()):
            print(str(i + 1) + " -> ", self.grafo[i])
            if not (i+1) % 20:
                print("\nÍndice atual:", str(indice))
                print("Vértices de " + str((indice-1)*20) + " a " +
                      str(indice*20) +" de", str(tamanho), "vértices")
                print("Pressione Enter para os próximos 20 itens")
                print("Digite 0 para encerrar a visualização")                
                indiceEntrada = input("")
                if not indiceEntrada:
                    indice += 1
                elif indiceEntrada == "0":
                    break
                elif indiceEntrada.isdigit():
                    indice = int(indiceEntrada)        

    def buscarLargura(self, u=1, v=-1):
        '''Descobre um caminho do U ao V por meio de uma busca em largura
        Caso o V seja 0, não buscará por nada, fazendo o maior caminho possível partindo do U
        Caso o V seja -1, buscará pelo último vértice do grafo'''
        if u == 0:
            return self.grafo.buscarLarguraAntecessores()
        return self.grafo.buscarLarguraCaminho(u, v)

    def buscarLarguraAteEncontrar(self, vertice):
        '''Faz uma busca por vértice começando de 1...
        Caso não encontre, busca de novo começando por 2 e assim por diante'''
        for i in range(self.quantidadeVertices()):
            resultado = self.buscarLarguraCaminho(i, vertice)
            if resultado[-1] == vertice:
                return resultado    

    def gerarAleatorio(self, quantidade):
        quantidade *= 2
        numeros = []
        tamanho = self.quantidadeVertices()
        while quantidade:
            numeros.append(randint(1, tamanho))
            quantidade -= 1
        return numeros
        
        
    def pesado(self):
        return self.grafo.getPesado()
    def direcional(self):
        return self.grafo.getDirecional()
    def aumentarGrafo(self, n):
        return self.grafo.alterarTamanho(self.quantidadeVertices + n)
    def diminuirGrafo(self, n):
        return self.grafo.alterarTamanho(self.quantidadeVertices + n)
    def redimensionarGrafo(self, n):
        return self.grafo.alterarTamanho(n)
    def adicionarVertice(self):
        return self.grafo.addVertice()
    def existeAresta(self, u, v):
        return self.grafo.checarAresta(u, v)
    def quantidadeVertices(self):
        return self.grafo.getTamanho()
    def quantidadeArestas(self):
        return self.grafo.getArestas()
    def vizinhosVertice(self, vertice):
        return self.grafo.getAdjacentes(vertice)
    def grauVertice(self, vertice):
        return self.grafo.getGrau(vertice)
            

from time import clock
class Relogio:
    'Classe simples usada para cronometrar as operações'    
    def __init__(self, texto="Operação", tempode=True):
        self.tempo = clock()
        self.texto = texto
        self.tempode = tempode
        
    def __del__(self):
        result = clock() - self.tempo        
        td = "Tempo de "
        if not self.tempode:
            td = ""
            self.texto = self.texto[0].upper() + self.texto[1:]
        print(td + self.texto + ":\n" + str(result), "segundos")
        
    def valor(self):
        result = clock() - self.tempo
        return result


c = Controle()


'''
c.lerArquivo("out.dolphins")
rel = Relogio("Percorrer")
print(c.grafo.buscarLarguraAntecessores())
del rel
rel = Relogio("Buscar 0")
print(c.grafo.buscarLarguraCaminho(1,0))
del rel
'''
mostrar = True

lista = ["out.dolphins", "out.ego-facebook",
         "out.linux", "out.maayan-faa", "out.opsahl-usairport",
         "out.subelj_euroroad_euroroad", "out.tntp-ChicagoRegional"]
for i in lista:
    print("\n------------------------------\n")
    rel = Relogio("leitura do arquivo " + i, False)    
    arestas, maior, direcional, pesado = c.lerArquivo(i, True)
    del rel
    rel = Relogio("criação do grafo [" + str(maior) + "V / " + str(len(arestas)) + "A]", False)
    c.gerarGrafo(arestas, maior, direcional, pesado)
    del rel
    del arestas

    print()
    rel = Relogio("busca do primeiro vértice para o último")
    c.buscarLargura()    
    del rel
    rel = Relogio("percorrer todo o grafo")
    antecessores = c.buscarLargura(0)
    del rel

    aleatorios = c.gerarAleatorio(1000)
    rel = Relogio("500 buscas de caminhos aleatórios", False)
    while aleatorios:
        c.buscarLargura(aleatorios.pop(0), aleatorios.pop())
    tempo = rel.valor()
    del rel
    print("Tempo médio: " + str(tempo/maior) + "segundos")

    if mostrar:
        print("Vetor de Antecessores:\n")
        print(antecessores)




