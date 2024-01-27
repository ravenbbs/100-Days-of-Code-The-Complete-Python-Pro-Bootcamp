print('Ingresa Tu Peso (kg): ')
weight = float(input())
print('Ingresa Tu ALtura (m): ')
height = float(input())

bmi = weight / (height * height)

print('Tu Indice de masa corporal es: ' + str(round(bmi)))