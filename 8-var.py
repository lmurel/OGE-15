x = int(input())
summa = 0
count = 0
while x != 0:
    if x % 2 != 0 and x > 100:
        summa += x
        count += 1
    x = int(input())
print(round(summa/count))