# Resolução do desafio 1
legumes = ['tomate', 'tomate', 'tomate', 'batata', 'batata', 'batata']


def algoritmoRegagem2():
    # utilizamos list comprehension
    _ = [print(regarLegume(legume)) for legume in legumes if legume[0] == 'b']

def algoritmoRegagem1():
    _ = [print(regarLegume(legume)) for i, legume in enumerate(legumes) if i>2]  


def regarLegume(legume:str):
    return 'Regando {}'.format(legume)


def main():
    algoritmoRegagem1()
    algoritmoRegagem2()    



if __name__ == '__main__':
    main()
