k = int(input())
l = int(input())
m = int(input())
n = int(input())
first = (k + l) % 2
second = (m + n) % 2
if first == second:
    print("YES")
else:
    print("NO")
