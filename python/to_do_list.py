# 1. Iniciar com uma lista vazia
# Iniciar uma variavel != Atribuir valor
# nome = "Georgean"

tarefas = []

# 2. Perguntar quantas tarefas o usuário quer adicionar
qtd_tarefas = int(input("Quantas tarefas você quer adicionar hoje?"))

# 3. Para pedir cada tarefa será necessário a utilizacação de um loop
for i in range(qtd_tarefas):
    # Pedimos a tarefa e guardamos na variável 'nova_tarefa'
    nova_tarefa = input(f'Tarefa numero {i + 1}:') # A letra 'f' antes da string permite colocar variáveis dentro dela com {}

    # Adicionamos a nova tarefa à nossa lista
    tarefas.append(nova_tarefa)

# 4. Usar outro laço for para exibir a lista final
print("\n--- Suas tarefas para hoje são: ---")
for tarefa in tarefas:
    # print('Tarefa:',  tarefa)
    print(f"- {tarefa}")