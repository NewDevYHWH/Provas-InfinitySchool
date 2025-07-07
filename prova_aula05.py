# [LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina.
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. 
# Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, 
# considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.
# Ao final, exiba a média geral da turma.

alunos = int(input('Quantos alunos são na turma? '))

media_total = 0
alunos_aprovados = 0

for i in range (alunos):
    nome = input(f'Qual nome do {i+1}º aluno: ')
    
    nota1 = float(input(f'Qual a primeira nota do aluno(a) {nome}: '))
    nota2 = float(input(f'Qual a segunda nota do aluno(a) {nome}: '))
    nota3 = float(input(f'Qual a terceira nota do aluno(a) {nome}: '))
    
    media = (nota1 + nota2 + nota3) / 3
    
    print(f'Aluno: {nome}')
    print(f'Notas: {nota1}, {nota2}, {nota3}')
    print(f'Média: {media}')
   
   
    if media >= 7.0:
        print('Aprovado!')
        alunos_aprovados += 1
    else:
        print('Reprovado!')
        
    media_total += media
    
media_geral = media_total / alunos
print(f'Média geral da turma foi: {media_geral}')
print(f'Total de alunos que foram aprovados: {alunos_aprovados}')
