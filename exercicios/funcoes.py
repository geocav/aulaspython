# Exercício 1: Catálogo de Produtos (Dicionários)

# 1.  Crie um dicionário para representar um produto de um e-commerce. Ele deve conter as seguintes chaves: `codigo`, `nome`, `categoria`, `preco` e `em_estoque` (este último com um valor booleano `True` ou `False`).
# 2.  Imprima o nome e o preço do produto, acessando os valores através de suas chaves.
# 3.  Simule uma promoção: altere o valor da chave `preco`, aplicando um desconto de 10%.
# 4.  Verifique o valor da chave `em_estoque`. Se for `True`, imprima "Produto disponível para compra\!". Caso contrário, imprima "Produto esgotado.".
# produto = {
#     "codigo": "12345",
#     "nome": "camisa",
#     "categoria": "roupa", 
#     "preco": 100,
#     "em_estoque": False
#     }
# print(produto["preco"])
# print(produto["nome"])
# produto["preco"] = produto["preco"] * 0.9
# print(produto["preco"])

# if (produto["em_estoque"] == True ):
#     print("Produto disponível para compra\!")
# else:    
#     print("Produto esgotado.")
# Exercício 2: Jogo de Adivinhação (Laço `while`)

# 1.  Defina um número secreto (por exemplo, `numero_secreto = 42`).
# 2.  Crie um laço `while` que continuará rodando enquanto o palpite do usuário for diferente do número secreto.
# 3.  Dentro do laço, peça para o usuário digitar um palpite. Não se esqueça de converter o `input` para `int`.
# 4.  Adicione uma condição `if` dentro do laço: se o usuário acertar, exiba uma mensagem de parabéns e use o comando `break` para sair do laço.
# 5.  Se o usuário errar, o laço continuará naturalmente.
# numero_secreto = 42

# while numero_secreto :
#     chute = int(input("qual o numero que estou pensando ??"))
#     if chute == numero_secreto:
#      print("ACERTOU")
#      break
# Exercício 3: Conversor de Temperatura (Funções)

# 1.  Crie uma função chamada `celsius_para_fahrenheit` que recebe um parâmetro: `temperatura_celsius`.
# 2.  Dentro da função, aplique a fórmula de conversão: `F = (C * 9/5) + 32`.
# 3.  A função deve usar `return` para devolver o resultado em Fahrenheit.
# 4.  Fora da função, chame-a com um valor (ex: `30` graus Celsius) e imprima o resultado de forma clara.
# def celsius_para_fahrenheit (temperatura_celsius):
#     F = (temperatura_celsius * 9/5) + 32
#     print(F)
#     return
# celsius_para_fahrenheit (30)

# Exercício 4: Validação de Login (Função com Dicionário)

# 1.  Crie um dicionário chamado `usuarios` onde as chaves são nomes de usuário e os valores são as senhas. Ex: `{"admin": "1234", "joao": "senha123"}`.
# 2.  Crie uma função chamada `validar_login` que recebe dois parâmetros: `usuario` e `senha`.
# 3.  Dentro da função:
#       * Verifique se o `usuario` existe como uma chave no dicionário `usuarios`.
#       * Se existir, verifique se a `senha` fornecida é igual ao valor correspondente no dicionário.
#       * A função deve retornar `True` se o login for válido, e `False` caso contrário.
# 4.  Peça para o usuário digitar seu nome de usuário e senha, e use sua função para imprimir se o acesso foi "Permitido" ou "Negado".
# 1. Criando o dicionário de usuários
# usuarios = {
#     "admin": "1234",
#     "joao": "senha123"
# }

# def validar_login(usuario, senha):
#     if usuario in usuarios:
#         if usuarios[usuario] == senha:
#             return True
#         else:
#             return False
#     else:
#         return False

# while usuarios:
#     login = input("Digite seu login: ")
#     senha = input("Digite sua senha: ")


#     if validar_login(login, senha) == True:
#         print("Acesso Permitido")
#         break
#     else:
#         print("Acesso Negado")
    #     print("TENTE NOVAMENTE")  


# Exercício 5: Gerador de Contagem (Função com `while`)

# 1.  Crie uma função chamada `contagem_regressiva` que recebe um parâmetro: `inicio`.
# 2.  Dentro da função, use um laço `while` que imprima os números desde `inicio` até 1.
# 3.  A cada impressão, o número deve diminuir em 1.
# 4.  Após o laço, a função deve imprimir "Fogo\!".
# 5.  Peça ao usuário um número e chame sua função com esse número.
# def contagem_regressiva(inicio):
#     while inicio:
#         if inicio == 0:
#             print("FOGO")
#             break
#         else:
#             print(inicio)
#             inicio = inicio-1
#     print("FOGO")
# numero = int(input("digite a contagem"))
# contagem_regressiva(numero)



# Desafio Final: Agenda de Contatos

# Este desafio vai integrar tudo: Dicionários para guardar os contatos, um **laço `while`** para o menu principal e **Funções** para organizar cada ação (adicionar, ver, sair).

# Crie um programa que simule uma agenda de contatos.

# 1.  Estrutura Principal:

#       Crie um dicionário vazio chamado `agenda`.
#       Crie um laço `while True` para manter o menu rodando até o usuário decidir sair.

# 2.  Função `adicionar_contato(agenda, nome, telefone)`:

#       Esta função recebe o dicionário da agenda, o nome e o telefone do novo contato.
#       Ela adiciona o novo contato ao dicionário (`agenda[nome] = telefone`) e imprime uma mensagem de sucesso.

# 3.  Função `ver_contatos(agenda)`:

#     Recebe o dicionário da agenda.
#     Usa um laço `for` com `.items()` para percorrer o dicionário e imprimir todos os contatos de forma organizada (ex: `Nome: [nome], Telefone: [telefone]`).
#     Se a agenda estiver vazia, deve imprimir "A agenda está vazia.".

# 4.  Lógica do Menu (dentro do `while`):

#     Imprima as opções para o usuário: 1-Adicionar Contato, 2-Ver Contatos, 3-Sair.
#     Peça a escolha do usuário.
#     Se a escolha for '1', peça o nome e o telefone e chame a função `adicionar_contato`.
#     Se a escolha for '2', chame a função `ver_contatos`.
#     Se a escolha for '3', imprima "Até logo\!" e use `break` para encerrar o laço `while`.
#     Se a escolha for inválida, mostre uma mensagem de erro.
agenda = {}
def adicionar_contato(nome, telefone):
    agenda[nome] = telefone
    print("DEU CERTO")

def ver_contatos(agenda):
    for contato in agenda:
        print(agenda.items()) 

while True:
    print("1-Adicionar Contato")
    print("2-Ver Contatos")
    print("3-Sair")
    numero = input("o que deseja:")
    if numero == "1":
        nom = input("Qual seu nome??")
        tel = input("qual seu telefone??")
        adicionar_contato(nom,tel)
    if numero == "2":
        ver_contatos(agenda)
    if numero == "3":
        break