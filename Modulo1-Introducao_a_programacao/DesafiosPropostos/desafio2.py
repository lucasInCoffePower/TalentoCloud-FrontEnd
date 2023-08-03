# desafio 2

legumes = {
        0: 'tomate',
        1: 'tomate',
        2: 'batata',
        3: 'batata',
        4: 'tomate',
        5: 'tomate'
        }


def regarLegume(legume:str):
        return f'Regando {legume}'


def algoritmoRegar1(leg:str):
    [print(regarLegume(legume)) for legume in legumes.values() if leg == legume]



def main():
    legume_regar = 'tomate'
    algoritmoRegar1(legume_regar)



if __name__ == '__main__':
    main()
