# Progrma calculadora
# Cálcula o resultado de uma expressão aritmética entre dois valores para as operações de adição, subtração, multiplicação e divisão



def calcularOperacao(numero1:float, numero2:float, operacao:str):
    '''
        Função para cálcular a operação entre dois floats
        Recebe 3 valores: dois floats como operandos e um string como operador
        Returna um tipo float: resultado da operação
    '''

    if operacao == '+':
        resultado = numero1+numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    elif operacao == '/' and numero2 != 0:
        resultado = numero1/numero2
    else:
        resultado = 0
    return resultado




def main():
    num1 = float(input('Insira o primeiro número: '))
    num2 = float(input('Insira o segundo número: '))
    operador = input('Insira a operação que deseja executar(+, -, *, /)')

    resultado_operacao = calcularOperacao(num1, num2, operador)
    print('{} {} {} =  {}'.format(num1, operador, num2, resultado_operacao))
    
    


if __name__ == '__main__':
    main()
