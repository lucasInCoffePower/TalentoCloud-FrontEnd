
def bem_vindo():
    '''Exibe o conteudo inicial'''
    print('''
    ##################################################
    Bem-vindo ao Descubra a Classe do Seu Veículo !
    
    O programa mostra a classe do veículo com base no
    peso, quantidade de rodas e quantidade de pessoas.
    ##################################################
    
    ''')


def encerramento():
    '''Exibe o conteúdo final'''
    print('''
    #################################################
    Obrigado. Adeus !
    ################################################''')


def main():
    '''funcao principal'''

    qtd_rodas, peso, qtd_pessoas = 0, 0.0, 0
    
    bem_vindo() # exibe o conteúdo da função bem_vindo
    

    # Recebendo dados
    qtd_rodas = int(input('Digite a quantidade de rodas do veículo: '))
    peso = float(input('Digite o peso do veículo em kilogramas: '))
    qtd_pessoas = int(input('Digite quantas pessoas o veículo pode suportar: '))
    

    # processamento e saída
    if qtd_rodas == 2 or qtd_rodas == 3:
        print('Classe A')
    elif qtd_rodas == 4 and qtd_pessoas <= 8 and peso <= 3500:
        print('Classe B')
    elif qtd_rodas >= 4 and 3500 < peso < 6000:
        print('Classe C')
    elif qtd_rodas >= 4 and qtd_pessoas > 8:
        print('Classe D')
    elif qtd_rodas >= 4 and peso > 6000:
        print('Classe E')
    else:
        print('A classe do veículo não pode ser identificada')


    encerramento() # mensagem de encerramento


if __name__ == '__main__':
    main()
