from memory_profiler import profile 
import random
m = 100000
@profile 
 


def list_quad2(n):
    lst = [random.randint(0,100) for _ in range(n)]
    lst = tuple(lst)
    lst2 = [lst[_]*lst[_] for _ in range(n)]
    lst2 = tuple(lst2)
    return lst2

if __name__ == '__main__':
    list_quad2(m) 