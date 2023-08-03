# desafio 3


plantas = {
        0:'tomate',
        1:'batata',
        2:'cenoura',
        3:'tomate',
        4:'batata',
        5:'cenoura'
        }


def regarPlantas(planta:str):
    return 'Regando ' + planta


def algoritmoRegagem():
    chaves_invertidas = sorted(plantas.keys(), reverse=True)
    _ = [print(regarPlantas(plantas[posicao])) for posicao in chaves_invertidas]    


def main():
    algoritmoRegagem()
    


if __name__ == '__main__':
    main()
