def linha(tam=42):

    return '-'*tam

def cabecalho(titulo):

    print(linha())
    
    print(f'{titulo:^42}')

    print(linha())

    pass

def menu(lista):

    cabecalho('Menu Principal')

    c=1

    for item in lista:

        print('{} - {}'.format(c,item))

        c+=1
        
    print(linha())
    opc=int(input('Sua Opção: '))

    return opc

    pass
