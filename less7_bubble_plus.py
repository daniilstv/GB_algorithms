#from memory_profiler import profile 
#%%
import random
import copy
n = 13
def rnd_lst(n):
    rnd_list = [random.randint(-100, 100) for i in range(n)]
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
print("Решение задачи 7.3 по отсортированному массиву:")
print(*a)
if len(a)%2 == 0:
    print(a[len(a)//2], a[len(a)//2-1], "-> медиана:", ( int (a[len(a)//2]) + int(a[len(a)//2-1]) ) / 2 )
    
else:
    print("Медиана:",a[len(a)//2])


#%%
# в работе
# print("Решение задачи 7.3 по неотсортированному массиву:")
b = copy.deepcopy(rnd_lst)