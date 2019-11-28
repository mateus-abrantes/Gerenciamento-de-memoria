def inicializar_tabela_de_pagina(tabela_de_pagina,n):
    for i in range(0,n):
        tabela_de_pagina[i] = 0

def print_tabela_de_pagina(tabela_de_pagina, n):
    for i in range(0,n):
        print(tabela_de_pagina[i])


ref_arquivo = open("sequencia02.dat","r")
tabela_de_pagina = [False]*1024
inicializar_tabela_de_pagina(tabela_de_pagina,1024)
acerto_pagina = 0
falha_pagina=0
acesso_memoria=0
operacao_ES=0
for endereco in ref_arquivo:
    pagina = int(endereco)//64
    #acesso a memoria para leitura da tabela de paginas
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
ref_arquivo.close()
print("RESULTADOS SEQUENCIA 2:")
print("QUANTIDADE DE ACERTOS DE PAGINA:",acerto_pagina)
print("QUANTIDADE DE FALHAS DE PAGINA:",falha_pagina)
print("QUANTIDADE DE ACESSOS A MEMORIA:",acesso_memoria)
print("QUANTIDADE DE OPERACOES DE E/S REALIZADAS:",operacao_ES);
