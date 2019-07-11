import collections
import matplotlib.pyplot as plt

num_friends = [100,40,30,30,30,30,30,30,30,30,54,54,54,54,54,54,54,54,25,3,100,100,100,3,3]

friend_counts = collections.Counter(num_friends)
print('friends:', friend_counts)

# 가시화 추가

xs = range(101)
ys = [friend_counts[x] for x in xs]  # friend_counts는 dictionary로 구성되어 있음

plt.bar(xs, ys)  # plt 막대 그래프 그리기
plt.axis([0, 101, 0, 25])
plt.xlabel("# for friends")
plt.ylabel("# of people")
plt.show()

# 가장 많은/적은 친구 수 찾기
num_friends = [100,40,30,30,30,30,30,30,30,30,54,54,54,54,54,54,54,54,25,3,100,100,100,3,3]
num_points = len(num_friends)
print(num_points)

max_value = max(num_friends)
min_value = min(num_friends)

# 평균 친구 수 구하기
def mean(x):
    return sum(x) / len(x)

avgOfFriends = mean(num_friends)
print(f'평균 친구 = {avgOfFriends}')

# 중앙값(median)구하기
def median(v):
    n = len(v)
    sorted_v = sorted(v) # 정렬
    midpoint = n // 2

    if midpoint%1 == 1: # 리스트가 홀수면 가운데 값
        return sorted_v(midpoint)
    else: # 짝수면 가운데 2개 값의 평균
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print(f"중앙값 = {median(num_friends)}")

# 최대, 최소 사이의 범위
def data_range(x):
    return max(x) - min(x)

print(f'최대 - 최소 = {data_range(num_friends)}')

# 이상치를 제외한 데이터 사이의 범위 차이
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def interquartile_range(x):
    return quantile(x, 0.75) * quantile(x, 0.25)

