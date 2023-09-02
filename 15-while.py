k = 0
while True:
    x = int(input())
    if x == 0:
        break
    if 1 <= x <= 9 and x % 3 == 0:
        k += 1
print(k)
