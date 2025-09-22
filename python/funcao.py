# Funções (Organizando e Reutilizando Código)

#  funções permitem que você "empacote" um bloco de código, dê um nome a ele e o chame sempre que precisar.

# definição da funcao
# def para especificar que vai ser declarada uma função
# exibir_saudacao é o nome da função
# () -> dentro do parenteses ficam os argumentos/atributos/parametros quando necessários
def exibir_saudacao():
    print("Olá! Seja bem-vindo(a) ao sistema.")

#usar a funcao
exibir_saudacao()

# Parâmetros e Retorno
# Funções ficam realmente poderosas quando podem receber dados (parâmetros) e devolver um resultado (return).

# Esta função recebe dois números como parâmetros
def somar(a, b):
    resultado = a + b
    return resultado # A função 'devolve' este valor

# Chamando a função e guardando o resultado
soma_dos_numeros = somar(10, 5)
print("O resultado da soma é:", soma_dos_numeros)

outra_soma = somar(100, 200)
print("O resultado da outra soma é:", outra_soma)