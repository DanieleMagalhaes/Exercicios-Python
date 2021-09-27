metro = float(input('Digite uma distancia em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print('A distancia de {} metros corresponde a: '.format(metro))
print('{} Quilômetros'.format(km))
print('{} Hectômetros'.format(hm))
print('{} Decâmetros'.format(dam))
print('{:.0f} Decímetros'.format(dm))
print('{:.0f} Centímetros'.format(cm))
print('{:.0f} Milímetros'.format(mm))


