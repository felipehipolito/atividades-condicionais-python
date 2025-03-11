
import os

os.system("cls")

print("Selecione o produto: ")
produto = input()

print("Digite a quantidade desejada: ")
quantidade = float(input())

print("Digite o valor unitário: ")
valor_unitario = float(input())

if quantidade <= 5:
    desconto = 0.2
elif quantidade > 5 and quantidade <= 10 :   
    desconto = 0.3
elif quantidade > 10:
    desconto = 0.5
else:
    desconto = 0

valor_total = quantidade * valor_unitario
valor_desconto = valor_total - (valor_total * desconto)

print("Produto: ", produto)
print("Quantidade: ", quantidade)
print("Valor unitário: ", valor_unitario)
print("Desconto: ", desconto)
print("Valor total: ", valor_total)
print("Valor com desconto: ", valor_desconto)

