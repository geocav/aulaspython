# Seu Primeiro Mini-Projeto - Calculadora de IMC

# 1. Saudação inicial

# 2. Pedir os dados para o usuário

# 3. Calcular o IMC

# 4. Mostrar o resultado

# 5. Dar um feedback com base no resultado
import os
import time
print("salve, hoje vou fazer seu IMC e ver se tu vai viver muito")
print("Vou precisar de algumas informações suas, nome, peso e altura")
time.sleep(4)
os.system("clear")
nome = input("Seu nome: ")
time.sleep(2)
os.system("clear")
peso = float(input("quantos KG vc pesa: "))
time.sleep(2)
os.system("clear")
altura = float(input("qual é sua altura: "))
time.sleep(2)
os.system("clear")
imc = (peso)/(altura**2)
print("seu IMC é: ", imc)
time.sleep(4)
os.system("clear")

if(imc<16):
    print("vc está em estado de magreza grave")
    time.sleep(4)
    os.system("clear")
    print(nome,",BORA SE CUIDAR")
elif (imc>=16 and imc<17):
    print("vc está em estado de magreza moderada")
    time.sleep(4)
    os.system("clear")
    print(nome,",BORA SE CUIDAR")
elif (imc>=17 and imc<18.5):
    print("vc está em estado de magreza leve")
    time.sleep(4)
    os.system("clear")
    print(nome,",BORA SE CUIDAR")
elif (imc>=18.5 and imc<25):
    print("vc está em estado de saudável")
    time.sleep(4)
    os.system("clear")
    print(nome, ",PARABENS, CONTINUE ASSIM")
elif (imc>=25 and imc<30):
    print("vc está em estado de sobrepeso")
    time.sleep(4)
    os.system("clear")
    print(nome,",BORA SE CUIDAR")
elif (imc>=30 and imc<35):
    print("vc está em estado de obesidade grau I")
    time.sleep(4)
    os.system("clear")
    print(nome,",BORA SE CUIDAR")
elif (imc>=35 and imc<40):
    print("vc está em estado de obesidade grau II")
    time.sleep(4)
    os.system("clear")
    print(nome,",BORA SE CUIDAR")
else:
    print("vc está em estado de obesidade grau III")
    time.sleep(4)
    os.system("clear")
    print(nome,",BORA SE CUIDAR")

