# for loops = ejecutan un bloque de codigo un numero de veces determinado
# se pueden iterar sobre un rango, una lista, una tupla, un diccionario, un conjunto o una cadena

for a in range(1,11): # una iteracion normal
    print(a)

for b in range(1,11,2): # una iteracion con saltos de 2
    print(b)
    
for c in reversed(range(1,11)): # una iteracion en reversa
    print(c)    
    
credit_card = '1234-5678-9012-3456'
for x in credit_card:
    print(x)

# saltar un elemento de la iteracion, si se quiere salir de la iteracion se usa break
for d in range(1,21):
    if d == 13:
        continue
    print(d)


#while loops = ejecutan un bloque de codigo mientras una condicion sea verdadera
name = input('Enter your name: ')

while name == '':
    name = input('Enter your name: ')
print(f'Hello, {name}!')

# se puede usar un while loop para validar la entrada de un usuario
age = int(input('Enter your age: '))

while age <0:
    print("Age can't be negative") 
    age = int(input('Enter your age: '))
print(f'You are {age} years old')

#ejemplo con comidas, cadena
food = input("Enter your favorite food (q to quit): )")
while not food.lower() == 'q':
    print(f'You entered {food}')
    food = input("Enter your favorite food (q to quit): )")
print('Goodbye!')

#ejemplo con operador logico OR
num = int(input('Enter a number between 1 and 10: '))
while num <1 or num >10:
    print('Invalid number!')
    num = int(input('Enter a number between 1 and 10: '))
print(f'You entered {num}')