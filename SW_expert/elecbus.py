# import time
# start = time.time()

# a = range(1,2015215)
# b = 3

# # temp = [x for x in a if b >= x]



# k=0
# while True:
#     if b>=a[k]:
#         k+=1
#     else:
#         break
# temp = a[:k]

# print(temp)
# print(time.time() - start)



bus_ride, bus_sta_num, supply_num = 5, 20, 5
bus_supply_list = [4, 7, 9, 14, 17]
bus_loc = 0
bus_elec_num = 0
# 1. bus를 bus_ride만큼 움직인다.

# 2. bus가 bus_ride만큼 움직였을 때, 그 장소가 supply_list에 있는지 확인한다. 

# 3. 만약 supply_list중 하나라면, 그 장소에서 충전한다.

# 4. 그렇지 않다면, bus_loc보다 작으면서 가장 가까운 bus_supply_list를 찾고, 그 장소를 bus_loc로 초기화한다.