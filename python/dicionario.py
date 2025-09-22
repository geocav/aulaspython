#  Um dicionário é como um fichário onde cada ficha tem uma etiqueta (uma "chave"). 
# Você não precisa saber o número da gaveta, apenas o nome da etiqueta para encontrar a informação.

# Rótulo (Chave): "nome" -> Dado (Valor): "Ana Silva"

# Rótulo (Chave): "idade" -> Dado (Valor): 28

# Rótulo (Chave): "cidade" -> Dado (Valor): "Belo Horizonte"


# 1. Por que usar Dicionários?
# Eles são perfeitos para armazenar informações que têm uma relação clara de "rótulo" e "dado". Por exemplo, os dados de um cliente:


# 2. Criando um Dicionário
# Criando um dicionário para representar um aluno
# {} - chaves
# [] - colchetes
# "" - aspas duplas
# '' - aspas simples
# `` - crase

aluno = {
    "nome": "Lucas Souza",
    "idade": 21,
    "curso": "Engenharia de Software",
    "matricula_ativa": True
}



print(aluno)
# frutas = ["maçã", "banana", "laranja", "uva"]
# print(frutas[0]) -> [0] na posição, sendo que o 0 é o indice da pesquisa

# Quando falamos em objetos e dicionarios, o acesso não é mais por indice numerico e sim pela chave que é o rótulo.
# 3. Acessando e Modificando Dados
print("O nome do aluno é:", aluno["nome"])

# Alterando o curso do aluno
aluno["curso"] = "Ciência da Computação"
print("O novo curso é:", aluno["curso"])

# Adicionando uma nova informação (chave-valor)
aluno["semestre"] = 5
print("O aluno agora tem a informação de semestre:", aluno)

# 4. Percorrendo um Dicionário com for
print("\n--- Ficha do Aluno ---")
for chave, valor in aluno.items():
    # capitalize deixa a primeira letra de cada palavra maiuscula
    print(f"{chave.capitalize()}: {valor}")