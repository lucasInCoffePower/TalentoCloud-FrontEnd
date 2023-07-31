# Calculadora

def adicao(n1:float, n2:float):
    '''resultado da soma'''
    return n1+n2


def subtracao(n1:float, n2:float):
    '''operação de subtração'''
    return n1-n2


def multiplicacao(n1:float, n2:float):
    '''multiplicação'''
    return n1*n2


def divisao(n1:float, n2:float):
    '''divisao'''
    return 'indeterminação' if n2 == 0 else n1/n2 


operacoes = {
    '1': (adicao, '+'),
    '2': (subtracao, '-'),
    '3': (multiplicacao, 'x'),
    '4': (divisao, '÷')
}


def calculadora():
    '''Apresenta e recebe operação, recebe operandos, e calcula resultados'''
    
    print('''
        \nEscolha a operação prosseguir
        1- Adição
        2- Subtração
        3- Multiplicação
        4- Divisão
        5- Sair
        ''')
    
    operacao = input()
    
    if operacao not in operacoes:
        print('Essa operação não existe !')
    elif operacao != '5':
        num1 = float(input('Digite o primeiro número'))
        num2 = float(input('Digite o segundo número'))
        resultado = operacoes[operacao]
        print('{}{}{}={}'.format(num1, resultado[1], num2, resultado[0](num1, num2)))
    else:
        return False
    return True
        
        
def main():
    while calculadora():
        pass


if __name__ == '__main__':
    main()
