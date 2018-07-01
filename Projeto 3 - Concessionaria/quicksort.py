
def particao(lista, esquerda, direita):
    pivo = lista[esquerda]
    i = esquerda
    j = direita + 1
    while True:
        i += 1
        while lista[i] < pivo:
            if i >= direita:
                break
            i += 1
        j -= 1
        while lista[j] > pivo:
            if j <= esquerda:
                break
            j -= 1
        if i >= j:
            break
        lista[i], lista[j] = lista[j], lista[i]
    lista[esquerda], lista[j] = lista[j], lista[esquerda]
    return j

def quick(lista, esquerda, direita):
    if esquerda >= direita:
        return
    p = particao(lista, esquerda, direita)
    quick(lista, esquerda, p-1)
    quick(lista, p+1, direita)

def quickSort(lista):
    quick(lista, 0, len(lista) - 1)
    return lista
    

def quickListas(lista):
    if not lista:
        return []
    else:
        pivo = lista.pop(0)
        menores = [x for x in lista if x.getPlaca() < pivo.getPlaca()]
        maiores = [x for x in lista if x.getPlaca() >= pivo.getPlaca()]
        return quickListas(menores) + [pivo] + quickListas(maiores)
