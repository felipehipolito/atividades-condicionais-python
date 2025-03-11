
import os

#LIMPANDO A TELA
os.system("cls")

#1 PASSO ENTRADA DE DADOS

print(''' 
██████╗░░█████╗░░██████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░
██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗
██████╔╝███████║██║░░██╗░███████║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║
██╔═══╝░██╔══██║██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║
██║░░░░░██║░░██║╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░ \n''')

print("Insira o nível do professor: ")
nivel = int(input())

if nivel == 1:
    print("Professor nível 1")

elif nivel == 2:
    print("Professor nível 2")

elif nivel == 3:
    print("Professor nível 3")

print("Insira a quantidade de aulas: ")
aulas = int(input())

salario = aulas * 12.00

print("O professor recebe: ", salario)

