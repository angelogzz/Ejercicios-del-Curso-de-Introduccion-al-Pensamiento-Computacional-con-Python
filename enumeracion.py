objetivo = int(input('Introduce un número entero:'))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
else:
    print(f' {objetivo} no tiene una raíz cuadrada exacta')