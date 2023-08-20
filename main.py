# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 1, 2, 5
# Вывод: 1, 3, 5, 7, 9

def ProgArrayGenerator(n, a1, d):
    progArray = []
    for i in range (1, n+1):
        a_i = a1 + (i - 1) * d
        progArray.append(a_i)
    return progArray

print()
print("ЗАДАЧА # 1.")
a1 = int(input("Введите первый элемент арифметической прогрессии a1: "))
d = int(input("Введите разность элементов d: "))
n = int(input("Введите количество элементов n: "))
myArray = ProgArrayGenerator(n, a1, d)
print(myArray)

#############################################################################################################################

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

def CreateArray(size):
    array = []
    for i in range (0, size):
        value =  int(input("Введите элемент массива: "))
        array.append(value)
    return array

def PrintArray(array, comment):
    print(comment, ": ", end="")
    print("[ ", end="")
    for i in range (0, len(array)):
        print(array[i], end=" ")
    print("]")

def Finder(array, min, max):
    for i in range (len(array)):
        if (array[i] >= min and array[i] <= max):
            print(i, end=", ")

print()
print("ЗАДАЧА # 2.")
arraySizeFirst = int(input("Введите размер 1-го массива: "))
myArray = CreateArray(arraySizeFirst)
PrintArray(myArray, "1-ый массив: ")
min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))
Finder(myArray, min, max)