# Exercício 1: Catálogo de Produtos (Dicionários)

# 1.  Crie um dicionário para representar um produto de um e-commerce. 
# Ele deve conter as seguintes chaves: `codigo`, `nome`, `categoria`, `preco` e `em_estoque` 
# (este último com um valor booleano `True` ou `False`).
# 2.  Imprima o nome e o preço do produto, acessando os valores através de suas chaves.
# 3.  Simule uma promoção: altere o valor da chave `preco`, aplicando um desconto de 10%.
# 4.  Verifique o valor da chave `em_estoque`. Se for `True`, imprima "Produto disponível para compra\!". Caso contrário, imprima "Produto esgotado.".
produto = {
    "codigo": "12345",
    "nome": "camisa",
    "categoria": "roupa", 
    "preco": 100,
    "em_estoque": False
    }
print(produto["preco"])
print(produto["nome"])
produto["preco"] = produto["preco"] * 0.9
# É a forma mais curta e comum para aplicar operação na propria variavel
# produto["preco"] *= 0.9
print(produto["preco"])

# Como o valor esperado já é True ou false, elimina a redundancia.
# if (produto["em_estoque"]):
if (produto["em_estoque"] == True ):
    print("Produto disponível para compra\!")
else:    
    print("Produto esgotado.")

# Exercício 2: Jogo de Adivinhação (Laço `while`)

# 1.  Defina um número secreto (por exemplo, `numero_secreto = 42`).
# 2.  Crie um laço `while` que continuará rodando enquanto o palpite do usuário for diferente do número secreto.
# 3.  Dentro do laço, peça para o usuário digitar um palpite. Não se esqueça de converter o `input` para `int`.
# 4.  Adicione uma condição `if` dentro do laço: se o usuário acertar, exiba uma mensagem de parabéns e use o comando `break` para sair do laço.
# 5.  Se o usuário errar, o laço continuará naturalmente.

numero_secreto = 42

while numero_secreto :
    chute = int(input("qual o numero que estou pensando ??"))
    if chute == numero_secreto:
     print("ACERTOU")
     break

#while True, cria um laço infinito
while True :
    chute = int(input("qual o numero que estou pensando ??"))
    if chute == numero_secreto:
        print("ACERTOU")
        break
    else:
        print("Errado, tente novamente!!")
# Exercício 3: Conversor de Temperatura (Funções)

# 1.  Crie uma função chamada `celsius_para_fahrenheit` que recebe um parâmetro: `temperatura_celsius`.
# 2.  Dentro da função, aplique a fórmula de conversão: `F = (C * 9/5) + 32`.
# 3.  A função deve usar `return` para devolver o resultado em Fahrenheit.
# 4.  Fora da função, chame-a com um valor (ex: `30` graus Celsius) e imprima o resultado de forma clara.

#Exerça uma atividade, sabendo só o necessário para ela funcionar e faça uma unica coisa
def celsius_para_fahrenheit (temperatura_celsius):
    return (temperatura_celsius * 9/5) + 32

print(celsius_para_fahrenheit(30))

# Exercício 4: Validação de Login (Função com Dicionário)

# 1.  Crie um dicionário chamado `usuarios` onde as chaves são nomes de usuário e os valores são as senhas. Ex: `{"admin": "1234", "joao": "senha123"}`.
# 2.  Crie uma função chamada `validar_login` que recebe dois parâmetros: `usuario` e `senha`.
# 3.  Dentro da função:
#       * Verifique se o `usuario` existe como uma chave no dicionário `usuarios`.
#       * Se existir, verifique se a `senha` fornecida é igual ao valor correspondente no dicionário.
#       * A função deve retornar `True` se o login for válido, e `False` caso contrário.
# 4.  Peça para o usuário digitar seu nome de usuário e senha, e use sua função para imprimir se o acesso foi "Permitido" ou "Negado".
# 1. Criando o dicionário de usuários
usuarios = {
    "admin": "1234",
    "joao": "senha123"
}

def validar_login(usuario, senha):
    if usuario in usuarios:
        if usuarios[usuario] == senha:
            return True
        else:
            return False
    else:
        return False
    
# def validar_login(usuario, senha):
    # verdadeiro (e/and) verdadeiro = verdadeiro
    # verdadeiro (e/and) false = falso
    # verdadeiro (ou/or) verdadeiro = verdadeiro
    # verdadeiro (ou/or) false = verdadeiro
    # false (ou/or) false = false
    # return usuario in usuarios and usuarios[usuario] == senha


