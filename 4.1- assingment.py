x = 5
y = 10
z = 20

x, y, z = 5, 16, 20

x, y = y, x

#Bazı işlemler
# x += 5          # x = x + 5
# x -= 5          # x = x - 5
# x *= 5          # x = x * 5
# x /= 5          # x = x / 5
# x %= 5          # x = x % 5
# y //= 5         # y = y // 5
# y **= z         # y = y ** z


values = 1, 2, 3, 4, 5
values1 = 1, 2, 3

print(values)
print(type(values))

x, y, *z = values     # * sayesinde en sondaki z ye ne kadar atanacak şey varsa atanır
x1, y1, z1 = values1

print(x, y, z)
print(x, y, z[1])
print(x1, y1, z1)