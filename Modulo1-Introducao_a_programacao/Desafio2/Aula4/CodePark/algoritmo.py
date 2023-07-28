# Algoritmo

def algoritmoPrints():
    '''Implementa um algoritmo com prints'''
    print(20)
    print(19)
    print(18)
    print(17)
    print(16)
    print(15)
    print(14)
    print(12)
    print(11)
    print(10)
    print(9)
    print(8)
    print(7)
    print(6)
    print(5)
    print(4)
    print(3)
    print(2)
    print(1)


def algoritmoFor():
    '''Implementa a estrutura for'''
     andares = range(20, 0, -1)
    for andar in andares:
        if andar != 13:
            print(andar)


def algoritmoWhile():
    '''Implementa a estrutura while'''
    andar = 20
    while andar != 0:
        if andar != 13:
            print(andar)
        conntador -=1

        
def main():
    print('#########Algoritmo com prints ############')
    algoritmoPrints()
    print('\n########Algoritmo com for   ############')
    algoritmoFor()
    print('\n########Algoritmo com while ############')
    algoritmoWhile()
    

if __name__ == '__main__':
    main()
