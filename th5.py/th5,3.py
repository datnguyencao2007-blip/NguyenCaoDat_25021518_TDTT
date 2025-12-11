# nhập vào 1 chuỗi gồm cả chữ và số, tính tổng các chữ số có trong chuỗi đó
str = input()
for ch in str :
    if ch.isalpha() :
        str = str.replace(ch, ' ')
    print(str)