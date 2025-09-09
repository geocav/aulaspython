print("Olá, Mundo!") # para escrever no terminal

print(10 + 5)

# 2. Variáveis: As "Caixas" para Guardar Informações
# Pense nelas como etiquetas para potes: você sabe o que tem dentro olhando a etiqueta.

# String (texto)
nome = "Maria"

# Integer (número inteiro)
idade = 30

# Float (número com casas decimais)
altura = 1.75

# Boolean (Verdadeiro ou Falso)
e_maior_de_idade = True

# Agora, vamos usar as variáveis
print("Nome da usuária:", nome)
print("Idade:", idade)

# 3. input() - Conversando com seu Programa
# Para conseguir obter informações do usuario

nome_usuario = input("Qual é o seu nome? ")
print("Olá, " + nome_usuario + "! Seja bem-vindo(a)!")

# 4. Condicionais: if, elif e else
# As estruturas condicionais permitem que seu programa tome caminhos diferentes dependendo da situação.

# int() converte o texto digitado para número
idade = int(input("Qual a usa idade?"))

# if (idade >= 18):
#     print("Maior de idade")
# else:
#     print("Menor de idade")

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é um adulto.")
else:
    print("Você está na melhor idade!")

# if (Se): O programa verifica a primeira condição. Se for verdadeira, ele executa o código dentro dela e ignora o resto.

# elif (Senão, se): Se o if for falso, ele testa esta segunda condição.

# else (Senão): Se nenhuma das condições anteriores for verdadeira, ele executa o código do else