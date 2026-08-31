from math import cos, sin, tan, radians
a = float(input('Digite um ângulo: '))
ar = radians(a)
s = sin(ar)
c = cos(ar)
t = tan(ar)

print(f'O ângulo {a}º tem:\n'
      f'Seno {s:.4f},\n'
      f'Cosseno {c:.4f}\n'
      f'Tangente {t:.4f}.')