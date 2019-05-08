import timeit
import random
from memory_profiler import memory_usage , profile
import sys
from pympler import asizeof

''' 
print("1. Анализ расчета чисел Фибоначи ") 
def fibonacci(n, m):
    pass
    a = [1,1]
    i = 1
    for i in range(m-2):
        a.append(a[i]+a[i+1])  
    return(a[n-1:m]) 

'''


print("1. Пузырьковая сортировка")

rnd_list = [random.randint(-100, 100) for i in range(100)]

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
#print(sort_to_max(rnd_list))


print("2. Пузырьковая сортировка с фиксированной длиной списка")

tuple(rnd_list)

def sort_to_max_9(origin_list):
    pass
    a = origin_list
    n = 0
    for i in range(99) :
        for i in range(99) :
            if a[i] < a[i+1]:
                n = a[i]
                a[i] = a[i+1]
                a[i+1] = n
    return(a)

print("Показатели памяти:")


print("memory_usage", memory_usage())
a = sys.getsizeof(sort_to_max(rnd_list))
print("sys.getsizeof ", a )
print("asizeof", asizeof.asizeof(sort_to_max(rnd_list)))

if __name__=='__main__':
    
    t = timeit.Timer(lambda: sort_to_max(rnd_list))
    f = t.timeit(number=100)
    print("Результат timeit ", f )
    
    
if __name__=='__main__':
    
    t = timeit.Timer(lambda: sort_to_max_9(rnd_list))
    f = t.timeit(number=100)
    print("Результат timeit без расчета len ", f )