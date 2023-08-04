# Valor inválido
# Menor que zero
# não divisível por 2 e por 3

def main():
    
    while True:
        try:
            numero = int(input('Digite um número: '))
            if numero < 0:
                raise Exception('Menor que 0')
            elif numero > 100:
                raise Exception('Maior que 100')
            elif numero%2!=0 and numero%3!=0:
                raise Exception('Não é divisível por 2 e por 3')
        except ValueError as e:
            print('Ocorreu um erro: {}'.format(e))
        except Exception as e:
            print('Um erro ocorreu: {}'.format(e))
        else:
            break
        

    

if __name__ == '__main__':  
    main()
