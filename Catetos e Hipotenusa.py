#co = float(input('Cumprimento do cateto oposto: '))
#ca = float(input('cumprimento do cateto adjacente: '))
#hip = (co ** 2 + ca ** 2) ** (1/2)
#print('O cumprimento da hipotenusa é: {:.2f} '.format(hip))

#import math
#co = float(input('Cumprimento do cateto oposto: '))
#ca = float(input('Cumprimento do cateto adjacente: '))
#hip = math.hypot(ca, co)
#print('O cumprimento da hipotenusa é {:.2f} '.format(hip))

from math import hypot
co = float(input('Cumprimento do caeto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('O cumprimento da hipotenusa é: {:.3f} '.format(hip))