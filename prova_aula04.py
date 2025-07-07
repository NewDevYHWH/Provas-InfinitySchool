# [LPIA-A04] Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. 
# O programa deve solicitar ao usuário que insira dois números inteiros,
# representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares.
# Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.
# Ao final, exiba a soma dos números pares encontrados.


inicio_intervalo = int(input('Digite qualquer número inteiro: '))
fim_intervalo = int(input('Digite outro número inteiro: '))

soma = 0

for n in range(inicio_intervalo, fim_intervalo +1):
     if n % 2 == 0:
         soma += n

if soma > 0:
     print(f'a soma dos números pares {inicio_intervalo} e {fim_intervalo} é: {soma}')
else:
     print(f'Não foram digitados números pares.')
