

def hex2ten(n): # конвертация в десятичный код
    for i in range(len(n)):
        if n[i] == "A":
            n[i] = 10
        elif n[i] == "B":
            n[i] = 11
        elif n[i] == "C":
            n[i] = 12
        elif n[i] == "D":
            n[i] = 13
        elif n[i] == "E":
            n[i] = 14  
        elif n[i] == "F":
            n[i] = 15           
    return n

def ten2hex(n): # обратная конвертация в шестнадцатиричный код
    for i in range(len(n)):
        if n[i] == 10:
            n[i] = "A"
        elif n[i] == 11:
            n[i] = "B"
        elif n[i] == 12:
            n[i] = "C"
        elif n[i] == 13:
            n[i] = "D"
        elif n[i] == 14:
            n[i] = "E"  
        elif n[i] == 15:
            n[i] = "F"           
    return n

def sum_ten(a,b): # сложение списков приведенных к десятичной системе
    len_a = len(a)
    len_b = len(b)
    c = ()
    d = ()

    if len_a >= len_b: # определяем первое слогаемое, бОльшее по разрядам. Разворачиваем списки
        c = a
        c.reverse()   

        d = b
        d.reverse()
        for i in range(len_a - len_b): # добиваем разряды второго слогаемого нулями
            d.append(0)

    else:
        c = b
        c.reverse()   
        d = a
        d.reverse()
        for i in range(len_b - len_a):
            d.append(0)


    for i in range(len(c)-1): # сложение бОльшего списка с меньшим по правилам 16х
        c[i] = int(c[i]) + int(d[i])
        c[i+1] = int(c[i+1]) + int(c[i]) // 16
        c[i] = int(c[i]) % 16

    if int(c[len(c)-1])+int(d[len(d)-1]) >= 16:            
        c.append( (c[len(c)-1]+int(d[len(d)-1]))// 16 )
        c[len(c)-2] =  (c[len(c)-2]+int(d[len(d)-1])) % 16
            

    c.reverse() # обратный разворот результата
    #d.reverse()
    return c
   
    
a = list(input("Введите первое шестнадцатеричное число "))

b = list(input("Введите второе шестнадцатеричное число "))
e = ()
e = a.copy()

f = list(input("Введите множитель для первого числа "))
hex2ten(f)
f.reverse()

n = 0
for i in range(len(f)):
    n += int(f[i])
print("Умножаем на ", n) 
    
hex2ten(a)
hex2ten(b)
c = sum_ten(a,b)
ten2hex(c)
print("Cумма чисел равна:", c)

g = [0]
hex2ten(e)
#print(e)
for i in range(n):
  #  print(g)
    g = sum_ten(g,e)
#    print(g)
#print(g)
ten2hex(g)

print("Произведение первого числа равно:", g)


