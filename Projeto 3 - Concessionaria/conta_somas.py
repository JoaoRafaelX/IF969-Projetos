###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:	João Rafael Santos Camelo
# Email:	jrsc2@cin.ufpe.br
# Data:		01/10/17
#
###############################################################################

import sys
from time import perf_counter
import numpy

MAX = 999999

class Cronometro:
   ''' Cronometra tempo gasto desde a criacao ate a chamada do metodo
       tempo_gasto
   '''    
   def __init__(self):
      self.__criacao = perf_counter()
   def tempo_gasto(self):
      return perf_counter() - self.__criacao


###
def mergesort(lista):
    '''Ordena uma lista, dividindo-a várias vezes pela metade recursivamente
    Complexidade de Tempo sempre O(n log n) e Complexidade de Espaço O(n)'''
    #Caso seja só 1 item, não tem o que ordenar
    if len(lista) > 1:        
        meio = len(lista)//2
        #Separa as listas recursivamente
        esquerda = mergesort(lista[:meio])
        direita = mergesort(lista[meio:])
        #Esquerda, Direita, Guardar
        #Servem como índices dos movimentos das listas
        e = d = g = 0
        while e < len(esquerda) and d < len(direita):
            if esquerda[e] < direita[d]:
                lista[g] = esquerda[e]
                e += 1
            else:
                lista[g] = direita[d]
                d += 1
            g += 1
        lista, g = mergeaux(lista, esquerda, e, g)
        lista, g = mergeaux(lista, direita, d, g)        
    return lista

###
def mergeaux(lista, metade, i, g):
    'Método auxiliar simples para evitar repetição'
    while i < len(metade):
        lista[g] = metade[i]
        i += 1
        g += 1
    return lista, g



def gera_seq_aleatoria(tam):
   return numpy.random.randint(-MAX,MAX, size=tam)


###
def conta_somas(vetor):
    tam = len(vetor)
    total = 0

    for i in range(tam):
        for j in range(i+1, tam):
            if buscaBinaria(-vetor[i]-vetor[j], vetor) > j:
                total += 1
    return total


###
def buscaBinaria(ij, vetor):
    '''Faz uma busca binária, retorna a Posição ou -1 caso não encontre'''
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        p = (inicio + fim) // 2
        if vetor[p] > ij:
            fim = p - 1
        elif vetor[p] < ij:
            inicio = p + 1
        else:
            return p
    return -1


def main():
	'''
	Contem os comandos em Python referentes `a implementacao do algoritmo
	'''
	seeds = [11, 7, 13, 19, 5189, 7919]
	tam = [50, 100, 250, 500, 1000, 1500]
	for i,seed in enumerate(seeds):
	   numpy.random.seed(seed)
	   vetor = gera_seq_aleatoria(tam[i])
	   cron = Cronometro()
	   total = conta_somas(vetor)
	   print("Tempo gasto com {0} elementos foi {1} segundos".format(tam[i],cron.tempo_gasto()))
	   del vetor
	   del cron


if __name__ == '__main__':
	main()
