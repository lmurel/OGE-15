print(min(filter(
    lambda x: x % 2 == 0 and 10 <= x <= 99,
    [int(input()) for _ in range(int(input()))]
)))