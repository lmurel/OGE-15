print(sum(filter(
    lambda x: x % 3 == 0 or x % 5 == 0,
    [int(input()) for _ in range(int(input()))]
)))