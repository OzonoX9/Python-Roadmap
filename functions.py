def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Jin", "Refsnes")
my_function("Tobias", "Refsnes")

#Argumentos arbitrarios (*args)
def second_function(*kids):
    print("The youngest child is " + kids[2])
second_function("Emil", "Jin", "Tobias")

#Argumentos con Keywords
def third_function(child3, child2, child1):
    print("The youngest child is " + child3)
third_function(child1 = "Emil", child2 = "Jin", child3 = "Tobias")
    
#Argumentos con Keywords arbitrarios (**kwargs)
def fourth_function(**kid):
    print("His last name is " + kid["lname"])
fourth_function(fname = "Tobias", lname = "Refsnes")

#Argumentos con valores por defecto
def fifth_function(country = "Norway"):
    print("I am from " + country)
fifth_function("Sweden")
fifth_function("India")
fifth_function()
fifth_function("Brazil")

#Pasar una lista como argumento
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Retornar valores
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Declaracion Pass, si por alguna razón no se desea implementar la función, se puede usar la declaración pass
def myfunction():
    pass

#Argumentos solo posicionales, si se desea que la función no acepte argumentos con keywords, se puede declarar la función con solo argument
def my_function(x,/):
    print(x)
my_function(3) #Correcto
#my_function(x=3) #Incorrecto

#Argumentos solo con keywords, si se desea que la función solo acepte argumentos con keywords, se puede declarar la función con solo argumentos con keywords
def my_function(*, x):
    print(x)
my_function(x=3) #Correcto
#my_function(3) #Incorrecto

#Combinar argumentos posicionales y con keywords
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)
my_function(1, 2, c=3, d=4) #Correcto
#my_function(1, 2, 3, 4) #Incorrecto
#my_function(1, 2, 3, d=4) #Incorrecto
#my_function(1, 2, c=3, 4) #Incorrecto

#Recursividad, una función que se llama a sí misma
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(f"result: {result}")
    else:
        result = 0
    return result
tri_recursion(6)