#!/usr/bin/env python
# coding: utf-8

# In[2]:


#BUSCA DE CUSTO UNIFORME

from pprint import pprint
from copy import deepcopy

print('Insira o numero de discos:')
n_discos = int(input())

#Estado Inicial 
estado_inicial = {
    'A':[i for i in range(n_discos,0,-1)],
    'B':[],
    'C':[]
}

#Estado final
estado_final = {
    'A':[],
    'B':[],
    'C':[i for i in range(n_discos,0,-1)]
}

visitado = []

#Ações
acoes = [
    'mover_A_B',
    'mover_A_C',
    'mover_B_A',
    'mover_B_C',
    'mover_C_A',
    'mover_C_B'
]

def mover(estado, origem, destino):
    if not estado[origem]:
        return None
    if not estado[destino]:
        estado = deepcopy(estado)
        estado[destino].append(estado[origem].pop())
        return estado
    elif estado[destino][-1] > estado[origem][-1]:
        estado = deepcopy(estado)
        estado[destino].append(estado[origem].pop())
        return estado
    else:
        return None

#Modelo de transição
#Dados um estado e uma ação, o modelo de transição de estados retorna todos os estados vizinhos (fronteira)
def sucessor_p(estado):
    #gera todos os estados sucessores nao repetidos
    fronteira_p = [
        (estado[0] + 1, mover(estado[1],'A','B')),
        (estado[0] + 1, mover(estado[1],'A','C')),
        (estado[0] + 1, mover(estado[1],'B','A')),
        (estado[0] + 1, mover(estado[1],'B','C')),
        (estado[0] + 1, mover(estado[1],'C','A')),
        (estado[0] + 1, mover(estado[1],'C','B'))
    ]
    return [estado for estado in fronteira_p if estado[1] and estado[1] not in visitado]

print('ESTADO INICIAL')
pprint(estado_inicial)
ei = (0,estado_inicial)
sucessor_p(ei)

def sucessor(estado):
    #gera todos os estados sucessores nao repetidos
    fronteira = [
        mover(estado,'A','B'),
        mover(estado,'A','C'),
        mover(estado,'B','A'),
        mover(estado,'B','C'),
        mover(estado,'C','A'),
        mover(estado,'C','B')
    ]
    return [estado for estado in fronteira if estado and estado]

def solucao_p(estado):
    while visitado_p:
        profv = visitado_p[-1][0]
        if caminho_p:
            profc = caminho_p[-1][0]
        else:
            profc =10000
        if profv != profc:
            if caminho_p:
                vizinhos = sucessor(caminho_p[-1][1])
                if visitado_p[-1][1] in vizinhos:
                    caminho_p.append(visitado_p.pop())
                else:
                    visitado_p.pop()
            else:
                caminho_p.append(visitado_p.pop())
        else:
            visitado_p.pop()
    caminho_p.reverse()

#busca de custo uniforme
def busca_custo_uniforme(fronteira_p):
    if not fronteira_p:
        return None
    #remove o proximo elemento da fronteira (Busca de custo uniforme - FIFO ordenada pelo custo da acao)
    #print('FRONTEIRA_P')
    #pprint(fronteira_p)
    nodo_p = fronteira_p.pop(0)
    if nodo_p in visitado_p:
        return None
    print('SOLUCAO ATUAL')
    pprint(nodo_p)
    visitado_p.append(nodo_p)
    visitado.append(visitado_p[len(visitado_p)-1][1])
    #print('VISITADO')
    #pprint(visitado)
    #Testa o objetivo
    if nodo_p[1] == estado_final:
        print('SOLUCAO FINAL')
        pprint(nodo_p[1])
        solucao_p(nodo_p)
        while fronteira_p:
            fronteira_p.pop(0)
        return None
    #Gera os sucessores do estado atual
    vizinhos_p = sucessor_p(nodo_p)
    #print('VIZINHOS')
    #pprint(vizinhos)
    fronteira_p += vizinhos_p
    fronteira_p.sort(key = lambda p: p[0])

def custo(caminho_p):
    return len(caminho_p) - 1
    
caminho_p = []
fronteira_p = [(0,estado_inicial)]
vizinhos_p = []
visitado_p = []

while fronteira_p:
    busca_custo_uniforme(fronteira_p)

print('Caminho')
pprint(caminho_p)
print('Resultado alcancado apos',len(visitado),'buscas.')
print('Custo total:',custo(caminho_p),'movimentos.')


# In[ ]:




