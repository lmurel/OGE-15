x = int(input())
s = 0
while x != 0:
    if x % 3 == 0 and x % 5 != 0:
        s += x
    x = int(input())
print(s)