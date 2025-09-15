# Nível 1: Aquecimento (Variáveis e print())
# O objetivo aqui é se familiarizar com a criação de variáveis e a exibição de mensagens na tela.

# Exercício 1: Apresentação Pessoal
# Crie variáveis para armazenar as seguintes informações:

# Seu nome (texto, string)
nome = "georgean"

# Sua idade (número inteiro, integer)
idade = 28
# Sua cidade (texto, string)
cidade = "teresina"
# Exemplo de saída: Olá, meu nome é João, tenho 25 anos e moro em Salvador.
print("Olá, meu nome é", nome, ", tenho", idade, "anos e moro em", cidade)
# Exercício 2: Calculadora Simples
# Crie duas variáveis, numero1 e numero2, e atribua um valor numérico a cada uma.
num1 = 10
num2 = 21
# Crie variáveis para armazenar os resultados das quatro operações matemáticas básicas: soma, subtracao, multiplicacao e divisao.
x = num1+num2
y = num1-num2
z = num1*num2
w = num1/num2

# Exemplo de saída:

# A soma de 10 e 5 é: 15
# A multiplicação de 10 e 5 é: 50
print("a soma de 10 + 21 = ", x)
print("a subtração de 10 + 21 = ", y)
print("a multiplicação de 10 + 21 = ", z)
print("a divisão de 10 + 11 = ", w)

# Nível 2: Tornando Interativo (input())
# Agora, vamos criar programas que conversam com o usuário, pedindo informações.
# Exercício 3: Eco Personalizado
# Pergunte o nome do usuário.
nome2 = input("qual teu nome? ")
# Pergunte qual a sua comida favorita.
comida = input("qual tua comida preferida?? ")
# Exiba uma mensagem personalizada usando as respostas.
print ("Olá,", nome2,"Eu vejo que sua comida favorita é", comida, ". Que delícia!")

# Exemplo de interação:

# Qual é o seu nome? Ana
# Qual é a sua comida favorita? Pizza
# Olá, Ana! Eu vejo que sua comida favorita é Pizza. Que delícia!
# Exercício 4: Conversor de Anos para Dias
# Pergunte ao usuário a idade dele em anos usando input().


# Calcule a idade do usuário em dias (considere que um ano tem 365 dias).
idade2 = int(input("qual tua idade: ")) 
# Exiba o resultado.
print("vc já viveu", idade2*365, "dia")
# Exemplo de interação:
# Quantos anos completos você tem? 30
# Você já viveu aproximadamente 10950 dias!

# Nível 3: Tomando Decisões (if, elif, else)
# Aqui o desafio é criar programas com lógica, que executam ações diferentes dependendo das condições.

# Exercício 5: Verificador de Aprovação
# Peça para o usuário digitar a nota de um aluno (de 0 a 10).
nota = float(input("digite sua nota de 0 a 10"))
# Converta a nota para um número (pode ser float() para aceitar notas como 7.5).

# Crie uma estrutura condicional:

# Se a nota for maior ou igual a 7.0, exiba "Aluno Aprovado!".
if nota >= 7:   
    print ("aluno aprovado")
elif nota < 7 and nota >= 5:
# elif nota >= 5:
    print("Aluno em Recuperação")  
else:
    print("Aluno Reprovado")

# Se a nota for menor que 7.0 mas maior ou igual a 5.0, exiba "Aluno em Recuperação.".

# Caso contrário (nota menor que 5.0), exiba "Aluno Reprovado.".

# Exercício 6: Par ou Ímpar?
# Peça ao usuário para digitar um número inteiro.
numimpar = int(input("digite um numero"))
# Use o operador de módulo % para descobrir se o número é par ou ímpar. O operador % retorna o resto de uma divisão. 
if numimpar%2 == 0:
    print ("numero par")
else:
    print ("numero impar")
# Exiba uma mensagem informando se o número é par ou ímpar.

# Exemplo de interação:

# Digite um número: 17
# O número 17 é ímpar.
# Desafio Final: Juntando Tudo
# Este exercício vai combinar todos os conceitos que vimos na aula: variáveis, input, conversão de tipo e condicionais.

# Exercício 7: Calculadora de Descontos
# Crie um programa para uma loja que calcula o preço final de um produto com desconto.

# Pergunte o preço original do produto.

# Pergunte o percentual de desconto (ex: 10 para 10%).

# Converta ambos os valores para números (float).

# Calcule o valor do desconto ( valor_desconto = preco_original * (percentual_desconto / 100) ).

# Calcule o preço final (preco_final = preco_original - valor_desconto).

# Exiba um resumo completo para o cliente.

# Bônus: Adicione uma condição. Se o preço final for maior que R$100,00, exiba uma mensagem adicional: "Parabéns! Sua compra tem frete grátis!".

# Exemplo de interação:

# Digite o preço original do produto: R$ 150.00
# Digite o percentual de desconto (%): 20

# --- Resumo da Compra ---
# Preço Original: R$ 150.0
# Desconto: R$ 30.0
# Preço Final: R$ 120.0
# Parabéns! Sua compra tem frete grátis!

valorTotal = float(input("preço da compra"))
valorDesconto = float(input("valor do desconto"))
precoFinal = valorTotal - (valorTotal * valorDesconto / 100)

print("Preço Original: ", valorTotal)
print("Descont: ", valorDesconto)
print("Preço Final: ", precoFinal)

if precoFinal >= 100 :
    print ("Parabéns! Sua compra tem frete grátis!")
