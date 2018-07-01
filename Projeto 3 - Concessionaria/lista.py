
class No():
    def __init__(self, item, ante = None, prox = None):
        self.prox = prox
        self.ante = ante
        self.item = item

    def __repr__(self):
        return repr(self.item)

from random import randint
class ListaEncadeada():
    'Banco de dados no formato de uma lista duplamente encadeada'
    
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def __iter__(self):
        'Atual é uma referência ao último item da pesquisa mais recente'
        self.atual = No(0, None, self.primeiro)
        return self

    def __next__(self):
        'Simplesmente percorre iterativamente a lista, atribuindo o Atual'
        if self.atual:
            self.atual = self.atual.prox
        if not self.atual:
            return
        return self.atual.item
    

    def buscar(self, item):
        'Percorre a lista em busca de um item, então devolve o nó correspondente'
        no = self.primeiro
        iteracao = iter(self)
        i = next(iteracao)
        while i != None:
            if i == item:
                return self.atual
            i = next(iteracao)
        return None

    def buscarAtributo(self, pesquisa, atributo, multiplo = False, indice = False):
        '''Percorre a lista em busca de um item com um atributo específico
        Pesquisa é o valor procurado e Atributo é o método usado
        O padrão é só o item ser devolvido, mas isso pode ser alterado
        Multiplo faz com que vários itens sejam devolvidos
        Indice faz com que o índice do nó seja devolvido'''
        resultados = []
        indice = 0
        iteracao = iter(self)
        i = next(iteracao)        
        while i != None:
            if atributo(i) == pesquisa:
                if multiplo:
                    resultados.append(i)
                elif indice:
                    return i, indice
                else:
                    return i
            i = next(iteracao)
        return resultados

    #
    def buscarIndice(self, indice):
        'Percorre a lista em busca de um índice usando um módulo, então o devolve'
        #Usados para percorrer o método em ambas direções da busca
        def getProx(no):
            if no.prox == None:
                return self.primeiro
            return no.prox        
        def getAnte(no):
            if no.ante == None:
                return self.ultimo
            return no.ante
        
        no = self.primeiro
        #Método que unifica ambas direções
        proxNo = getProx
        #Valor negativo faz com que a busca vá de trás para frente
        if indice < 0:
            proxNo = getAnte
            indice = indice * (-1)
            no = self.ultimo
            indice -= 1
        #Evita repetições usando um módulo
        indice = indice % self.tamanho
        while indice:
            no = proxNo(no)
            indice -= 1            
        return no


    def inserir(self, item):
        '''Insere um item como último da lista
        Também trata o caso da lista estar vazia'''            
        if self.tamanho == 0:
            self.primeiro = No(item)
            self.ultimo = self.primeiro
        else:
            no = No(item, self.ultimo, None)
            self.ultimo.prox = no
            self.ultimo = no              
        self.tamanho += 1
    
    def inserirPrimeiro(self, item):
        'Insere um item como primeiro da lista'
        if self.tamanho == 0:
            self.inserir(item)
        else:
            no = No(item, None, self.primeiro)
            self.primeiro.ante = no
            self.primeiro = no
            self.tamanho += 1      

    #
    def inserirNo(self, item, ante, prox):
        'Conecta dois nós a um novo nó entre eles'
        no = No(item, ante, prox)
        ante.prox = no
        prox.ante = no
        self.tamanho += 1        

    def inserirOrdenado(self, item, decrescente = False):
        '''Percorre a lista para encontrar a posição correta de inserção de um nó
        Compara tanto de forma crescente quanto decrescente'''
        #Métodos que unificam a ordenação crescente e decrescente
        def cmpCr(item, outro):
            return item < outro
        def cmpDecr(item, outro):
            return item > outro
        if decrescente: cmp = cmpDecr
        else: cmp = cmpCr
        
        no = self.primeiro
        if self.tamanho == 0:
            self.inserir(item)
        #Caso só tenha 1 item na lista
        elif no.prox == None:
            self.inserir(item)
        #Caso venha antes do primeiro item
        elif cmp(item, no.item):
            self.inserirPrimeiro(item)
        #Caso padrão
        else:
            no = no.prox
            while no:
                if cmp(item, no.item):                    
                    self.inserirNo(item, no.ante, no)
                    return
                no = no.prox
            #Caso seja o último item
            self.inserir(item)

    #
    def inserirAleatorio(self, item):
        'Insere um item em uma posição aleatória'
        if self.tamanho == 0:
            self.inserir(item)
        else:
            random = randint(0, self.tamanho)
            self.inserirIndice(item, random - int(random/2))        

    #
    def inserirIndice(self, item, indice):
        'Insere um item no índice indicado, empurrando o nó existente'
        if self.tamanho == 0:
            self.inserir(item)
            return
        no = self.buscarIndice(indice)
        #Tratamento de casos especiais
        if no == self.primeiro:
            self.inserirPrimeiro(item)
        elif no == self.ultimo:
            self.inserir(item)
        else:           
            self.tamanho += 1
            #Caso padrão, empurra o nó para frente
            if indice >= 0:
                no.ante.prox = No(item, no.ante, no)
                no.ante = no.ante.prox
            #Caso o índice seja negativo, empurra o nó para trás
            else:
                no.prox.ante = No(item, no, no.prox)
                no.prox = no.prox.ante
                

    def pop(self):
        '''Remove o último nó, então o devolve
        Trata o caso do item removido ser o único da lista'''
        if self.tamanho == 0:
            return
        #Caso seja o único item da lista
        #Faz com que a lista fique vazia
        elif self.tamanho == 1:
            no = self.primeiro
            self.primeiro = None
            self.ultimo = None
            self.tamanho -= 1
        else:
            no = self.ultimo        
            self.ultimo = no.ante
            self.ultimo.prox = None
            self.tamanho -= 1
        return no

    #
    def popPrimeiro(self):
        'Remove o primeiro nó, então o devolve'
        if self.tamanho == 0:
            return
        elif self.tamanho == 1:
            return self.pop()            
        no = self.primeiro
        no.prox.ante = None
        self.primeiro = no.prox        
        self.tamanho -= 1
        return no

    #
    def popItem(self, item):
        'Busca o nó de um item específico, então o remove com um pop'
        return self.popNo(self.buscar(item))

    #
    def popNo(self, no):
        'Remove o nó conectando o ante e prox dele, então o devolve'
        #Tratamento de casos especiais
        if no == self.primeiro:
            return self.popPrimeiro()           
        elif no == self.ultimo:
            return self.pop()
        elif no:
            no.prox.ante = no.ante
            no.ante.prox = no.prox                
            self.tamanho -= 1         
        return no

    #
    def popIndice(self, indice = -1):
        '''Percorre a lista em busca do nó com o índice inserido, seja ele positivo ou negativo
        Desfaz as referências desse nó encontrado e em seguida o devolve'''
        if self.tamanho == 0:
            return
        elif self.tamanho == 1:
            return self.pop()
        no = self.buscarIndice(indice)
        return self.popNo(no)

    #
    def popAtual(self):
        'Remove o nó da iteração mais recente'
        return self.popNo(self.atual)
        
    #
    def substituirAtual(self, item):
        'Substitui o item do nó da iteração mais recente'
        self.atual.item = item

    #
    def substituirItemIndice(self, item, indice):
        'Busca por um índice e substitui o item do nó'
        iteracao = iter(self)
        i = next(iteracao)
        while indice:
            i = next(iteracao)
            indice -= 1
        self.atual.item = item

    #
    def inverterLista(self):
        'Inverte a direção da lista completa'
        iteracao = iter(self)
        i = next(iteracao)
        while i != None:
            aux = self.atual
            i = next(iteracao)
            aux.ante, aux.prox = aux.prox, aux.ante
        self.primeiro, self.ultimo = self.ultimo, self.primeiro
