###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:	Joao Rafael Santos Camelo
# Email:	jrsc2@cin.ufpe.br
# Data:		2017-08-16
#
# Descricao:  Conta quantas triplas em um vetor de inteiros somam a zero
#
#
# Licenca: The MIT License (MIT)
#			Copyright(c) 2017 Fulano de Tal
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

def gera_seq_aleatoria(tam):
   return numpy.random.randint(-MAX,MAX, size=tam)


# Voce deve implementar essa funcao
def conta_somas(vetor):
   tam = len(vetor)
   total = 0
   
   for i in range(tam):
      for j in range(i + 1, tam):
         for k in range(j + 1, tam):
            if not vetor[i] + vetor[j] + vetor[k]:
               total += 1 
   return total


def main():
	'''
	Contem os comandos em Python referentes `a implementacao do algoritmo
	seeds = [11,7,13,19,5189,7919]
	'''
	seeds = [11, 7,13,19,5189,7919]
	tam = [50,100,250,500,1000,1500]
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
	print("\n")
