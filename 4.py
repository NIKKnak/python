# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# a = list(map(int, input().split()))
# print(min(a),max(a))


# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения (D = b^2-4ac, x1 = (-b+/- sqtr(D))/a)
# 2) с помощью дополнительных библиотек Python(sympy, scipy)(Дополнительно)

# import math

# a = int(input())
# b = int(input())
# c = int(input())


# D = b**2-4*a*c
# print(D)
# if D > 0:
#     x1 = (-b + (math.sqrt(D))/(2*a))
#     print(x1)
#     x2 = (-b - (math.sqrt(D))/(2*a))
#     print(x2)
# elif D == 0:
#     x1 = -b/(2*a)
#     print(x1)
# else:
#     print("корней нет")


# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Пример:
# 4, 5 -> 20
# 4,6 -> 12



# a,b = int(map(input().split()))

# a = int(input())
# b = int(input())

# if a < b:
#     i = a
#     while i <= b:
#         if i % a == 0 and i % b == 0:
#             print(i)
#         elif i % a != 0 and i % b != 0:
#             print(a * b)
#         i += 1

# elif b < a:
#     j = b
#     while j <= a:
#         if j % b == 0 and j % a == 0:
#             print(j)
#         elif j % b != 0 and j % a != 0:
#             print(a * b)
#         j += 1

# elif a == b:
#     print(a)


def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)


    
a, b = map(int, input().split())
print(a*b//gcd(a,b))
