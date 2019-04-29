#import collections
# не нашел пока, для. чего тут применить модуль collections. Реализовал на словаре.

db = {}
n = int(input("Введите количество предприятий: "))

for i in range(n): # Заполнение словаря данными о предприятиях
    name = str(input(f"Введите название предприятия {i+1} "))
    quoters = []
    sum_prib = 0
    avg_prib = 0
    for j in range(4):
        quoters.append(int(input(f"Прибыль в {j}-м квартале: ")))
        sum_prib += quoters[j-1]
    
    quoters.append(sum_prib)
    avg_prib = sum_prib / 4 # среднемес. прибыль - не используется в дальнейшем
    quoters.append(avg_prib)
    db[name] = quoters
    
    
#print(db)


total_sum = 0

for i in db:
#    print(db[i][4])
    total_sum += db[i][4]

avg_total_sum = total_sum / len(db)
print("Средняя прибыль по предприятиям за год - ", avg_total_sum)

for i in db:
#    print(db[i][4])
    total_sum += db[i][4]

above_avg = [x for x in db if db[x][4] > avg_total_sum]
print("Предприятия с прибылью выше среднего: ", *above_avg)

below_avg = [x for x in db if db[x][4] < avg_total_sum]
print("Предприятия с прибылью ниже среднего: ", *below_avg)