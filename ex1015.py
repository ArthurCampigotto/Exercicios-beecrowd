import math

entrada1 = input().split()
x1,y1 = entrada1
entrada2 = input().split()
x2,y2 = entrada2

resultado = math.sqrt((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2)
print('{:.4f}'.format(resultado))