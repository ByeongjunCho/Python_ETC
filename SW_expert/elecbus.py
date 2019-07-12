import time
start = time.time()
K, N, M = 5, 40, 8
elec_supply = [3, 8, 11, 16, 18, 23, 28, 33]
# temp = [x for x in a if b >= x]
test_case = 1
bus_loc = 0
sup_num = 0


while True:
        bus_loc += K
        if bus_loc >= N:
            break
        temp = [x for x in elec_supply if bus_loc >= x]
        if len(temp) == 1:
            bus_loc = temp[-1]
            sup_num += 1
            del(elec_supply[0])
        elif len(temp):
            bus_loc = temp[-1]
            sup_num += 1
            del(elec_supply[:len(temp)])
        else:
            sup_num = 0
            break
print(f'#{test_case} {sup_num}')
print(temp)
print(time.time() - start)