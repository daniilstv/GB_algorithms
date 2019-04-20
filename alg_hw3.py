""" 
Дьяченко Даниил
Алгоритмы и структуры данных на Python.
Домашнее задание к уроку 3.

В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
Определить, какое число в массиве встречается чаще всего.
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
Найти максимальный элемент среди минимальных элементов столбцов матрицы. Примечание. Решите 6 интересных для вас задач из 9 (блок-схемы были нужны только в первом уроке, в этом и следующих практических заданиях их использование по желанию)
"""

# HW3.1 done

l = [randint(2,100) for x in range(50)]

b = 0
for j in range(2,10):
    for i in range(len(l)):
        if l[i] % j == 0:
#            print(j)
            b += 1
    print(j, "кратно", b, "раз")
    b = 0



# HW3.2 done

l = [randint(0,100) for x in range(50)]
print(l)
n = []
for i in range(50):
    if l[i] % 2 == 0:
        n.append(i)
print(n)



# HW3.3 done
from random import randint

l = [randint(0,1000) for x in range(50)]
print("Индекс минимального значения - ", l.index(min(l)), "Значение - ", min(l))
print("Индекс максимального значения - ", l.index(max(l)), "Значение - ", max(l))

a, b = l[l.index(min(l))], l[l.index(max(l))]
l[l.index(max(l))], l[l.index(min(l))] = a, b
# l[l.index(min(l))], l[l.index(max(l))] = l[l.index(max(l))], l[l.index(min(l))]

print("Индекс минимального значения - ", l.index(min(l)), "Значение - ", min(l))
print("Индекс максимального значения - ", l.index(max(l)), "Значение - ", max(l))


# HW3.4.1
# Со словарем решения не получилось. Не дошел до того как вытащить ключ.
l = [randint(1,100) for x in range(50)]
n = dict.fromkeys(l,0)
a = 0
for i in n.keys():
    for j in l:
        if i == j:
            n[i] = n[i] + 1
print(max(n.values()))



# HW3.4 done
l = [randint(1,100) for x in range(50)]
count_max = 0
for i in range(len(l)):
    count = 1
    for j in range(len(l)):
        if l[i] == l[j]:
            count += 1 
    if count > count_max:
        count_max = count
        x = l[i]
print(x , " встречается x",  count_max)



# HW3.5 done

l = [randint(-50,50) for x in range(50)]
print(l)
b = 0    
c = - 50
for i in range(len(l)):
    b = l[i]
    if l[i] < 0:
        b = l[i]
        if c < b:
            c = b
            
print(c) 



# hw 3.8 done

#matrix = [ [ randint(1,100) for i in range(4)] for i in range(4)]
matrix = [ [ int(input("..")) for i in range(4)] for i in range(4)]
for i in range(4):
    
    print(*matrix[i], " sum = ", end="")
    print(sum(matrix[i]))


# hw 3.9 done

a = 8
matrix = [ [ randint(1,100) for i in range(a)] for i in range(a)]

# rotate = list(map(list, zip(*matrix)))
result = 0
for x in range(len(matrix)):
    n = matrix[0][x]
    for i in range(1,len(matrix)):
        if n > matrix[i][x]:
            n = matrix[i][x]
    print(n)
    
    if result < n:
        result = n
print(result)