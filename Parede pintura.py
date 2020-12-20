larg = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))
area = larg*alt
tinta = area/2
print('A medida da parede é de: {}m2 x {}m2 \nE a área e de: {:.2f}'.format(larg, alt, area))
print('A quantidade de tinta é: {} Litros'.format(tinta))
