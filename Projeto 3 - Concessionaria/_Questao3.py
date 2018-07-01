from controle import *
from relogio import *

print("Teste da Árvore Binária")

placasAleatorias = []
c = Controle("veiculos.txt", "PYTHON", "SAMPLE", True)
placasAleatorias = c.getSample()

print("\n\nLeitura do arquivo")
print("Inserção binária - O(log n)")
c = Controle("veiculos.txt", "AB", "", True)
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
print("Item anterior - O(log n)")
rel = Relogio()
c.veiculos.popItem("PGD-8507")
del rel


print("\n\n\nTeste dos piores casos da Árvore Binária")


print("\n\nLeitura de um arquivo crescente")
print("Inserção binária - O(n)")
c = Controle("veiculosCrescente.txt", "AB", "", True)
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
print("Item anterior - O(n)")
rel = Relogio()
c.veiculos.popItem("PZZ-9459")
del rel

print("\n\nLeitura de um arquivo decrescente")
print("Inserção binária - O(n)")
c = Controle("veiculosDecrescente.txt", "AB", "", True)
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
