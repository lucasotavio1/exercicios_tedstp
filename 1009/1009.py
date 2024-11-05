nome = input()
salarioFixo = float(input())
totalVendas = float(input())
TOTAL = salarioFixo + totalVendas * 0.15
print("TOTAL = R$ {:.2f}".format(TOTAL))
