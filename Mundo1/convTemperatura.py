celsius = float(input('Informe a temperatura em graus Celsius: '))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273
print('\n{}°C é igual a {}°F'.format(celsius,fahrenheit))
print('{}°C é igual a {}°K'.format(celsius,kelvin))