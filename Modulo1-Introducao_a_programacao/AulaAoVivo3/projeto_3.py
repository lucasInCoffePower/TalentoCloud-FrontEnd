

TABUADAS ={
        1:'tabuada do 1',
        2:'tabuada do 2',
        3:'tabuada do 3',
        4:'tabuada do 4',
        5:'tabuada do 5',
        6:'tabuada do 6',
        7:'tabuada do 7',
        8:'tabuada do 8',
        9:'tabuada do 9'
        }


def multiplicacao(fator1:int, fator2:int):
    return fator1*fator2


def gerarTabuada(numero:int, tamanho:int, tabuada:str ):
    print('#####{}#####'.format(tabuada))
    for valor_variavel in range(tamanho):
        resultado = valor_variavel*numero
        print(f'{valor_variavel}x{numero}={resultado}')


def main():
    tam_tabuada = 10
    for tabuada in TABUADAS:
        gerarTabuada(tabuada, tam_tabuada, TABUADAS[tabuada])
        

if __name__ == '__main__':
    main()
