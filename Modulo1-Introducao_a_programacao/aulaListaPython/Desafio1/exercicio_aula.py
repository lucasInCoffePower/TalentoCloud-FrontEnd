nomes = ('Carlos', 'David', 'Stephanie', 'Angela')


def receber_nome():
    return input('Digite o seu nome: ')


def buscar_nome(nome:str):
    return True if nome in nomes else False


def main():
    if buscar_nome(receber_nome()):
        print('A pessoa foi encontrada')
    else:
        print('A pessoa não foi encontrada')


if __name__ == '__main__':
    main()
