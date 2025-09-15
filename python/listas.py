#  Lidando com Coleções e Repetições

# Preciso guardar uma lista de compras
# Uma turma completa de Alunos
# Resultado de uma campanha de marketing

# Listas - É uma estrutura de dados
# Analogia: Uma caixa com varias divisorias. Onde é possivel guardar varios itens diferentes nela.
# Cada item vai ter uma posição.

# 1. Criando uma Lista
frutas = ["maçã", "banana", "laranja", "uva"]

numeros_sorteados = [5, 12, 23, 34, 45, 56]

dados_cliente = ["Carlos", 35, "carlos@email.com", True]

print(frutas)
print(dados_cliente)

# 2. Acessando Itens da Lista
# Cada item em uma lista tem uma posição, chamada de índice. 
# A contagem dos índices começa em 0.

primeira_fruta = frutas[0]
print("A primeira fruta é:", primeira_fruta) 

terceira_fruta = frutas[2]
print("A terceira fruta é:", terceira_fruta) 

# Dica Pro: Para pegar o último item, você pode usar o índice -1.
print(frutas[-1]) # Saída: uva

# 3. Modificando Listas
# Adicionar um item ao final: .append()
frutas.append("morango")
print(frutas)

# Remover um item pelo nome: .remove()
frutas.remove("laranja")
print(frutas)

# Ver o tamanho da lista: len()
print("Agora tenho", len(frutas), "frutas na lista.") 

# Laços de Repetição (for) 

# print(frutas[0])
# print(frutas[1])
# print(frutas[2])

# for -> Para cada item na minha lista, faça alguma coisa

print("---- Minha lista de compras ----")
for fruta in frutas:
    print("Comprar :", fruta)

print('---- Fim da minha lista ----')

# 2. Usando for com range() para Repetir N Vezes
# Usar o for tanto para percorrer listas quanto para 
# repetir ações um número fixo de vezes com range().
for numero in range(5):
    print("Esta é a repetição número:", numero)