
def regarComWhile(legumes:list):
    qtd_legumes = len(legumes)
    legume = 0
    while legume < qtd_legumes:
        print(f'Reguei {legumes[legume]}')
        legume +=2
    

def regarComFor(legumes:list):
    for i, legume in enumerate(legumes):
        if i%2==0:
            print('Reguei {} {ordem}'.format(legume, ordem=(i+1)))


def main():
    legumes = ['tomate', 'batata', 'tomate', 'batata', 'tomate', 'batata']
    regarComFor(legumes)
    regarComWhile(legumes)
   


if __name__ == '__main__':
    main()
