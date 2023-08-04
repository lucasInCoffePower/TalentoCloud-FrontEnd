# Valor inválido
# Menor que zero
# não divisível por 2 e por 3


def validar_numero(numero):
        if numero < 0:
            raise ValueError('Menor que 0')
        elif numero > 100:
            raise ValueError('Maior que 100')
        elif numero%2!=0 and numero%3!=0:
            raise ValueError('Não é divisível por 2 e por 3')


def main():
    while True:
        try:
            numero = int(input('Digite um número: '))
            validarNumero(numero)
        except ValueError as e:
            print('Ocorreu um erro: {}'.format(e))
        except Exception as e:
            print('Um erro ocorreu: {}'.format(e))
        
        
if __name__ == '__main__':  
    main()
