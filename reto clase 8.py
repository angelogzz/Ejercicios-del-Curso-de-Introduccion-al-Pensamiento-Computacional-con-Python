user_1 = (input('Introduce el nombre del primer usuario: '))
ageuser_1 = int(input('Cual es su edad? '))
user_2 = (input('Introduce el nombre del segundo usuario: '))
ageuser_2 = int(input('Cual es su edad? '))

if ageuser_1 > ageuser_2:
    print(f'{user_1} es mayor que {user_2}')
elif ageuser_2 > ageuser_1:
    print(f'{user_2} es mayor que {user_1}')
else:
    print('Ambos tienen la misma edad')