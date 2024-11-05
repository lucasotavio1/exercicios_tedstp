A, B, C = map(float, input().split())
pi = 3.14159
areaTri = A * C/2
areaCir = pi * C ** 2
areaTrap = A + B * C/2
areaQua = B ** 2
areaRet = A * B
print("TRIANGULO: {:.3f}".format(areaTri))
print("CIRCULO: {:.3f}".format(areaCir))
print("TRAPEZIO: {:.3f}".format(areaTrap))
print("QUADRADO: {:.3f}".format(areaQua))
print("RETANGULO: {:.3f}".format(areaRet))
