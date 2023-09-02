print(max(filter(
    lambda x: x % 2 != 0 and 100 <= x <= 999,
    [int(input()) for _ in range(int(input()))]
)))