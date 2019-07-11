# 1. bubble sort

def exchange(data, des):
    data_len = len(data)
    for i in range(des-1):
        temp = 0
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
        else:
            continue
    return data

def bubble_sort(data):
    count = len(data)
    while True:
        exchange(data, count)
        count-=1
        if count==1:
            break
    return data    
import random
a = bubble_sort(random.sample(range(1,100), 30))
print(a)

