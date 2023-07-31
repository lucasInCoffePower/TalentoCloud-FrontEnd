# Calculadora


def menuOperacoes():
    '''Apresenta as operações'''
    print('''
        \nEscolha a operação prosseguir
        1- Soma
        2- Subtração
        3- Multiplicação
        4- Divisão
        5- Sair
        ''')



def calculadora():
    '''Recebe operação e operandos, e calcula resultados'''
    menuOperacoes()
    operacao = int(input())
    
    if operacao == 5:
        return False
    elif operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4:
        print('Operação inválida')
    else:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        if operacao == 1:
            soma = numero1+numero2
            print('{}+{}={}'.format(numero1, numero2,soma))
        elif operacao == 2:
            diferenca = numero1-numero2
            print('{}-{}={}'.format(numero1, numero2, diferenca))
        elif operacao == 3:
            produto = numero1*numero2
            print('{}x{}={}'.format(numero1, numero2, produto))
        else:
            razao = 'Indeterminação' if numero2 == 0 else numero1/numero2
            print('{}/{}={}'.format(numero1, numero2, razao))

    return True
        
        
def main():
    while calculadora():
        pass


if __name__ == '__main__':
    main()
