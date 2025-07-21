produtos = {}

for i in range(5):
    nome = input(f'Insira o nome do produto {i+1}: ')
    preco = float(input(f'Insira o preço de {nome}: R$ '))
    produtos[nome] = preco

valor_total = sum(produtos.values())

print(f'\nResumo da compra:')
for nome, preco in produtos.items():
    print(f'{nome}: R$ {preco:.2f}')
    
print(f'\nO valor total da compra é: R$ {valor_total:.2f}')