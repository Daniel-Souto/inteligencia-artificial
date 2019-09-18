#!/usr/bin/env python
# coding: utf-8

# In[5]:


#BUSCA HILL CLIMBING

from pprint import pprint
from copy import deepcopy

#ESTADO INICIAL [tempo_restante,n_patinetes,n_monociclos, lucro]
estado_inicial = [1200, 0, 0, 0]
print('ESTADO INICIAL')
pprint(estado_inicial)
visitado = []

#ESTADO FINAL maximizar lucro
def lucro(n_patinetes, n_monociclos):
    return 1000*n_patinetes + 1800*n_monociclos

#ACOES
acoes = ['fazer_patinete','fazer_monociclo']

#MODELO DE TRANSICAO
def fazer_patinete(estado):
    if estado[1] < 40 and estado[0] >= 20:
        estado = deepcopy(estado)
        estado[1] +=1
        estado[0] -= 20
        estado[3] = lucro(estado[1],estado[2])
        return estado
    else:
        return None
        
def fazer_monociclo(estado):
    if estado[2] < 30 and estado[0] >= 30:
        estado = deepcopy(estado)
        estado[2] +=1
        estado[0] -= 30
        estado[3] = lucro(estado[1],estado[2])
        return estado
    else:
        return None
        
def sucessor(estado):
    #gera todos os estados sucessores nao repetidos
    fronteira = [
        fazer_patinete(estado),
        fazer_monociclo(estado)
    ]
    return [estado for estado in fronteira if estado and estado not in visitado]

#TESTE DO OBJETIVO (so interessa o maior valor possivel)
def max_lucro(estado,vizinho):
    if vizinho[3] > estado[3]:  #lucro do vizinho maior que o atual
        return vizinho[3]
    else:
        return estado[3]
    
    
#BUSCA HILL CLIMBING
def hill_climbing(fronteira):
    #pprint(fronteira)
    nodo = fronteira.pop(0)
    #pprint(nodo)
    #pprint(fronteira)
    if nodo in visitado:
        return None
    if nodo[0] < 30:
        if nodo[1] == 40:
            while fronteira:
                fronteira.pop()
            return nodo
        else:
            if nodo[0] < 20:
                while fronteira:
                    fronteira.pop()
                return nodo
    print('SOLUCAO ATUAL')
    pprint(nodo)
    visitado.append(nodo)
    vizinhos = sucessor(nodo)
    vizinhos.sort(key = lambda l: l[3])  # ajeita de acordo com o lucro (crescente)
    vizinhos.reverse()
    print('VIZINHOS')
    pprint(vizinhos)
    maxL = max_lucro(nodo,vizinhos[0])
    if maxL == nodo[3]: #atingiu um pico
        while fronteira:
            fronteira.pop()
        return nodo
    fronteira += [estado for estado in vizinhos if estado[3] == maxL]
    #print('FRONTEIRA')
    #pprint(fronteira)

sucessor(estado_inicial)
maxL = 0
fronteira = [estado_inicial]

while fronteira:
    estado_final = hill_climbing(fronteira)

print('ESTADO FINAL:')
print('Tempo restante:',estado_final[0])
print('Numero de patinetes:',estado_final[1])
print('Numero de monociclos',estado_final[2])
print('Lucro:',estado_final[3])
print('Resultado alcancado apos',len(visitado),'buscas.')


# In[ ]:




