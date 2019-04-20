""" 
Дьяченко Даниил
Алгоритмы и структуры данных на Python.
Домашнее задание к уроку 2.
"""


# 2. Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input("Введите число: "))
ch = 0
ne_ch = 0
while a / 10 > 0.01:
    b = a % 10
    print(b)
    if b % 2 == 0:
        ch += 1 
    else:
        ne_ch += 1
    a = a // 10 
print(f"Четных {ch}, не четных {ne_ch}")

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

a = int(input("Введите число: "))
c = 0
while a / 10 > 0.01:
    b = a % 10 
    c = c*10 + b
#    print(c)    
    a = a // 10 
print(c)

#  4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125...
# Количество элементов (n) вводится с клавиатуры.

a = int(input("Введите количество элементов "))
b = 1
c = 0
for i in range(a-1):
    b = b / 2 * (-1)
    c += b
print(c)

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

a = (127 - 32) // 10
b = 0
for j in range( a + 1 ):
    for i in range (10):
        if i+b+32 < 128:
            print(f"{i+b+32}:{chr(i+b+32)}",end=' ')
    b += 10
    print("\n")

# 6. В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться больше или меньше 
# введенное пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint 

a = randint(0,100)

for i in range(9):
    b = int(input("Угадайте число "))
    if a == b:
        print("Вы угадали!")
        break
    elif a < b:
        print("Ваше число больше загаданного")
    else: # a > b:
        print("Ваше число меньше загаданного")
print("Было загадано ", a)

# 7. Напишите программу, доказывающую или проверяющую, 
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, 
#  где n - любое натуральное число.

a = int(input("Введите размер множества:"))

b =  0
c = a*(a+1)/2

for i in range(1, a+1):
    b += i
#    print (b)

print("Для множества чисел: 1+2+...+n = n(n+1)/2")
print(c == b)
print (b, c)
    
# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. 
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

a = int(input("Введите цифру "))
b = int(input("Введите последовательность "))
c = 0
while b / 10 > 0.01:
    if a == b % 10:
        c += 1
    
    b = b // 10 
    
print(f"Цифра {a} встречается {c} раз")


# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
# Вывести на экран это число и сумму его цифр.

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = 0
d = 0
a1 = a
b1 = b

while a / 10 > 0.01:
    c += a % 10
    a = a // 10 
#print (c)

while b / 10 > 0.01:
    d += b % 10
    b = b // 10 
#print (d) 

if c < d:
    print("Число {} Сумма цифр {}".format(b1,d))
    
elif c > d:
    print("Число {} Сумма цифр {}".format(a1,c))
else:
    print("Сумма цифр обоих чисел равна {}".format(c))
    