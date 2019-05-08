from memory_profiler import profile 
import random

# print("Пузырьковая сортировка")

rnd_list = [random.randint(-100, 100) for i in range(1000)]

@profile

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

if __name__ == '__main__':
    sort_to_max(rnd_list) 

#print(sort_to_max(rnd_list))