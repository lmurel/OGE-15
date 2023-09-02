x = int(input())
k = 0
while x != 0:
    if x % 2 == 0 and 100 <= x <= 999:
        k += 1
    x = int(input())
print(k)