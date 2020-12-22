from listagem import *

def menu():
    options = ['Listar Marketplaces', 'Listar Categorias por Marketplace',
               'Listar Subcategoria por Categoria', 'Sair']

    print('\nOPÇÕES: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')

    op = int(input('Selecione uma opção: '))
    return op

while True:
    try:
        op = menu()
        if op == 1:
            print(exibir_marketplaces())
        elif op == 2:
            print(exibir_categorias()) 
        elif op == 3:
            print(exibir_subcategorias()) 
        elif op == 4:
            exit(0)
        else:
            print('Opção indisponível. Tente novamente.')
    except ValueError:
        print('Opção indisponível. Tente novamente.')