print('='*44)
print('-_-_-_-_-_-_-_-_-_ ANGULO -_-_-_-_-_-_-_-_-_')
print('_'*44)
from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print('O anglo de {} - tem o seno de {:.2f} '.format(angulo, seno))
cos = cos(radians(angulo))
print('O angulo de {} - tem o cosseno de: {:.2f} '.format(angulo, cos))
tang = tan(radians(angulo))
print('O angulo de {} - tem a tangente de: {:.2f} '.format(angulo, tang))

print('='*44)
