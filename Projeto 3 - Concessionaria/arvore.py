
class No():
    def __init__(self, item, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
        self.item = item

    def __repr__(self):
        return repr(self.item)
    

class ArvoreBinaria():
    'Banco de dados no formato de uma árvore binária'
    def __init__(self):
        self.raiz = None

    def __iter__(self):
        '''Atual é o último resultado da busca iterativa
        Próximo é o próximo nó que será lido na busca
        E a Pilha é uma lista com todos os nós da árvore'''
        self.atual = None
        self.proximo = self.raiz
        self.pilha = []
        return self

    def __next__(self):
        '''Percorre iterativamente a árvore binária
        Segue primeiro pela esquerda de cada nó, então pela direita
        Vai adicionando todos os nós encontrados na Pilha
        E retorna o item do nó Atual'''
        while self.proximo:
            self.pilha.append(self.proximo)
            self.proximo = self.proximo.esquerda
        if not self.pilha:
            self.atual = None
            return 
        self.proximo = self.pilha.pop()
        self.atual = self.proximo
        self.proximo = self.proximo.direita
        return self.atual.item
    
    def filhos(self, no):
        'Retorna a quantidade de filhos de um nó'
        quantidade = 0
        if no.esquerda:
            quantidade += 1
        if no.direita:
            quantidade += 1
        return quantidade

    def buscar(self, item, atual = False):
        'Percorre a lista em busca de um item, o devolvendo caso encontrado'
        no = self.raiz
        while no != None:
            if item < no.item:
                no = no.esquerda
            elif item > no.item:
                no = no.direita
            else:
                if atual: self.atual = no
                return no.item
        #Será None caso o item não esteja na árvore
        return
    
    #
    def buscarAtual(self, item):
        return buscar(item, True)
    
    def buscarAtributo(self, pesquisa, atributo, multiplo = False):
        '''Percorre a lista iterativamente, de forma crescente pela Placa
        Atributo é um método a ser usado no item e Pesquisa é o resultado procurado
        Caso Múltiplo seja True, retorna uma lista com todos resultados'''
        resultados = []
        iteracao = iter(self)
        i = next(iteracao)
        while i != None:
            if atributo(i) == pesquisa:
                if multiplo:
                    resultados.append(i)
                else:
                    return i
            i = next(iteracao)
        return resultados

    #
    def buscarNo(self, item, paternidade = False):
        '''Percorre a lista em busca de um item, devolve o nó
        Paternidade devolve o nó e seu pai'''
        no = self.raiz
        pai = None
        while no:
            if item < no.item:
                if no.esquerda:
                    pai = no
                    no = no.esquerda
                else: break
            elif item > no.item:
                if no.direita:
                    pai = no
                    no = no.direita
                else: break
            else: break
        if paternidade:
            return no, pai
        return no


    def inserir(self, item):
        'Insere um item na árvore, caso ele já exista, substitui'
        no = No(item, None, None)
        if self.raiz == None:
            self.raiz = no
            return
        
        pai = self.buscarNo(item)
        if item > pai.item:
            pai.direita = no
        elif item < pai.item:
            pai.esquerda = no
        else:
            #Substitui o antigo caso seja igual
            pai = No(item, pai.esquerda, pai.direita)
        
    #
    def substituirAtual(self, item):
        'Usa o Atual salvo de alguma pesquisa iterativa anterior'
        self.atual.item = item

    #
    def popItem(self, item):
        '''Junto do buscarHerdeiro, busca e faz a remoção de um nó
        Para isso, busca o herdeiro mais adequado e faz a substituição
        Caso não tenha herdeiros, o nó é simplesmente deletado'''
        #Bem confuso, mas é o que tem pra hoje
        if not self.raiz:
            return        
        no, pai = self.buscarNo(item, True)
        morto = no.item        
        filhos = self.filhos(no)
        if filhos == 2:
            paiHerdeiro, herdeiro = self.buscarHerdeiro(None, no.direita)        
            if paiHerdeiro:
                paiHerdeiro.esquerda = herdeiro.direita
            if herdeiro:
                herdeiro.esquerda = no.esquerda
                herdeiro.direita = no.direita
            else:
                herdeiro = None
        elif filhos == 1:
            if no.esquerda:
                herdeiro = no.esquerda
            if no.direita:
                herdeiro = no.direita
        else:
            herdeiro = None
        
        if pai == None:
            if herdeiro == None:
                self.raiz = None
                return morto
            self.raiz = herdeiro            
            return morto

        if pai.esquerda == no:
            pai.esquerda = herdeiro
        elif pai.direita == no:
            pai.direita = herdeiro
            
        return morto
    
    #
    def buscarHerdeiro(self, avo, pai):
        '''Método auxiliar da remoção
        Busca o filho mais da esquerda de um pai para se tornar o avô'''
        if pai == None:
            return avo, pai
        filhos = self.filhos(pai)
        if filhos == 1:
            if pai.direita:
                return avo, pai
            if pai.esquerda:
                return pai, pai.esquerda
        elif filhos == 2:
            return self.buscarHerdeiro(pai, pai.esquerda)
        else:
            return avo, pai       
        
    #
    def lerArvore(self, no = "raiz"):
        'Faz uma representação da árvore'
        if no == "raiz":
            no = self.raiz
            print("A Raiz é", no)
        if no:
            if no.esquerda:
                print("Na esquerda do", no, "está o", no.esquerda)
                self.percorrer(no.esquerda)
            if no.direita:
                print("Na direita  do", no, "está o", no.direita)
                self.percorrer(no.direita)     

            
