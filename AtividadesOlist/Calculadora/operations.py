def soma(numero1: float, numero2: float)->float:
    if valida_float(numero1) and valida_float(numero2):
        soma = numero1 + numero2
        return soma

def subtracao(numero1: float, numero2: float)->float:
    if valida_float(numero1) and valida_float(numero2):
        sub = numero1 - numero2
        return sub

def multiplicacao(numero1: float, numero2: float)->float:
    if valida_float(numero1) and valida_float(numero2):
        mult = numero1 * numero2
        return mult

def divisao(numero1: float, numero2: float)->float:
    if valida_float(numero1) and valida_float(numero2):
        if numero2 != 0:
            div = numero1/numero2
            return div
        else:
            print('Dividendo não pode ser 0')


def valida_float(numero: float)->bool:
    if isinstance(numero, float):
        return True
    raise ValueError(f'{numero} não é numérico')