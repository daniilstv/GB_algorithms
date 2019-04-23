import timeit
import profile
import cProfile




print("Анализ нагруженных элементов в функции показал, что самый затратный элемент - len()")
def sort_to_max(origin_list):
    
    a = origin_list
    n = 0
    for i in range(len(a)-1) :
        for i in range(len(a)-1) :
            if a[i] < a[i+1]:
                n = a[i]
                a[i] = a[i+1]
                a[i+1] = n
    return(a)
#sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

cProfile.run("sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])")
profile.run("sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])")


print("Убрали бутылочное горлышко , исключив len() из кода, указав длину явно.")

def sort_to_max_9(origin_list):
    
    a = origin_list
    n = 0
    for i in range(8) :
        for i in range(8) :
            if a[i] < a[i+1]:
                n = a[i]
                a[i] = a[i+1]
                a[i+1] = n
    return(a)
cProfile.run("sort_to_max_9([2, 10, -12, 2.5, 20, -11, 4, 4, 0])")
profile.run("sort_to_max_9([2, 10, -12, 2.5, 20, -11, 4, 4, 0])")

## ----

# Сравнение алгоритмов Фибоначи 

def fibonacci(m):
    a = [1,1]
    i = 1
    m = m+1
    for i in range(m-2):
        a.append(a[i]+a[i+1])  
    return(a[m-2]) 
#fibonacci(11)
cProfile.run("fibonacci(15)")

def f(n):
#    n+=1
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)

#f(11)
cProfile.run("f(15)")



    
print("Сравнение алгоритмов нахождения числа Фибоначи:")

def fibonacci(m):
    a = [1,1]
    i = 1
    m = m+1
    for i in range(m-2):
        a.append(a[i]+a[i+1])  
    return(a[m-2]) 
#fibonacci(11)
#cProfile.run("fibonacci(15)")

def f(n):
#    n+=1
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)

#f(11)
#cProfile.run("f(15)")

print("Метод прохождения последовательности")
print(timeit.timeit("fibonacci(15)", setup="from __main__ import fibonacci", number=1))
print("Рекурсивный метод")
print(timeit.timeit("f(15)", setup="from __main__ import f", number=1))


def primes(n):
    a = [0] * n # создание массива с n количеством элементов
    for i in range(n): # заполнение массива ...
        a[i] = i # значениями от 0 до n-1
     
    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
     
    m = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n: # перебор всех элементов до заданного числа
        if a[m] != 0: # если он не равен нулю, то
            j = m * 2 # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0 # заменить на 0
                j = j + m # перейти в позицию на m больше
        m += 1
     
    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
     
    del a
    return b

#primes(200)

print("Решето Эратосфена")
print(timeit.timeit("primes(1000)", setup="from __main__ import primes", number=1000))