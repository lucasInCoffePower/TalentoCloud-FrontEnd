def main():
  numero = 5
  print(numero)
  print(type(numero))

  
  bebidaTipo, bebidaValor, almocoTipo, almocoValor, sobremesaTipo, sobremesaValor ='vinho', 10, 'filé de peito', 20.00, 'creme de amendoin', 10.00
  orcamento = 200
  qtdConvidados = 4
  
  
  conta=(bebidaValor*3)+(almocoValor*4)+(sobremesaValor*2)
  rachaPessoa=conta/qtdConvidados
  
  print('Conta: R$ {}\nRachão: R$ {}'.format(conta, rachaPessoa)
  
  bomAmigo = True
  
  if orcamento >= rachaPessoa:
   print("Vamos dividir")
  elif bomAmigo:
    print('Top')
  else:
   print('Não')

  


if __name__ == '__main__':
  main()
