a = int(input())
b = int(input())
n = int(input())
cost = a * 100 + b
cost = cost * n

print(cost // 100, cost % 100)
