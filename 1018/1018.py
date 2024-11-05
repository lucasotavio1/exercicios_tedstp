N = int(input())
valorInicial = N
notas100 = N//100
N %= 100
notas50 = N//50
N %= 50 
notas20 = N//20
N %= 20
notas10 = N//10
N %= 10
notas5 = N//5
N %= 5
notas2 = N//2
N %= 2
notas1 = N//1
N %= 1
print(valorInicial)
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")
