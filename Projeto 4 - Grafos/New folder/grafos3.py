
class Grafo(list):
    '''O Grafo funciona como uma lista de conjuntos ou dicionários
    O grafo em si é uma lista com |v| índices, que são os seus vértices
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
                self.append(set())

    #Não vi necessidade de colocar privado
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
            u.add(aresta[1])
            if not self.direcional:
                v.add(aresta[0])

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
            self.append(set())
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
            return "Vértice não existe"
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
            return "Vértice não existe"
        v = self[vertice-1]
        saida = len(v)            
        if not self.direcional:
            return saida
        entrada = 0
        for v in self:
            if vertice in v:                    
                entrada += 1        
        return saida, entrada

    def buscarLargura(self, de=1, para=0):
        if not para:
            para = self.getTamanho()            
        visitados = [False]*self.getTamanho()
        visitados[de-1] = True
        visitar = [de]
        caminho = []
        while visitar:
            atual = visitar.pop(0)
            caminho.append(atual)
            for vizinho in self[atual-1]:
                if not visitados[vizinho-1]:                    
                    if vizinho == para:
                        return caminho + [vizinho] 
                    visitar.append(vizinho)
                    visitados[vizinho-1] = True
            input(str(atual) + ":\t" + str(visitar))
        return visitados
            
        

class Controle():
    ' '

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
            
        #Ignorar comentários do arquivo
        while linha[0] == "%":
            linha = f.readline()

        arestas = []
        maior = 0
        while linha:
            linha = linha.split()
            for i in range(len(linha)):
                linha[i] = int(linha[i])
            #Procura o maior vértice, obtendo o tamanho do Grafo
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
                self.grafo.addAresta(arestas.pop())
                
    def gerarGrafo(self, arestas, maior, direcional, pesado):
        'Cria o grafo de acordo com os dados obtidos no LerArquivo'
        self.grafo = Grafo(maior, direcional, pesado)
        for a in arestas:
            self.grafo.addAresta(a)
    
    def adicionarAresta(self, u, v, peso=0):
        if self.grafo.getPesado():
            return self.grafo.addAresta((u, v, peso))
        return self.grafo.addAresta((u, v))

    def imprimirGrafo(self):
        for i in range(self.quantidadeVertices()):
            print(str(i + 1) + ":", self.grafo[i])
            if not (i+1) % 20:
                if input("\nInsira 0 para interromper"):
                    break

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
    def __init__(self):
        self.tempo = clock()
    def __del__(self):
        print("Tempo de Operação:", str(clock() - self.tempo))


c = Controle()

rel = Relogio()
c.lerArquivo("out.dolphins")
del rel



'''
rel = Relogio()
c.lerArquivo("PESADAO")
del rel
input()
c = Controle()

rel = Relogio()
arestas, maior, direcao, peso = c.lerArquivo("PESADAO", True)
del rel
rel = Relogio()
c.gerarGrafo(arestas, maior, direcao, peso)
del rel
'''

'''
rel = Relogio()
c.lerArquivo("out.dolphins")
print(c.grafo.grauVertice(1))
c.lerArquivo("out.ego-facebook")
print(c.grafo.grauVertice(1))
c.lerArquivo("out.linux")
print(c.grafo.grauVertice(1))
c.lerArquivo("out.maayan-faa")
print(c.grafo.grauVertice(1))
c.lerArquivo("out.opsahl-usairport")
print(c.grafo.grauVertice(1))
c.lerArquivo("out.subelj_euroroad_euroroad")
print(c.grafo.grauVertice(1))
c.lerArquivo("out.tntp-ChicagoRegional")
print(c.grafo.grauVertice(1))

del rel
'''


'''
rel = Relogio()
for v in range(len(c.grafo)):
    c.grafo.grauVertice(v)
del rel
'''
                
        

        
'''
    def delAresta(self, aresta):        
        self[aresta[0]].remove(aresta[1])
        if not self.direcional:
            self[aresta[1]].remove(aresta[0])

    def delVertice(self, vertice):        
        try:   
            vizinhos = self[vertice]
            while i in range(len(vizinhos)):
                self.delAresta((v, vertice))
            del self[vertice]
        except KeyError:
            return "Vértice não encontrado"



class Grafo2(dict):
    ' '
  
    def __init__(self, vertices=[], arestas=[], direcional=False):
        self.direcional = direcional
        for v in vertices:
            self[v] = set()
        for a in arestas:
            self.addAresta(a)

    def addAresta(self, aresta):
        ' '
        self[aresta[0]].add(aresta[1])
        if not self.direcional:
            self[aresta[1]].add(aresta[0])

    def addVertice(self, vertice):
        ' '
        self[vertice] = set()

    def delAresta(self, aresta):
        self[aresta[0]].remove(aresta[1])
        if not self.direcional:
            self[aresta[1]].remove(aresta[0])

    def delVertice(self, vertice):
        try:
            vizinhos = self[vertice]
            for v in vizinhos:
                self.delAresta((v, vertice))
            del self[vertice]
        except KeyError:
            return "Vértice não encontrado"

'''
