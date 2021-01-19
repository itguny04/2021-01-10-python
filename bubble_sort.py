
import random
import time
a = []

for i in range(10001):
    a.append(random.randint(1, 1000))

t1 = time.time()

for i in range(len(a)-1, 0, -1):
    for j in range(0, i, 1):
        if(a[j]<a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]

t2 = time.time()

for i in a:
    print(i, end=' ')

print('\n%.2fs'%(t2-t1))

