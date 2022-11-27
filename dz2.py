# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


x = input('Введите число ')

#Проверка на знак перед числом
def summa(x):                            
    if float(x) < 0:                            
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел равна {summa(x)}')


####################################################################
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

x = int(input('Введите число '))
y = 1
for i in range(x):
    i +=1
    y = i * y
    print(y, end=" ")



######################################################################
# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: ')) 

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))

#####################################################################
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
from random import Random, randint

N = int(input('Введите число '))
numbers = []

for i in range(N):
    numbers.append(randint(-N,N+1))
    
print(numbers)
print(numbers[1] * numbers[3])

f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)