#!/usr/bin/env python
# coding: utf-8

# In[6]:


#BUSCA TABU

from pprint import pprint
from copy import deepcopy

#ESTADO INICIAL [tempo_restante,n_patinetes,n_monociclos, lucro]
estado_inicial = [1200, 0, 0, 0]
print('ESTADO INICIAL')
pprint(estado_inicial)

visitado = []
sucessor(estado_inicial)
maxL = 0
fronteira = [estado_inicial]
melhor_estado = estado_inicial
melhor_candidato = estado_inicial
tabu = []
tabu.append(estado_inicial)

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
    
    
#BUSCA TABU
def busca_tabu(fronteira,melhor_estado):
    nodo = fronteira.pop(0)
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
    #print('VIZINHOS')
    #pprint(vizinhos)
    i = 0
    while i < len(vizinhos): #acha o melhor candidato entre os vizinhos
        if vizinhos[i] not in tabu and vizinhos[i][3] > nodo[3]:
            melhor_candidato = vizinhos[i]
        if melhor_candidato[3] > melhor_estado[3]:
            melhor_estado = melhor_candidato
        tabu.append(nodo)
        i += 1
    print('MELHOR VIZINHO')
    pprint(melhor_candidato)
    fronteira += [candidato for candidato in vizinhos if candidato == melhor_candidato]
    print('FRONTEIRA')
    pprint(fronteira)
    return melhor_estado


fronteira = [estado_inicial]

while fronteira:
    estado = busca_tabu(fronteira,melhor_estado)
    melhor_estado = estado

print('ESTADO FINAL:')
print('Tempo restante:',melhor_estado[0])
print('Numero de patinetes:',melhor_estado[1])
print('Numero de monociclos',melhor_estado[2])
print('Lucro:',melhor_estado[3])
print('Resultado alcancado apos',len(visitado),'buscas.')


# In[ ]:




