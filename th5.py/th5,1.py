# Kiểm tra số nguyên tố và in ra các số nguyên tố nhỏ hơn nó
import math
def kiemtrasonguyento(n:int) -> bool :
    if n < 2 :
        return False
    for i in range(2, math.isqrt(n) + 1) :
        if n % i == 0 :
            return False
    return True
n = int(input())
for i in range(2, n+1) :
    if kiemtrasonguyento(i) :
        print(i, end = ' ') 
