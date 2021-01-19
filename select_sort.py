import random
import time
a = []

for i in range(10001):
    a.append(random.randint(1, 1000))

t1 = time.time()

for i in range(0, len(a), 1):
    max = i
    for j in range(i+1, len(a), 1):
        if(a[j]>a[max]):
            a[j], a[max] = a[max], a[j]

t2 = time.time()

for i in a:
    print(i, end=' ')

print('\n%.2fs'%(t2-t1))