while usuarios:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")


    if validar_login(login, senha) == True:
        print("Acesso Permitido")
        break
    else:
        print("Acesso Negado")
        print("TENTE NOVAMENTE")  


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


def contagem_regressiva(inicio):
    while inicio > 0:
        print(inicio)
        inicio -= 1 #ou inicio = inicio-1

    print("FOGO")
numero = int(input("digite a contagem"))
contagem_regressiva(numero)



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

agenda = {'eva': '1234'}

# def adicionar_contato(, nome, telefone): dependencia oculta
# def adicionar_contato(agenda, nome, telefone): contrato fica mais claro
def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    print(f"Contato '{nome}' adicionado com sucesso!")

def ver_contatos(agenda):
    print("\n--- Sua Agenda de Contatos ---")
    if not agenda:
        print("A agenda está vazia.")
        return

    for nome, telefone in agenda.items():
        print(f"Nome: {nome} | Telefone: {telefone}")

while True:
    print("1-Adicionar Contato")
    print("2-Ver Contatos")
    print("3-Sair")
    numero = input("o que deseja:")
    if numero == "1":
        nom = input("Qual seu nome??")
        tel = input("qual seu telefone??")
        adicionar_contato(agenda, nom,tel)
    elif numero == "2":
        ver_contatos(agenda)
    elif numero == "3":
        break
    else:
        print("Opção invalida")




# ========================================== A FAZER

# Jogo de Adivinhação (Laço `while`) -   Variação

# Informe ao usuario se o valor que ele forneceu é maior ou menor ao valor esperado.
numero_secreto = 42

while True :
    chute = int(input("qual o numero que estou pensando ??"))
    if chute == numero_secreto:
     print("ACERTOU")
     break

# ======================================================
# Nível Intermediário: Caixa Registradora de Lanchonete
# Objetivo: Criar um sistema de linha de comando que permita a um atendente registrar os itens de um pedido e calcular o total da conta.

# Requisitos:

# O programa deve ter um cardápio predefinido com nomes de produtos e seus respectivos preços.

# O sistema deve permitir que o usuário adicione múltiplos itens ao pedido, um de cada vez.

# O programa deve validar se o item inserido pelo usuário existe no cardápio. Itens inválidos não devem ser adicionados ao pedido.

# Deve haver uma forma de o usuário sinalizar que terminou de adicionar itens.

# Ao final, o programa deve exibir um resumo de todos os itens do pedido e o valor total a ser pago.

# ======================================================

# Nível Avançado: Sistema de Votação Simples
# Objetivo: Desenvolver um programa que simule uma urna eletrônica, registrando votos para candidatos predefinidos e apurando o resultado final.

# Requisitos:

# O programa deve iniciar com uma lista de candidatos, todos com zero votos.

# O sistema deve permitir que múltiplos votos sejam registrados sequencialmente.

# O programa deve rejeitar votos para candidatos que não existam na lista oficial.

# O usuário deve ter uma maneira de encerrar o processo de votação.

# Após o encerramento, o programa deve exibir a contagem de votos de cada candidato e declarar 
# quem foi o vencedor (o candidato com o maior número de votos).

# =============================================================

# Nível Desafio: Mini Jogo RPG - Batalha em Turnos
# Objetivo: Construir um jogo de batalha baseado em turnos, onde um herói controlado pelo jogador luta contra um monstro controlado pelo computador até que um deles seja derrotado.

# Requisitos:

# O herói e o monstro devem ser representados por estruturas de dados que contenham seus atributos: no mínimo, nome, vida, ataque e defesa.

# A batalha deve ocorrer em turnos. Em cada rodada, o herói ataca primeiro, seguido pelo ataque do monstro (se ele ainda estiver vivo).

# O dano de um ataque deve ser calculado com base nos atributos de ataque do atacante e de defesa do defensor. A lógica para este cálculo fica a seu critério.

# A cada turno, o status atual (pelo menos a vida) de ambos os personagens deve ser exibido ao jogador.

# O jogo termina quando a vida de um dos personagens chegar a 0 ou menos.

# Ao final da batalha, uma mensagem declarando o vencedor (Herói ou Monstro) deve ser exibida.