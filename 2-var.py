maximum = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x < 1000 and x > maximum:
        maximum = x
print(maximum)