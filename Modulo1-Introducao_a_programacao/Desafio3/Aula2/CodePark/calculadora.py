# Calculadora
operacoes = {
    '1':'Soma'
    '2':'Subtração'
    '3':'Multiplicação'
    '4':'Divisão'
}

def adicao(n1:float, n2:float):
    '''resultado da soma'''
    return n1+n2


def subtracao(n1:float, n2:float):
    '''operação de subtração'''
    return n1-n2


def multiplicação(n1:float, n2:float):
    '''multiplicação'''
    return n1*n2


def divisao(n1:float, n2:float):
    '''divisao'''
    return 'indeterminação' if n2 == 0 else n1/n2 


def calculadora():
    '''Apresenta e recebe operação, recebe operandos, e calcula resultados'''
    
    print('''
        \nEscolha a operação prosseguir
        1- Soma
        2- Subtração
        3- Multiplicação
        4- Divisão
        5- Sair
        ''')
    
    operacao = input()
    
    if operacao not in operacoes:
        print('Essa operação não existe !')
    elif operacao == '5':
        return False
    else:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        if operacao == '1':
            print('{}+{}={}'.format(numero1, numero2, adicao(numero1, numero2)))
        elif operacao == '2':
            print('{}-{}={}'.format(numero1, numero2, subtracao(numero1, numero2)))
        elif operacao == '3':
            print('{}x{}={}'.format(numero1, numero2, multiplicacao(numero1, numero2)))
        else:
            print('{}/{}={}'.format(numero1, numero2, divisao(numero1, numero2)))

    return True
        
        
def main():
    while calculadora():
        pass


if __name__ == '__main__':
    main()
