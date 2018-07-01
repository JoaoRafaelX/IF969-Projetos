from controle import *
from quicksort import *
from relogio import *

print("Testes do Quick Sort com 500 elementos")

c = Controle("veiculos.txt", "PYTHON", "")
desordenada = c.lista[0:500]
c = Controle("veiculosCrescente.txt", "PYTHON", "")
crescente = c.lista[0:500]
c = Controle("veiculosDecrescente.txt", "PYTHON", "")
decrescente = c.lista[0:500]


print("\n\n\nQUICKSORT DIVIDIR E CONQUISTAR")

print("\nQuickSort na lista desordenada")
rel = Relogio()
quickListas(desordenada)
del rel

print("\nQuickSort na lista crescente")
rel = Relogio()
quickListas(crescente)
del rel

print("\nQuickSort na lista decrescente")
rel = Relogio()
quickListas(decrescente)
del rel


print("\n\n\nQUICKSORT PARTICIONADO")

print("\nQuickSort na lista desordenada")
rel = Relogio()
quickSort(desordenada)
del rel

print("\nQuickSort na lista crescente")
rel = Relogio()
quickSort(crescente)
del rel

print("\nQuickSort na lista decrescente")
rel = Relogio()
quickSort(decrescente)
del rel

