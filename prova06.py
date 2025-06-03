# Credenciais corretas
usuario_correto = "admin"
senha_correta = "1234"

# Número máximo de tentativas
tentativas_max = 3

for tentativa in range(tentativas_max):
    # Solicita entrada do usuário
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verifica se as credenciais estão corretas
    if usuario == usuario_correto and senha == senha_correta:
        print("\n Bem-vindo, acesso concedido!")
        break
    else:
        restante = tentativas_max - tentativa - 1
        if restante > 0:
            print(f"\n Usuário ou senha incorretos. Tentativas restantes: {restante}\n")
        else:
            print("\n Usuário ou senha incorretos.\n")

# Caso as três tentativas falhem, mostra "Acesso bloqueado" três vezes
else:
    for _ in range(3):
        print("Acesso bloqueado")