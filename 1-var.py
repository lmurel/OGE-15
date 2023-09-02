num = int(input())
k = 0
for _ in range(num):
    x = int(input())
    if x % 2 != 0 and x % 10 != 1:
        k += 1
print(k)