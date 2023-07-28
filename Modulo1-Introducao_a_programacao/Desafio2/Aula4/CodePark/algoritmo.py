



def algoritmoPrints():
    '''Implementa um algoritmo com prints'''
    print(20, end='\n')
    print(19, end='\n')
    print(18, end='\n')
    print(17, end='\n')
    print(16, end='\n')
    print(15, end='\n')
    print(14, end='\n')
    print(12, end='\n')
    print(11, end='\n')
    print(10, end='\n')
    print(9, end='\n')
    print(8, end='\n')
    print(7, end='\n')
    print(6, end='\n')
    print(5, end='\n')
    print(4, end='\n')
    print(3, end='\n')
    print(2, end='\n')
    print(1, end='\n')


def algoritmoFor():
    '''Implementa a estrutura for'''
     
    [print(i, end='\n') for i in range(20,0,-1) if i != 13]
        


def algoritmoWhile():
    '''Implementa a estrutura while'''

    contador = 20

    while contador != 0:
        print(contador)
        if contador == 14:
            contador -=2
        else:
            contador -=1

        

def main():
    print('#########Algoritmo com prints ############')
    algoritmoPrints()
    print('\n########Algoritmo com for   ############')
    algoritmoFor()
    print('\n########Algoritmo com while ############')
    algoritmoWhile()
    



if __name__ == '__main__':
    main()
