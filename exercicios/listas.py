

#  Nível 1: Dominando as Listas

# O foco aqui é criar, acessar e modificar listas.

# Exercício 1: Minha Playlist

# 1.  Crie uma lista chamada `playlist` com o nome de 3 das suas músicas favoritas.
# 2.  Exibir a lista completa.
# 3.  Adicionar uma nova música à sua playlist.
# 4.  Retire a primeira música que você havia adicionado.
# 5.  Mostre a playlist atualizada e diga quantas músicas ela tem.


# Exercício 2: Acesso Secreto

# 1.  Crie uma lista chamada `convidados` com o nome de 5 pessoas.
# 2.  Exiba uma mensagem de boas-vindas para a primeira pessoa da lista.
# 3.  Exiba uma mensagem especial para a última pessoa da lista.

#  Nível 2: O Poder do `for`

# Vamos praticar a automação de tarefas com o laço de repetição.

# Exercício 3: Tabuada Interativa

# 1.  Peça ao usuário para digitar um número inteiro.
# 2.  Use um laço `for` com a função.
# 3.  Dentro do laço, calcule e imprima a tabuada do número digitado pelo usuário.
     

# Exercício 4: Nomes na Vertical

# 1.  Crie uma lista de `nomes` com pelo menos 4 nomes.
# 2.  Use um laço `for` para percorrer a lista.
# 3.  Dentro do laço, imprima cada nome com uma mensagem, um por linha.
     

#  Nível 3: Combinando Tudo

# Aqui, vamos misturar listas, laços e as condicionais (`if`/`else`) da primeira aula.

# Exercício 5: Média da Turma

# 1.  Crie uma lista vazia chamada `notas`.
# 2.  Use um laço `for` para pedir ao usuário que digite 4 notas (de 0 a 10). A cada nota digitada, adicione-a à lista `notas`.
# 3.  Crie uma variável `soma_das_notas` iniciada com o valor `0`.
# 4.  Use um segundo laço `for` para percorrer a lista `notas`. Dentro deste laço, some cada nota à variável `soma_das_notas`.
# 5.  Fora do laço, calcule a `media` (`soma_das_notas / len(notas)`).
# 6.  Exiba a média final. Se a média for maior ou igual a 7, dê os parabéns\! Caso contrário, diga para o aluno se esforçar mais.

# Exercício 6: Filtrando Números Positivos

# 1.  Crie uma lista chamada `numeros` que contenha números positivos e negativos. Ex: `[10, -5, 8, -12, 3, -20]`.
# 2.  Crie uma lista vazia chamada `positivos`.
# 3.  Use um laço `for` para percorrer a lista `numeros`.
# 4.  Dentro do laço, use um `if` para verificar se o número da vez é maior ou igual a zero.
# 5.  Se for, adicione-o à lista `positivos`.
# 6.  No final, fora do laço, imprima a lista `positivos`.

#  Desafio Final: Pequeno Sistema de Supermercado

# Este desafio vai exigir que você use quase tudo o que aprendeu até agora.

# 1.  Crie uma lista vazia chamada `carrinho_de_compras`.
# 2.  Crie uma lista chamada `produtos_disponiveis` com alguns itens. Ex: `["arroz", "feijão", "óleo", "sal", "açúcar"]`.
# 3.  Use um laço `for` para dar ao usuário 3 chances de adicionar um produto ao carrinho.
# 4.  Dentro do laço:
#        Mostre a lista de produtos disponíveis para o usuário.
#        Peça para ele digitar o nome de um produto que deseja comprar.
#        Use um `if` para verificar se o produto digitado está na lista `produtos_disponiveis`.
#        Se o produto existir, adicione-o ao `carrinho_de_compras` e informe ao usuário.
#        Se não existir, avise que o produto não está disponível.
# 5.  No final do programa, exiba todos os itens que o usuário adicionou ao `carrinho_de_compras`.
