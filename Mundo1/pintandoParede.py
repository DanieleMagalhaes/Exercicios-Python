base = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = base * altura
print('Sua parede tem a dimensão de {:.2f}X{:.2f} e a sua área é de {:.2f}m².'. format(base,altura,area))
print('Para pintar essa parece, você precisará de {:.2f} litros de tinta.' .format(area/2))