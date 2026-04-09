#1. Agregar y eliminar elementos de una lista

fruits = ["Orange","Apple","Lemon","Banana","Grape"]
fruits.append("Papaya")
fruits.insert(2,"Mango")
fruits.remove("Orange")
fruits.pop()

print(fruits)


#2. Ordenar y contar elementos en una lista

numbers = [4,2,7,2,9,1,2]
numbers.sort()
numbers.reverse()
number_2A = numbers.count(2)
pos_7 = numbers.index(7)

print(number_2A)
print(numbers)
print(pos_7)


#3. Copiar y extender listas

a = [1, 2, 3]
b = [4, 5, 6]


c = a.copy()

print (c)





