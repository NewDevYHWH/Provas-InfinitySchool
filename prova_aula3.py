# [LPIA-A03] Você está criando um programa em Python para simular um jogo simples de adivinhação. 
# O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
# O jogador terá até 3 tentativas para acertar o número.
# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar 
# ou atingir o limite de tentativas.
# Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte
# e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.

print('Jogo da adivinhação: \nVocê terá três tentativas para acertar o número correto!')
numero_fixo = 7
tentativas = 3

while tentativas > 0:
    jogador = int(input('Digite o número: '))
    if jogador == numero_fixo:
        print('Parabéns, Você acertou o número!')
        break
    else:
        tentativas -= 1
    if tentativas > 0:
        print(f'Quase lá, você ainda tem {tentativas} tentativa(s).')
    else:
        print('Suas tentativas acabaram!')
else:
    print(f'Você perdeu! O número correto era {numero_fixo}.')