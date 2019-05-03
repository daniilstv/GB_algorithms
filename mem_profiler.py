from memory_profiler import profile 
import random
m = 100000
@profile 
def list_quad(n):
    lst = [random.randint(0,100) for _ in range(n)]
    lst2 = [lst[_]*lst[_] for _ in range(n)]

    return lst2
if __name__ == '__main__':
    list_quad(m) 