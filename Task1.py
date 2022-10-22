# #Задача 1. добавить к аргументу "а" и вывести результат.
# x = lambda a: a+10
# print(x(5))

# #Задача 2. перемножить аргументы и вывести результат.
# x = lambda a, b: a*b
# print(x(5,6))

# #Задача 3. Посчитать сумму чисел и вывести результат.
# x = lambda a, b, c: a+b+c
# print(x(5,6,2))

# #Задача 4. Использовать функцию для перемножения ф-ии и числа.
# def myfunc(n):
#     return lambda a: a*n
# mydoubler = myfunc(2)# (a)
# print(myfunc(11))# адрес ячейки памяти
# print(mydoubler(11))#(11) 22

#Задача 5. Использовать функцию lambda заменить строчные буквы
# на прописные и сделать разворот строки
# strl='GeekforGeeks'
# rev_upper = lambda string: string.upper()[::-1]
# print(rev_upper(strl))# SKEEGROFKEEG
# #print(rev_upper)# адрес ячейки памяти

# Задача 6. Применить ф-ию if else в ф-ии lambda
# Max=lambda a, b: a if (a>b) else b
# print(Max(55,2))

# # Задача 7. выбрать из каждого списка второе после масимального число
# list=[[2, 3, 4],[1, 4, 16, 64], [3, 6, 9, 12]]
# sortList= lambda x: (sorted(i) for i in x)#сортировка
# secondLargest = lambda x, f: [y[len(y)-2] for y in f(x)]#2й с конца списка
# res = secondLargest(list, sortList)
# print(res)

# # Задача 8. отсортируйте кортеж по второму признаку
# subject_marks= [('English', 88), ('Science', 90), ('Maths', 97), ('Social Science', 82)]
# print('исходный список:')
# print(subject_marks)
# subject_marks.sort(key=lambda x: x[1])
# print(subject_marks)

# #Задача 8. отсортировать список по четным и нечетным числам
# from pyparsing import nums
# nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('исходный список чисел:')
# print(nums)
# print('\n Список четных чисел:')
# even_nums=list(filter(lambda x: x%2==0, nums))
# print(even_nums)
# print('\n Список нечетных чисел:')
# odd_nums=list(filter(lambda x: x%2!=0, nums))
# print(odd_nums)

# #Задача 9. используя ф-ию filter выбрать нечетные числа
# li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# final_list=list(filter(lambda x: x%2!=0, li))
# print(final_list)

# #Задача 10. выберите людей из списка с возрастом старше 18лет
# ages =[13, 90, 17, 59, 21, 60, 5]
# adults=list(filter(lambda ages: ages>18, ages))
# print(adults)

# #Задача 11. перемножить все элементы списка на 2 используя map и lambda
# li =[13, 90, 17, 59, 21, 60, 5]
# final_list=list(map(lambda x: x*2, li))
# print(final_list)

# # #Задача 12. удвоить значение чисел списка
# def addition(n):
#     return n+n
# numbers =[13, 90, 17, 59, 21, 60, 5]
# result =map(addition, numbers)
# print(list(result))

# #Задача 13. преобразовать все элементы списка на прописные
# animals=['dog', 'cat', 'parrot', 'rabbit']
# uppend_animals = list(map(lambda animals: animals.upper(), animals))
# print(uppend_animals)

# #Задача 14. Пронумеруйте список
# l1=['eat', 'sleep', 'repeat']
# s1 = 'geek'
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)
# print('return type:', type(obj1))#выдаст тип данных
# print(list(enumerate(l1)))#выдаст пронумерованный список начиная с "0"
# print(list(enumerate(s1,2)))#выдаст пронумерованный список начиная с "2"
# for x in enumerate(l1,1):#выдаст пронумерованный столбец начиная с "1"
#     print(x)#выдаст список в столбец

# # задача 15. демонстрация функции enumerate
# l1=['eat', 'sleep', 'repeat']
# for ele in enumerate(l1,1):#выдаст пронумерованный столбец начиная с "1"
#     print(ele)
# for count, ele in enumerate(l1,100):#выдаст пронумерованный столбец начиная с "100"
#     print(count, ele)
# for count, ele in enumerate(l1,1):#выдаст пронумерованный столбец начиная с "1"
#     print(count)
#     print(ele)

# # задача 16. выбрать слова из списка с буквой "а"
# fruits=['apple', 'banana', 'cherry','kiwi','mango']
# new_list=[]
# for x in fruits:
#     if 'a' in x:
#         new_list.append(x)
#         print(new_list)#выдаст список прибаляяя по 1 слову
# print(new_list)#выдаст сразу список
# new_list=[x for x in fruits if 'a' in x]
# print(new_list)#выдаст сразу список

# #Задача 17. Пронумеровать список
# values = ['a', 'b', 'c']
# index=1
# for value in values:
#     print(index,value)
#     index +=1
# for value in enumerate(values,1):
#     print(value)

# #Задача 18. Составить список из слова
# h_letters = []
# text = 'human'
# for letter in text:
#     h_letters.append(letter)
# print(h_letters)

# h_letters=[letter for letter in 'human']
# print(h_letters)

# #Задача 19. Пример фйнкции zip
# a =  ['John', 'Christy','Monika']
# b = ('Jerry', 'Charles', 'Mike')
# x = zip(a,b)
# print(x)#выдаст ячейку памяти
# list(zip(a,b))
# print(list(zip(a,b)))#выдаст список

#Задача 20. Выдать список со случайной последовательностью
name = ['Manjeet', 'Nikhil', 'Shambhavi', 'Astha']
roll_no=[4, 1, 3, 2]
mapped = zip(name, roll_no)
print(set(mapped))