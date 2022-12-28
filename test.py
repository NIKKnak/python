
import os
os.system('cls' if os.name == 'nt' else 'clear')
##################################################################
# n, roman_numbers = int(input()), ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
# print(roman_numbers[n-1] if 1 <= n <= 10 else 'ошибка')
##################################################################



a = int(input())
b = a // 100
c = a % 10
f = (a % 100) //10
g = max(b,c)
h = min(b,c)

print(g)
print(h)
print((a % 100) //10)
if g - h == (a % 100) //10:
    print('Число интересное')
else:
    print('Число неинтересное')