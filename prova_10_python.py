import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    
    nome_field = ft.TextField(label="Nome", width=400)
    email_field = ft.TextField(label="Email", width=400)
    mensagem_field = ft.TextField(label="Mensagem", multiline=True, min_lines=3, max_lines=5, width=400)

    confirmacao_text = ft.Text("", color="green")

    def enviar_formulario(e):
        if nome_field.value and email_field.value and mensagem_field.value:
            confirmacao_text.value = "✅ Formulário enviado com sucesso!"
        else:
            confirmacao_text.value = "❌ Por favor, preencha todos os campos."
        page.update()

    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    page.add(
        ft.Text("Entre em contato conosco:", size=20, weight="bold"),
        nome_field,
        email_field,
        mensagem_field,
        botao_enviar,
        confirmacao_text,
    )

ft.app(target=main)