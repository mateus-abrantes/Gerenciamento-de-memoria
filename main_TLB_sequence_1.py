import matplotlib.pyplot as plt
from collections import deque
cont = 0 
def inicializar_tabela_de_pagina(tabela_de_pagina,n):
    for i in range(0,n):
        tabela_de_pagina[i] = 0

def print_tabela_de_pagina(tabela_de_pagina, n):
    for i in range(0,n):
        print(tabela_de_pagina[i])
def create_TLB(TLB_line,n):
    TLB = []
    for i in range(0,n):
        TLB.append(TLB_line.copy())
    return TLB  

def verificar_TLB(TLB,pagina):
    #Procura em toda a TLB com validade verdadeira
    for i in range(0,len(TLB)):
        if(TLB[i]['validade'] == True):
            #Se nas linhas validas se encontra a pagina procurada
            if(TLB[i]['pagina'] == pagina):
                return True
    return False
def atualizar_TLB(TLB,pagina,fila_TLB):
    #Procura na TLB se existe uma linha com validade false disponivel
    for i in range(0,len(TLB)):
        #Se tiver e carregada nessa linha a pagina e coloca com validade true
        if(TLB[i]['validade'] == False):
            TLB[i]['pagina'] = pagina
            TLB[i]['validade'] = True
            #Adiciona a posicao ocupada na fila da TLB FIFO
            fila_TLB.append(i)
            return TLB,fila_TLB
    #Se nao existirem linhas com validade false pegamos a posicao da primeira linha com validade true 
    #colocada na TLB (fila TLB FIFO) e substituimos pela nova pagina 
    posicao = fila_TLB.popleft()
    TLB[posicao]['pagina'] = pagina
    TLB[posicao]['validade'] = True
    #Adiciona a posicao ocupada na fila da TLB FIFO
    fila_TLB.append(posicao)
    return TLB,fila_TLB

ref_arquivo = open("sequencia01.dat","r")
tabela_de_pagina = [False]*1024
inicializar_tabela_de_pagina(tabela_de_pagina,1024)
fila_TLB = deque([])
TLB_line = {"pagina":None,"validade":False}
TLB = create_TLB(TLB_line,128)
acerto_TLB = 0
falha_TLB = 0
acerto_pagina = 0
falha_pagina=0
acesso_memoria=0
operacao_ES=0
for endereco in ref_arquivo:
    pagina = int(endereco)//64
    #acesso a memoria para leitura da tabela de paginas
    acesso_memoria+=1
    #Verificar TLB
    if(verificar_TLB(TLB,pagina) == True):
        #incrementa acerto da TLB
        acerto_TLB+=1
        #incrementa acesso a memoria
        acesso_memoria+=1
    else:
        #incrementa falha da TLB
        falha_TLB+=1
        #incrementa acesso a memoria
        acesso_memoria+=1
        #Verificar na tabela de pagina
        if(tabela_de_pagina[pagina] == True):
        #A pagina ja esta na memoria principal
            acerto_pagina+=1
        #Acesso da memoria para a leitura do dado do endereco
            acesso_memoria+=1
        else:
        #A pagina nao se encontra na tabela de paginas
        # ou seja a página não está ainda na memória principal
            falha_pagina+=1
        # SO vai acessar o disco e colocar a página para a memória principal
            operacao_ES+=1
        #Atualizar a tabela de pagina informando que a pagina agora esta carregada na memoria principal
            tabela_de_pagina[pagina] = True
        #Atualizar a TLB
            TLB,fila_TLB = atualizar_TLB(TLB,pagina,fila_TLB)

ref_arquivo.close()
print("RESULTADOS SEQUENCIA 1:")
print("QUANTIDADE DE ACERTOS DE PAGINA:",acerto_pagina)
print("QUANTIDADE DE FALHAS DE PAGINA:",falha_pagina)
print("QUANTIDADE DE ACESSOS A MEMORIA:",acesso_memoria)
print("QUANTIDADE DE OPERACOES DE E/S REALIZADAS:",operacao_ES)
print("QUANTIDADE DE FALHAS NA TLB:",falha_TLB)
print("QUANTIDADE DE ACERTOS NA TLB:",acerto_TLB)
y = [acerto_pagina,falha_pagina,acesso_memoria,operacao_ES,falha_TLB,acerto_TLB]
x = ["ACERTOS DE PAGINA","FALHAS DE PAGINA","ACESSO A MEMORIA","OPERACOES DE E/S","FALHAS NA TLB","ACERTOS NA TLB"]
plt.bar(x,y,color="red")
plt.xticks(x)
plt.ylabel("Qtd.")
plt.xlabel("Variaveis")
plt.title("Resultados para a sequencia 1")
plt.show()
