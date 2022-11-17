# print('Molekula')
# peoples = 48
# while True:
#     age = int(input('Age: '))
#     deposit = int(input('Deposit: '))
#     dc = int(input('Input 1 if you classic 2 if no: '))
#     fc = int(input('Face control 1 to 10: '))
#     tanysh = input('Are you have Bratan? Yes/No ')
#     exit = input('Exit? Y/N ')
    
#     if age >= 21 and deposit >= 2000 and dc == 1 and (fc >= 7 or fc <= 10) or deposit >= 100_000 or tanysh == 'Yes' and fc == 10:
#         print(f'Welcome, in Malekula {peoples} peoples')
#         if peoples < 50:
#             peoples += 1
#             print(f'Welcome, in Malekula {peoples} peoples')    
#         else:
#             print(f'Sorry in club {peoples} peoples club is full')
#             break
#         if exit == 'Y':
#             break
#         continue
#     else:
#         print('Good bye')
#         if exit == 'Y':
#             break
#         continue

# for i in range(0, 10, 2):
#     print(i)

# print(list(range(10)))

# i = 0
# while i < 10:
#     print(i)
#     i += 1


# languages = ['go', 'java', 'php', 'python', 'javascript', 1111111,  'ruby']
# num = 1

# for i in languages:
#     print(i)

#     for j in str(i):
#         print(j + str(num))
#         num += 1


# num1 = 7
# for i in range(4):
#     num1 *= num1 
#     print(num1)

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# a = 1
# for i in languages:
#     print(str(a)+i)
#     a += 1


# num5 = 0
# while num5 < 10:
#     print
#     num5 += 1



'''
Создайте 2 переменные 
со значениями 2**3 и 3**2 и покажите значение переменной в которой значение больше.
'''
# num1 = 2 ** 3
# num2 = 3 ** 2
# if num1 > num2:
#     print(f'num1 больше чем num2', num1)
# else:
#     print(f'num2 больше чем num1', num2)

'''
Создайте условие которое определит самое большое и самое маленькое число из трёх.
'''
# print(max([5,143,345]))
# print(min([432,543,312]))



'''
Есть три числа 17391, 546, 934.

Если каждое из них поделить на 17 по модулю, где остаток меньше всего? 
'''
# sum1 = 17391 % 17
# sum2 = 546 % 17
# sum3 = 934 % 17
# if sum1 <= sum2 and sum1 <= sum3:
#     print(f'sum1:', sum1)
#     if sum2 <= sum1 and sum2 <= sum3:
#         print(f'sum2:', sum2)
# else:
#     print(f'sum3:', sum3)



'''
Есть переменная 

x = 13.

Нужно возвести её в квадрат и сравнить с числом 172.

Если x всё ещё меньше возвести в квадрат ещё раз.
'''
# x = 13
# s = x ** 2
# if s <= 172:
#     s *= 2
#     print(s)
# else:
#     print(f'x равно', 172)

'''
Написать программу которая проверит число на несколько критериев:

Чётное ли число?

Делится ли число на 3 без остатка?

Если возвести его в квадрат, больше ли оно 1000?
'''
# summ = int(input())
# if summ % 2 == 0:
#     print('Четное')
# else:
#    print('Не четное')

# if summ % 3 == 0:
#     print('Делится')
# else:
#     print('Не делится')

# ss = summ ** 2
# if ss >= 1000:
#     print('Больше', ss)
# else:
#     print('Меньше', ss)


'''
У нас есть числа от 0 до 100, но не все числа разрешены!

Разрешенённые:

От 0 до 21

От 57 до 100

Как узнать что какое-то число из запрещёноого диапазона?
'''
# for i in range(0, 101):
#     if i > 0 and i <= 21 or i >= 57 and i <= 100:
#         print(i, 'Разрешен!')
#     else:
#         print(i, 'Запрещен')



'''
Создайте условие которое будет срабатывать в любом случае.
'''
# if True:
    # print('Хочу есть!')

'''
Создайте 3 вложенных друг в друга условия.
'''
# old = int(input('Ваш возраст: '))
# print('Рекомендовано:', end=' ')
# if 3 <= old < 6:
#     print('"Заяц в лабиринте"')
 
# if 6 <= old < 12:
#     print('"Марсианин"')
 
# if 12 <= old < 16:
#     print('"Загадочный остров"')
 
# if 16 <= old:
#     print('"Поток сознания"')


'''
У вас есть переменная а=10//5 и b=10/5

Ровны ли переменные a и b?

если они равны выведите  их сумму
'''
# a = 10 // 5
# b = 10 / 5
# if a == b:
#     print(f'Равен', a, b)
# else:
#     print(f'Не равен')



'''
Напишите условие, которое выводит отрицательные числа
'''
sam = int(input())
if sam > 0:
    print('Положителное')
else:
    print('Отрицательное')