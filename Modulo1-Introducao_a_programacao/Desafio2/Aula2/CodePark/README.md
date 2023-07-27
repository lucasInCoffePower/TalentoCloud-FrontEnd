# Code Park

## Questão
*Cada exercício da tabela em anexo tem declaração de variáveis e, na sequência, uma sentença que usa as variáveis e operadores lógicos. Determine qual é o 
resultado final (Verdadeiro ou Falso) de cada sentença.*  

![Imagem da tabela](https://github.com/lucasInCoffePower/TalentoCloud-FrontEnd/blob/main/Modulo1-Introducao_a_programacao/Desafio2/Aula2/CodePark/Tabela_PeerTutoring01_IntroducaoProgramacao.png)


## Resposta

**O resultado final é mostrado na tabela abaixo**

| Linhas   | Variáveis | Sentença   | Resultado |
|----------|---------- | --------   | --------- |
| Linha 1  | nota = 10 | nota <= 10 |    True   |
| Linha 2  | nota, faltas = 6, 4  | nota <=6  and faltas<=3| False |    
| Linha 3  | convidados, fumante = 3, False | convidados > 4 or fumante == True | False |
| Linha 4  | dia = "qua" | dia == "sab" or dia == "dom" | False |
| Linha 5  | feriado = True | not feriado == False | True |
| Linha 6  | dia, feriado = "ter", False | dia == "seg" or !(feriado == False) | False (obs: No python dá erro de sintaxe: a função do operador `!` é feito pelo `not`, então ele não existe)  |
