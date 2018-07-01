

class Grafo(dict):
    ' '
    def __init__(self, direcional=False, pesado=False):
        self.direcional = direcional
        self.pesado = pesado

    def addAresta(self, aresta):
        ' '        
        vertice1 = self.getVertice(aresta[0])
        vertice2 = self.getVertice(aresta[1])
        if self.pesado:
            vertice1[aresta[1]] = aresta[2]
            if not self.direcional:
                vertice2[aresta[0]] = aresta[2]
        else:
            vertice1.add(aresta[1])
            if not self.direcional:
                vertice2.add(aresta[0])

    def getVertice(self, vertice):
        ' '
        try:
            return self[vertice]
        except KeyError:
            if self.pesado:
                self[vertice] = {}
            else:
                self[vertice] = set()
            return self[vertice]

    def grauVertice(self, vertice):
        ' '
        self.getVertice(vertice)
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
                try:                    
                    if self[v][vertice] != None:
                        entrada += 1
                except KeyError:
                    pass                        
        return saida, entrada

class Controle():
    ' '

    def __init__(self):
        self.grafo = None

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
        self.grafo = Grafo(direcional, pesado)

        #Ignorar comentários do arquivo
        while linha[0] == "%":
            linha = f.readline()
            
        while linha:
            linha = linha.split()
            for i in range(len(linha)):
                linha[i] = int(linha[i])
            if len(linha) and linha[0] != "%":
                self.grafo.addAresta(linha)             
            linha = f.readline()
        f.close()

        

from time import clock
class Relogio:
    'Classe simples usada para cronometrar as operações'    
    def __init__(self):
        self.tempo = clock()
    def __del__(self):
        print("Tempo de Operação:", str(clock() - self.tempo))

        

c = Controle()

rel = Relogio()
c.lerArquivo("PESADAO")
del rel

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

c.lerArquivo("out.linux")
rel = Relogio()
for v in c.grafo:
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
