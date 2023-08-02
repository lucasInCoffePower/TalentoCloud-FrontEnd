def regar(planta:int):
    print(f'Regar planta {planta+1}')
    return planta


def main():
    qtd_plantas = 5
    planta = 0
    while regar(planta) < qtd_plantas :
         planta +=1      


if __name__ == '__main__':
    main()
