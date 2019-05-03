
from timeit import Timer
import cProfile
import os
import random
import sys
from pympler import asizeof
from memory_profiler import memory_usage , profile
#from guppy import hpy


m = 1000

print("Задача: получить квадраты значений последовательности чисел\n")
print("Решаем через списки..")

# @profile 
def list_quad(n):
    lst = [random.randint(0,100) for _ in range(n)]
    lst2 = [lst[_]*lst[_] for _ in range(n)]

    return lst2

#print(list_quad(20))
print("cProfile показывает затратные процедуры по количеству вызовов:")
cProfile.run("list_quad(m)")

a = os.system("list_quad(m)")
print("Результат os.system ", a)
print("memory_usage", memory_usage())
a1 = sys.getsizeof(list_quad(m))
print("sys.getsizeof ", a1)
print("id ", id(list_quad(m)))
print("asizeof", asizeof.asizeof(list_quad(m)))

if __name__=='__main__':
    
    t = Timer(lambda: list_quad(m))
    f = t.timeit(number=200)
    print("Результат timeit ", f )


print("\n\nСгенерированный и расчитанный списки преобразуем в кортеж ")

def list_quad2(n):
    lst = [random.randint(0,100) for _ in range(n)]
    lst = tuple(lst)
    lst2 = [lst[_]*lst[_] for _ in range(n)]
    lst2 = tuple(lst2)
    return lst2

#print(list_quad(20))
print("cProfile показывает те же затратные процедуры по количеству вызовов:")
cProfile.run("list_quad2(m)")

b = os.system("list_quad2(m)")
print("Результат os.system ", b)
print("memory_usage", memory_usage())
b1 = sys.getsizeof(list_quad2(m))
print("sys.getsizeof  ", b1 )
print("id", id(list_quad2(m)))
print("asizeof", asizeof.asizeof(list_quad2(m)))

if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: list_quad2(m))
    g = t.timeit(number=200)
    print("Результат timeit ", g )

    
print("\n\nРезультат timeit различается на ", (f/g - 1)*100, "%.")    
print("Результат sys.getsizeof различается на ", (a1/b1 - 1)*100, "%.")  

