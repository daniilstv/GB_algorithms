from memory_profiler import profile 
#import random

#rnd_list = [random.randint(-100, 100) for i in range(500)]



print("Анализ расчета чисел Фибоначи ") 

@profile
def fibonacci(n, m):
    pass
    a = [1,1]
    i = 1
    for i in range(m-2):
        a.append(a[i]+a[i+1])  
    return(a[n-1:m]) 

if __name__ == '__main__':
    fibonacci(1000, 1000000)

