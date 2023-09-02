num = int(input())
summa = 0
count = 0
for _ in range(num):
    x = int(input())
    if x % 10 == 3 or x % 10 == 7:
        summa += x
        count += 1
print(summa/count)