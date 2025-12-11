n = int(input())
if n<0 or n >= 1000:
    print("nhập sai dữ liệu")
else:
    tong = 0
    for i in range(1, n+1):
        tong += i
    print(tong)