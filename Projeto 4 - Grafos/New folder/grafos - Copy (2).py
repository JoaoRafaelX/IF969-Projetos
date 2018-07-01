
class Grafo(list):
    ' '
    def __init__(self, tamanho=0, direcional=False, pesado=False):
        self.direcional = direcional
        self.pesado = pesado
        for i in range(tamanho):
            if pesado:
                self.append({})
            else:
                self.append(set())
                
    def getPesado(self):
        return self.pesado
    def getDirecional(self):
        return self.direcional
    def getTamanho(self):
        return len(self)

    def addAresta(self, aresta):
        ' '
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

    
    def getArestas(self):
        total = 0
        for i in range(len(self)):
            total += len(self[i])
        if not self.direcional:
            return total/2
        return total
        
    def grauVertice(self, vertice):
        ' '
        saida = len(self[vertice])
        if not self.direcional:
            return saida, saida

        entrada = 0
        if not self.pesado:            
            for v in self:
                if vertice in self[v]:
                    entrada += 1
        else:
            for v in self:              
                if vertice in self[v]:
                    entrada += 1            
        return saida, entrada

class Controle():
    ' '

    def __init__(self, arquivo=""):
        self.grafo = None
        if arquivo:
            self.criarGrafo(arquivo)

    def lerArquivo(self, arquivo):
        f = open(arquivo, "r")
        
        linha = f.readline()
        linha = linha.split()
        if not linha:
            return
        
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
            if len(linha) and linha[0] != "%":
                arestas.append(linha)
                if linha[0] > linha[1]:
                    n = linha[0]
                else:
                    n = linha[1]
                if n > maior:
                    maior = n
            linha = f.readline()        
        f.close()

        return arestas, maior, direcional, pesado

    def gerarGrafo(self, arestas, maior, direcional, pesado):
        self.grafo = Grafo(maior, direcional, pesado)
        for a in arestas:
            self.grafo.addAresta(a)

    def criarGrafo(self, arquivo):        
        arestas, maior, dire, peso = self.lerArquivo(arquivo)
        self.gerarGrafo(arestas, maior, dire, peso)
        
            



        

from time import clock
class Relogio:
    'Classe simples usada para cronometrar as operações'    
    def __init__(self):
        self.tempo = clock()
    def __del__(self):
        print("Tempo de Operação:", str(clock() - self.tempo))

        

c = Controle()
rel = Relogio()
c.criarGrafo("a.txt")
'''
c.criarGrafo("out.dolphins")
print(c.grafo.grauVertice(1))
c.criarGrafo("out.ego-facebook")
print(c.grafo.grauVertice(1))
c.criarGrafo("out.linux")
print(c.grafo.grauVertice(1))
c.criarGrafo("out.maayan-faa")
print(c.grafo.grauVertice(1))
c.criarGrafo("out.opsahl-usairport")
print(c.grafo.grauVertice(1))
c.criarGrafo("out.subelj_euroroad_euroroad")
print(c.grafo.grauVertice(1))
c.criarGrafo("out.tntp-ChicagoRegional")
print(c.grafo.grauVertice(1))
'''
del rel

rel = Relogio()
c.lerArquivo("out.linux")
del rel
rel = Relogio()
for v in c.grafo:
    c.grafo.grauVertice(v)
del rel

                
        

        
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
