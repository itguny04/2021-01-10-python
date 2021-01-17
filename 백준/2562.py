a = int(input())
b = int(input())
c = int(input())

d = [0 for i in range(1,10)]

number = a*b*c
int(number)

while number:
    d[number%10]+=1
    number //= 10

for i in d:
    print(i)