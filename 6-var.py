run = True
mini = 30_001
while run:
    x = int(input())
    if x == 0:
        break
    if x % 7 == 0 and x % 10 != 4 and x != 0 and x < mini:
        mini = x
print(mini)


