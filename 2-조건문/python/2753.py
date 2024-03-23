a=int(input())
print(1 if a % 4 == 0 and a % 100 != 0 else (1 if a % 400 == 0 else 0))