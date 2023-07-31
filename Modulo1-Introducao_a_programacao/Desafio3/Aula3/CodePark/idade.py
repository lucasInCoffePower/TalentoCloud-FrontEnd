

from datetime import datetime  # biblioteca para manipular datas 
import os


def limparTela():
    if os.name == 'nt':
        # limpar cli Windows
        os.system('cls')
    else:
        # limpar cli MacOs e Linux
        os.system('clear')


def receberAnoNascimento():
    try:
        ano_nascimento = int(input('Digite o ano em que você nasceu: '))
        if ano_nascimento < 1922 or ano_nascimento > 2021:
            raise Exception('Data inválida ! Intervalo de data menor que 1922 ou maior que 2021 são inválidos!') 
    except ValueError as ve:
        raise ValueError('Digitou texto ao invés de número !')
    else:
        return ano_nascimento


def receberNome():
    nome = input('Digite o seu nome: ')
    return nome


def calcularIdade(ano_nascimento:int):
    '''Calcula a idade no ano atual'''
    ano_atual = datetime.today().year
    idade = ano_atual-ano_nascimento
    return idade, ano_atual


def main():
    
    nome = receberNome()
    while True:
        try:
            ano_nascimento = receberAnoNascimento()
            idade, ano_atual = calcularIdade(ano_nascimento)
        except ValueError as ve:
            print('Um erro ocorreu!')
            print('Erro: {}'.format(ve))
        except Exception as e:
            print('Um erro ocorreu')
            print('Erro: {}'.format(e))
        else:
            print(f'Olá, {nome} ! Em {ano_atual} você completa {idade} anos de idade')
            break
        input('Digite a data de nascimento novamente! Pressione enter para continuar!')
        limparTela()
        


if __name__ == '__main__':
    main()
