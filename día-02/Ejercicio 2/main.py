print('Cuantas semanas te quedan de vida?')
print('Ingresa tu edad')
age = int(input())
print('Ingresa tu edad en esperanza de vida')
dead = int(input())

weeks = (dead - age) * 52
print(f'Tu edad es {age}, y tu esperanza de vida es {dead}')
print(f"Te quedan {weeks} semanas de vida")