import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

tarefas = []
desfeitas = []

while True:
    decisao = input('Digite uma tarefa ou comando (listar, desfazer, refazer, clear, sair): ').strip()

    comando = decisao.lower()

    if comando == 'listar':
        if not tarefas:
            print('Nenhuma tarefa cadastrada.')
        else:
            print('\n'.join(f'{i}: {tarefa}' for i, tarefa in enumerate(tarefas, 1)))

    elif comando == 'desfazer':
        if not tarefas:
            print('Não há nada para desfazer.')
        else:
            tarefa = tarefas.pop()
            desfeitas.append(tarefa)
            print(f'Tarefa "{tarefa}" desfeita.')

    elif comando == 'refazer':
        if not desfeitas:
            print('Não há nada para refazer.')
        else:
            tarefa = desfeitas.pop()
            tarefas.append(tarefa)
            print(f'Tarefa "{tarefa}" refeita.')

    elif comando == 'clear':
        clear()

    elif comando == 'sair':
        print('Saindo do programa...')
        break

    else:
        tarefas.append(decisao)
        desfeitas.clear()
        print(f'Tarefa "{decisao}" adicionada.')
