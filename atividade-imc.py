
import os

#LIMPANDO A TELA
os.system("cls")

print('''
█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█   █ █▀▄▀█ █▀▀
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█   █ █░▀░█ █▄▄ \n ''')

#1 PASSO ENTRADA DE DADOS
print("Digite o seu peso: ")
peso = float(input())

print("Digite a sua altura: ")
altura = float(input())

#2 PASSO PROCESSAMENTO
imc = peso / (altura * altura)

#3 PASSO SAIDA DE DADOS
print("Seu IMC é: ", imc)

if imc < 17:
    print("Muito abaixo do peso")
elif imc > 17 and imc <= 18.4:
    print("Abaixo do peso")
elif imc > 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc > 25 and imc <= 29.9:
    print("Acima do peso")
elif imc > 30 and imc <= 34.9:
    print("Obesidade I")
elif imc > 35 and imc <= 39.9:
    print("Obesidade II")
elif imc > 40:
    print("Obesidade III")