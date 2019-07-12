import time
start = time.time()

a = range(1,2015215)
b = 3

# temp = [x for x in a if b >= x]



k=0
while True:
    if b>=a[k]:
        k+=1
    else:
        break
temp = a[:k]

print(temp)
print(time.time() - start)