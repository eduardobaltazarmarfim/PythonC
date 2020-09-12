from  Objetos.tela import *
from os import system
from time import sleep
from  Objetos.criar import *

arq='eduproject.txt'

if arquivoExiste(arq):

    print('Arquivo encontrado com sucesso!')

else:

    print('Arquivo não encontrado!')

def sistema():

    system('cls')

    while True:

        resposta=menu(['Ver pessoa cadastrada','Cadastrar Pessoa','Sair do Sistema'])

        if resposta==1:

            cabecalho('Opção 1')

        elif resposta==2:

            cabecalho('Opção 2')

        elif resposta==3:

            cabecalho('Saindo do sistema até logo!')

            break

        else:

            cabecalho('Erro! Digite uma opção valida!')

        sleep(2)
    
    pass

sistema()