n = int(input())
a = n % 10
b = (n // 10) - (n // 100)*10
c = (n // 100) - (n // 1000)*10
d = n // 1000

print(a+b+c+d)
