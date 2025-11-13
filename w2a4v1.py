# Đọc 6 điểm số từ một dòng, chuyển đổi thành số thực và gán vào các biến
a1, b1, c1, a2, b2, a3 = map(float, input().split())

# Tính điểm trung bình (TB) theo công thức:
# TB = ( (a1+b1+c1)*1 + (a2+b2)*2 + a3*3 ) / 10
average = (a1 + b1 + c1 + (a2 + b2) * 2 + a3 * 3) / 10

# In kết quả, làm tròn và lấy 1 chữ số thập phân
print("{average:.1}")