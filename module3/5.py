n = int(input())
sut = n//1440
hour = n//60 - sut
minute = n%60

print(hour, minute)
