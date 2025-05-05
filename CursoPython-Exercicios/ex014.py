# EXC 14 - Escreva um programa que converta uma temperatura digitada em °C para °F (adicional: faça também para °K)

# 1- De Celsius para Fahrenheit
tempC = float(input('Digite a temperatura atual do seu local em °C: '))
tempF = (tempC * 1.8) + 32

# 2- De Celsius para Kevin
tempK = tempC + 273.15 # Valor de Graus Kevin é pré definido para 273.15

# 3- De Fahrenheit para Celsius
tempF2 = float(input('Digite qual a sua temperatura local em °F: '))
tempC2 = (tempF2 - 32) * 5/9

# Exibição dos Resultados
print('1- Valor em Celsius: {:.1f}°C convertido em Fahrenheit: {:.1f}°F'.format(tempC,tempF))
print('2- Valor em Celsius: {:.1f}°C convertido em Kevin: {:.1f}°K'.format(tempC, tempK))
print('3- Valor em Fahrenheit: {:.1f}°F convertido em Celsius: {:.1f}'.format(tempF2, tempC2))
