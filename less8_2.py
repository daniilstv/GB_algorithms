import hashlib
import cProfile
import random
import string

char_set = string.ascii_lowercase
s = ''.join(random.sample(char_set *100, 1000))
#s = input("Введите строку из маленьких латинских букв")
#s = "kjgvkjgvkgvkhgvkjhgvkjhgvkhgvkhgvjkhgvkhgckhgckhgcfcngfcjghfcvhvjhbkjhvkgv"
#s = "hello"



def substring_counter(s):
    uniq_set = []

    # секция оптимизации, чтобы каждый раз не расчитывать длину и не добавлять лишние хэши
    zero = ""
    zero_md5 = hashlib.md5(zero.encode('utf-8')).hexdigest()
    full_md5 = hashlib.md5(s.encode('utf-8')).hexdigest()
    len_s = len(s)
    #print(zero_md5)

    for i in range(len_s):
        for j in range(len_s): # проход вправо
        
            line = s[:i+j]
            hash_string = hashlib.md5(line.encode('utf-8')).hexdigest()
            if hash_string != zero_md5 and hash_string != full_md5 :
                uniq_set.append(hash_string)  
                #print("проход влево s[:i+j]", line)   


            line = s[i+j:]
            hash_string = hashlib.md5(line.encode('utf-8')).hexdigest()
            if hash_string != zero_md5 and hash_string != full_md5 :
                #print("проход вправо s[i+j:]", line)
                uniq_set.append(hash_string)

            line = s[j:i]
            hash_string = hashlib.md5(line.encode('utf-8')).hexdigest()
            if hash_string != zero_md5 and hash_string != full_md5 :
                #print("проход к центру s[j:i]", line)
                uniq_set.append(hash_string)
            
            # Есть подозрение, что у меня не все проверки на вхождение подстрок.
            # Не хватает выборки подстроки переменной длины разноудаленной от начала и конца 

    return len(set(uniq_set))
   
print("В заданной строке " , substring_counter(s) , " подстрок. Рассчитано на hash md5.")
cProfile.run("substring_counter(s)") 

def substring_counter_wo_hash(s):
    uniq_set = []

    # секция оптимизации, чтобы каждый раз не расчитывать длину
    len_s = len(s)


    for i in range(len_s):
        for j in range(len_s): # проход вправо
        
            line = s[:i+j]
            
            if line != "" and line != s :
                uniq_set.append(line)  
                #print("проход влево s[:i+j]", line)   


            line = s[i+j:]
            
            if line != "" and line != s :
                #print("проход вправо s[i+j:]", line)
                uniq_set.append(line) 

            line = s[j:i]
            if line != "" and line != s :
                #print("проход к центру s[j:i]", line)
                uniq_set.append(line) 
    return len(set(uniq_set))

print("В заданной строке " , substring_counter_wo_hash(s) , " подстрок. Рассчитано без hash")
cProfile.run("substring_counter_wo_hash(s)") 

print("На малых строках алгоритм без хэша производительнее, т.к. нет затрат на хеширование.")
print("На строке в 1000 случайных символов алгоритм без хэша производительнее в 4 раза")