from controle import *
from relogio import *

print("Testes dos piores casos da Lista Duplamente Encadeada")

placasAleatorias = []
c = Controle("veiculos.txt", "SAMPLE", "", True)
placasAleatorias = c.getSample()

print("\n\nLeitura do arquivo")
print("Inserção em fila - O(1)")
c = Controle("veiculos.txt", "L2E", "", True)
numeros = [1, 100, 500, 1000, 5000]
tempos = c.testarLeitura(numeros)
numeros.append(20000)
print(str(numeros[0]), "elemento\t\t", str(tempos[0]))
for i in range(1, len(numeros)):
    print(str(numeros[i]), "elementos\t\t", str(tempos[i]))


print("\n\nBusca por placa")
print("Último item do arquivo desordenado")
rel = Relogio()
c.pesquisarPlaca("PGD-8507")
del rel
print("Último item do arquivo crescente")
rel = Relogio()
c.pesquisarPlaca("PZZ-9459")
del rel
print("Último item do arquivo decrescente")
rel = Relogio()
c.pesquisarPlaca("OAA-3655")
del rel
print("\n500 placas aleatórias")
rel = Relogio()
for i in placasAleatorias:
    c.pesquisarPlaca(i)
del rel



print("\n\nPop")
#Também funciona por índice, mas como O(n)
print("Último item da lista - O(1)")
rel = Relogio()
c.veiculos.pop()
del rel

print("\n\nLeitura do arquivo desordenado")
print("Inserção ordenada crescente - O(n)")
c = Controle("veiculos.txt", "L2E", "CRES", True)
numeros = [1, 100, 500, 1000, 5000]
tempos = c.testarLeitura(numeros)
numeros.append(20000)
print(str(numeros[0]), "elemento\t\t", str(tempos[0]))
for i in range(1, len(numeros)):
    print(str(numeros[i]), "elementos\t\t", str(tempos[i]))
    
print("\n\nLeitura de um arquivo crescente")
print("Inserção ordenada crescente - O(n)")
c = Controle("veiculosCrescente.txt", "L2E", "CRES", True)
numeros = [1, 100, 500, 1000, 5000]
tempos = c.testarLeitura(numeros)
numeros.append(20000)
print(str(numeros[0]), "elemento\t\t", str(tempos[0]))
for i in range(1, len(numeros)):
    print(str(numeros[i]), "elementos\t\t", str(tempos[i]))
    

print("\n\nBusca por placa")
print("Último item do arquivo desordenado")
rel = Relogio()
c.pesquisarPlaca("PGD-8507")
del rel
print("Último item do arquivo crescente")
rel = Relogio()
c.pesquisarPlaca("PZZ-9459")
del rel
print("Último item do arquivo decrescente")
rel = Relogio()
c.pesquisarPlaca("OAA-3655")
del rel
print("\n500 placas aleatórias")
rel = Relogio()
for i in placasAleatorias:
    c.pesquisarPlaca(i)
del rel

print("\n\nLeitura do arquivo desordenado")
print("Inserção ordenada decrescente - O(n)")
c = Controle("veiculos.txt", "L2E", "DECR", True)
numeros = [1, 100, 500, 1000, 5000]
tempos = c.testarLeitura(numeros)
numeros.append(20000)
print(str(numeros[0]), "elemento\t\t", str(tempos[0]))
for i in range(1, len(numeros)):
    print(str(numeros[i]), "elementos\t\t", str(tempos[i]))
    
print("\n\nLeitura de um arquivo decrescente")
print("Inserção ordenada decrescente - O(n)")
c = Controle("veiculosDecrescente.txt", "L2E", "DECR", True)
numeros = [1, 100, 500, 1000, 5000]
tempos = c.testarLeitura(numeros)
numeros.append(20000)
print(str(numeros[0]), "elemento\t\t", str(tempos[0]))
for i in range(1, len(numeros)):
    print(str(numeros[i]), "elementos\t\t", str(tempos[i]))
    

print("\n\nBusca por placa")
print("Último item do arquivo desordenado")
rel = Relogio()
c.pesquisarPlaca("PGD-8507")
del rel
print("Último item do arquivo crescente")
rel = Relogio()
c.pesquisarPlaca("PZZ-9459")
del rel
print("Último item do arquivo decrescente")
rel = Relogio()
c.pesquisarPlaca("OAA-3655")
del rel
print("\n500 placas aleatórias")
rel = Relogio()
for i in placasAleatorias:
    c.pesquisarPlaca(i)
del rel



input()
