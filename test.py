
# import os
# os.system('cls' if os.name == 'nt' else 'clear')
# ##################################################################
# # n, roman_numbers = int(input()), ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
# # print(roman_numbers[n-1] if 1 <= n <= 10 else 'ошибка')
# ##################################################################







# a = int(input())
# count = 0
# while 0 < a <= 5:
#     if a == 5:
#         count +=1
#     a = int(input())
# print(count)
   

((x < oo) & (-1 + sqrt(7) < x)) | ((-oo < x) & (x < -sqrt(7) - 1))
f<0: (x < -1 + sqrt(7)) & (-sqrt(7) - 1 < x)

print ('Дана функция f(x) = 5x^2 + 10x - 30')
x = symbols('x')
print(f'корни уравнения: {solve (5*x**2+10*x-30 == 0, x)}')
print(f'промежутки, на которых f>0: {solve (5*x**2+10*x-30 > 0, x)}')
print(f'промежутки, на которых f<0: {solve (5*x**2+10*x-30 < 0, x)}')
ans = diff(5*x**2+10*x-30 == 0, x)
print(f'вершина ф-ии: {solve (ans)}')
ans1 = diff(5*x**2+10*x-30 > 0, x)
print(f'промежутки, на которых ф-я возрастает: {solve (ans1)}')
ans2 = diff(5*x**2+10*x-30 < 0, x)
print(f'промежутки, на которых ф-я убывает: {solve (ans2)}')
print(plot(5*x**2+10*x-30))
