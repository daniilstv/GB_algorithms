import timeit
import cProfile
import os
import random

m = 1000

print("Задача: получить квадраты значений последовательности чисел\n")
print("Решаем через списки..")
def list_quad(n):
    lst = [random.randint(0,100) for _ in range(n)]
    lst2 = [lst[_]*lst[_] for _ in range(n)]
    return lst2

#print(list_quad(20))
print("cProfile показывает затратные процедуры по количеству вызовов:")
cProfile.run("list_quad(m)")

a = os.system("list_quad(m)")
print("Результат os.system ", a)

if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: list_quad(m))
    print("Результат timeit " )
    f = t.timeit(number=200)
    print (f)
    
   

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


if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: list_quad2(m))
    print("Результат timeit " )
    g = t.timeit(number=200)
    print (g)
    
print("Результат timeit разлиичается на ", (f/g - 1)*100, "%.")    
print("\n\nПровел несколько экспериментов. Значение os.system не поменялось. Результат timeit колеблется +-10% Отличия не являются статистически значимыми.")