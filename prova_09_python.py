import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    
    task_input = ft.TextField(label="Nova tarefa", width=300)
    
    tasks_list = ft.Column()
    
    def add_task(e):
        if task_input.value.strip() != "":
            tasks_list.controls.append(ft.Text(task_input.value.strip()))
            task_input.value = ""
            page.update()
    
    add_button = ft.Button(text="Adicionar", on_click=add_task)
    
    page.add(
        task_input,
        add_button,
        ft.Divider(),
        tasks_list
    )

ft.app(target=main)