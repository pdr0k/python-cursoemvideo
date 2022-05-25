import math

sen = float(input('Qual é o cateto oposto do triângulo? - '))
cos = float(input('Qual é o cateto adjacente do triângulo? - '))
hip = ((sen**2)+(cos**2)) **(1/2)

print(f'A hipotenusa é {hip}.')