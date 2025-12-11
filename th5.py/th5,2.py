# Nhập vào một số nguyên dương n. Tính tổng các chữ số của n mà là số nguyên tố.
def tinhtongchusocuasnt(n :int) -> int :
    tong = 0
    while n > 0 :
        if n % 10 == 2 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7 :
            tong += n % 10
        n //= 10
    return tong
n = int(input())
print(tinhtongchusocuasnt(n))
