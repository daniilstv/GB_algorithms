import timeit
import profile
import cProfile

print("Анализ расчета чисел Фибоначи ") 
def fibonacci(n, m):
    pass
    a = [1,1]
    i = 1
    for i in range(m-2):
        a.append(a[i]+a[i+1])  
    return(a[n-1:m]) 

cProfile.run("fibonacci(150, 152)")
profile.run("fibonacci(150, 152)")

# ---


print("Анализ нагруженных элементов в функции показал, что самый затратный элемент - len()")
def sort_to_max(origin_list):
    pass
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
    pass
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

