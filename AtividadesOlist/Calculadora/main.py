from operations import soma, subtracao, multiplicacao, divisao

def menu():
    options = ['Soma', 'Subtração', 'Multiplicação', 'Divisão']

    print('\nOPÇÕES: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')

    op = int(input('Selecione uma opção: '))
    return op

while True:
    try:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        op = menu()
        if op == 1:
            resultado = soma(numero1, numero2) 
        elif op == 2:
            resultado = subtracao(numero1, numero2) 
        elif op == 3:
            resultado = multiplicacao(numero1, numero2) 
        elif op == 4:
            resultado = divisao(numero1, numero2) 
        else:
            print('Opção indisponível. Tente novamente.')
    except ValueError:
        print('Opção indisponível. Tente novamente.')

    if resultado is not None:
        print(f'Resultado = {resultado}')