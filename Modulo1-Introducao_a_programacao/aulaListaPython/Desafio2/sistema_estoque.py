import os

estoque = ['Banana','Maçã','Teclado','Arroz','Feijão','Biscoito','Refrigerante']

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def inserir_produto(produto):
    estoque.append(produto)


def ver_estoque():
    print('##############Estoque################')
    for i, produto in enumerate(estoque):
        print('|', i,'-', produto, end ='| ')
    print('\n')


def buscar_produto(produto:str):
    if produto in estoque:
        print('Produto encontrado !')
        return True
    else:
        print('Produto não encontrado!')
        return False


def pegar_indice(produto):
    for i, produto_est in enumerate(estoque):
        if produto == produto_est:
            return i
    

def alterar_produto(produto_buscar, produto_alterar):
    if buscar_produto(produto_buscar):
        indice = pegar_indice(produto_buscar)
        estoque[indice] = produto_alterar
        print('Produto substituido!')
    else:
        print('Não é possível substituir!')


operacoes = {
            '1': inserir_produto,
            '2': ver_estoque,
            '3': buscar_produto,
            '4': alterar_produto
        }


def operacoes_sistema():
    print('''
        ########Bem-vindo#########
        Qual operação você deseja realizar ?
        1 - Inserir produto
        2 - ver o estoque
        3 - Buscar produto
        4 - Alterar produto
        0 - Para sistema

    ''')


def logica_sistema(operacao):
    
    if operacao in operacoes:
        if operacao == '1':
            operacoes[operacao](input('Digite o produto que deseja inserir: '))
        elif operacao == '3':
            operacoes[operacao](input('Digite o nome do produto que deseja buscar: '))
        elif operacao == '4':
            operacoes[operacao](input('Digite o produto a ser buscado: '), input('Digite o produto a ser inserido: '))
        elif operacao == '2':
            operacoes[operacao]()
        else:
            print('Operação Inválida')
            return True
    else:
        raise ValueError('Operação inválida')
               

def main():
    operacao =''
    while True:
        try:
            operacoes_sistema()
            operacao = input('Digite a operação a ser executada da operação: ')
            if logica_sistema(operacao):
                break
        except ValueError as e:
            print('Ocorreu um erro')
            print(' Erro: {}'.format(e))
        except Exception as e:
            print('Um erro inesperado ocorreu!')
            print('Erro: {}'.format(e))
        
        _ = input('Aperte enter para continuar')
        limpar_tela()
    limpar_tela()
    
    print('Obrigado por nos visitar')
        


if __name__ == '__main__':
    main()
