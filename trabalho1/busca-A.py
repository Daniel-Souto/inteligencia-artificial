#!/usr/bin/env python
# coding: utf-8

# In[4]:


#BUSCA A*

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

mov_min = (2**n_discos) -1
print('Menor numero possivel de movimentos:',mov_min)
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

#A soma do menor numero de movimentos possivel para o problema
#com o numero atual de movimentos
def func_heu(estado, prof): 
    if not estado:
        return -1
    return prof + mov_min


#Modelo de transição
#Dados um estado e uma ação, o modelo de transição de estados retorna todos os estados vizinhos (fronteira)
def sucessor_p(estado):
    #gera todos os estados sucessores nao repetidos
    fronteira = [
        (func_heu(mover(estado[1],'A','B'),estado[2]+1),mover(estado[1],'A','B'),estado[2]+1),
        (func_heu(mover(estado[1],'A','C'),estado[2]+1),mover(estado[1],'A','C'),estado[2]+1),
        (func_heu(mover(estado[1],'B','A'),estado[2]+1),mover(estado[1],'B','A'),estado[2]+1),
        (func_heu(mover(estado[1],'B','C'),estado[2]+1),mover(estado[1],'B','C'),estado[2]+1),
        (func_heu(mover(estado[1],'C','A'),estado[2]+1),mover(estado[1],'C','A'),estado[2]+1),
        (func_heu(mover(estado[1],'C','B'),estado[2]+1),mover(estado[1],'C','B'),estado[2]+1)
    ]
    return [estado for estado in fronteira if estado[1] and estado not in visitado_p]

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

caminho_p = []
vizinhos_p = []
visitado_p = []
print('ESTADO INICIAL')
pprint(estado_inicial)
ei=(0,estado_inicial,0)
sucessor_p(ei)

caminho = []

def solucao_p(estado):
    while visitado_p:
        profv = visitado_p[-1][2]
        if caminho_p:
            profc = caminho_p[-1][2]
        else:
            profc =10000
        if profv != profc:
            if caminho_p:
                vizinhos = sucessor(caminho_p[-1][1])
                if visitado_p[-1][1] in vizinhos and visitado_p[-1][2] != caminho_p[-1][2]:
                    caminho_p.append(visitado_p.pop())
                else:
                    visitado_p.pop()
            else:
                caminho_p.append(visitado_p.pop())
        else:
            visitado_p.pop()
    caminho_p.reverse()

        
#Busca gulosa
def busca_A(fronteira):
    if not fronteira:
        return None
    #remove o proximo elemento da fronteira (Busca gulosa - FIFO ordenada pela funcao heuristica)
    nodo = fronteira.pop(0)
    if nodo[1] in visitado:
        return None
    if nodo[0] > 2*mov_min: #ignora qualquer no que ultrapasse o
        return None         #menor numero possivel de movimentos para o problema
    print('SOLUCAO ATUAL')
    pprint(nodo)
    visitado_p.append(nodo)
    visitado.append(visitado_p[-1][1])
    #Testa o objetivo
    if nodo[1] == estado_final:
        print('SOLUCAO FINAL')
        pprint(nodo)
        solucao_p(nodo)
        while fronteira:
            fronteira.pop(0)
        return None
    #Gera os sucessores do estado atual
    vizinhos_p = sucessor_p(nodo)
    #print('VIZINHOS')
    #pprint(vizinhos_p)
    fronteira += vizinhos_p
    fronteira.sort(key = lambda h: h[0])
    #print('FRONTEIRA')
    #pprint(fronteira)
    
def custo(caminho_p):
    soma = 0
    i = 0
    while i < len(caminho_p):
        soma += caminho_p[i][0]
        i += 1
    return soma 

caminho_p = []
vizinhos_p = []
visitado_p = []
fronteira = [(0,estado_inicial,0)]
while fronteira:
    busca_A(fronteira)
print('Caminho')
print('(val func heuristica , estado, profundidade)')
pprint(caminho_p)
print('Resultado alcancado apos',len(visitado),'buscas.')
print('Custo total:',custo(caminho_p))


# In[ ]:




