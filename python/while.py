# O Laço while (Repetição Baseada em Condição)
# O laço while repete um bloco de código enquanto uma condição for verdadeira. 

# A Estrutura do while
# Um laço while típico tem 3 partes:

# Inicialização: Uma variável que controla a condição é criada antes do laço.

# Condição: A verificação que é feita no início de cada repetição.

# Atualização: Uma mudança na variável de controle dentro do laço para que ele eventualmente termine.

# Exemplo: Contagem regressiva
contador = 5

while contador > 0:
    print(contador)
    contador = contador - 1

print("Decolar!")

opcao = ""

while opcao != "3":
    print("\n--- MENU ---")
    print("1: Ver Notícias")
    print("2: Ver Previsão do Tempo")
    print("3: Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Hoje não há notícias importantes.")
    elif opcao == "2":
        print("Previsão de sol para Barbacena/MG.")
    elif opcao == "3":
        print("Saindo do programa...")
    else:
        print("Opção inválida!")