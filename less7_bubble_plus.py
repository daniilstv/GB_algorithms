#from memory_profiler import profile 
#%%
import random
import copy
n = 15
min_rnd = -100
max_rnd = 100 
def rnd_lst(n, min_rnd = min_rnd , max_rnd = max_rnd):
    rnd_list = [random.randint(min_rnd, max_rnd) for i in range(n)]
    print("Создали список из %d элементов:" % (n) )
    return rnd_list

rnd_lst = rnd_lst(n)
print(*rnd_lst)

#%%
print("Пузырьковая сортировка:")
# @profile
a = copy.deepcopy(rnd_lst)

def sort_to_max(origin_list):
    pass
    n = 0
    for i in range(len(a)-1) :
        for i in range(len(a)-1) :
            if a[i] > a[i+1]:
                n = a[i]
                a[i] = a[i+1]
                a[i+1] = n
    return(a)

print(*sort_to_max(a))

#%%

''' 7.3 Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках.
'''
print("Решение задачи 7.3 по отсортированному массиву..")
print(*a)
if len(a)%2 == 0:
    print(a[len(a)//2], a[len(a)//2-1], "-> медиана:", ( int (a[len(a)//2]) + int(a[len(a)//2-1]) ) / 2 )
    
else:
    print("Медиана:",a[len(a)//2])


#%%
print("Решение задачи 7.3 собственным алгоритмом по неотсортированному массиву с нечетным числом элементов..")
b = copy.deepcopy(rnd_lst)
print(*b)

def id_min(lst, max_rnd = max_rnd):
    x_min = max_rnd+1
    x_min_idx = 0
    for i in range(len(lst)):
        if x_min > lst [i]:
            x_min = lst [i]
            x_min_idx = i
    return x_min_idx

def id_max(lst, min_rnd = min_rnd):
    x_max = min_rnd - 1
    x_max_idx = 0
    for i in range(len(lst)):       
        if x_max < lst [i] :
            x_max = lst [i]
            x_max_idx = i
    return x_max_idx
#%%
for i in range(len(b)//2):
 #   print("По индексу удаляю максимальное и минимальное значение в массиве. Индексы: ", id_max(b), id_min(b))
    b.pop(id_max(b))
    b.pop(id_min(b))

print("Медиана:", *b)
