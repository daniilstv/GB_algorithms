print("\n 1.1 Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.")

a = list(input("Введите трёхзначное число "))
print("Сумма цифр трехзначного числа", int(a[0]) + int(a[1]) + int(a[2]))
print( "Произведение цифр трехзначного числа", int(a[0]) * int(a[1]) * int(a[2]))


print("\n 1.2 Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6." \
    "\nВыполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.")

a = 5
print(f"{a} = {bin(a)} ")
b = 6
print("%d = %s" % (b, bin(b)))

print("Результат побитового ИЛИ ", bin(a) or bin(b))
c = bin(a|b)
c = int(c, 2)
print('Преобразование результата в int10', c)

print("Результат побитового И ", bin(a & b))
d = bin(a) and bin(b)
d = int(d, 2)
print('Преобразование результата в int10', d)

print("Смещение вправо", bin(a>>2), "int:", int( bin(a>>2), 2 ))
print("Смещение влево", bin(a<<2), "int:", int( bin(a<<2), 2 ))


print("\n 1.6 Пользователь вводит номер буквы в алфавите. Определить, какая это буква.")

a = int(input("Введите номер буквы:"))+96
print(chr(a))


print("\n 1.8 Определить, является ли год, который ввел пользователь, високосным или невисокосным." \
"\nВисокосные года делятся нацело на 4. Однако из этого правила есть исключение:",
"\nстолетия, которые не делятся нацело на 400, високосными не являются.")

a = int(input("Введите год, который хотите проверить: "))
if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
    print("Год невисокосный")
else:
    print("Год високосный")

print("\n 1.9 Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).")

a = input("Введите три числа:").split(" ")

if a[0] < a[1] < a[2] or a[2] < a[1] < a[0]:
    print(a[1])
elif a[1] < a[2] < a[0] or a[0] < a[2] < a[1]:
    print(a[2])
else:
    print(a[0])


print("\n 1.3 По введенным пользователем координатам двух точек вывести уравнение прямой вида ")

#y=kx+b, проходящей через эти точки.
a = input("Введите координаты двух точек через пробел:").split(" ")

k = (int(a[1]) - int(a[3]) )/ (int(a[0]) - int(a[2]))
b = int(a[3]) - k*int(a[2])
print(" y = %.2f*x + %.2f" % (k, b))
