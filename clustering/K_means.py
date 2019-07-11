# k-means
# Reference
# kaggle => https://www.kaggle.com/andyxie/k-means-clustering-implementation-in-python
# scikit-learn => https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-auto-examples-cluster-plot-kmeans-assumptions-py
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
# 0. load iris dataset
# iris는 3가지 종류가 있다.
iris = datasets.load_iris()
x = iris.data[:, 0:2]
y = iris.target

# print(np.shape(x))
# print(np.shape(y))

# 1. Non use scikit-learn

# Number of clusters 
k = 3
# Number of training data
n = x.shape[0]

# Number of features in the data
c = x.shape[1]

# 무작위 중심점을 구한다. 여기서는 평균과 분산을 기준으로 구했다.
mean = np.mean(x, axis=0)
std = np.std(x, axis=0)
centers = np.random.randn(k,c) * std + mean # [3, 2] 크기의 행렬 생성

centers_old = np.zeros(centers.shape)  # 오차 계산을 위해 기존 센터값을 저장하는 변수
centers_new = deepcopy(centers)  # 새롭게 생성된 중심값

# 각 center와 데이터간의 거리를 계산하기 위해 새로운 변수들을 생성한다.
clusters = np.zeros(n)  # training data의 개수만큼 영행렬 생성, 
                        # 초기분할행렬로 데이터의 개수만큼 생성한다.
distances = np.zeros((n,k)) # 중심점과 데이터 사이의 거리값 계산을 위한 행렬

error = np.linalg.norm(centers_new - centers_old)  # 여기서 error값은 norm으로 한다. 

while error != 0:
    for i in range(k):
        # 내가 정한 센터값과 데이터간의 거리를 저장한다.
        distances[:,i] = np.linalg.norm(x - centers[i], axis=1)
    # 거리를 계산하고 여기서 가장 큰 있는 인덱스를 출력한다.
    clusters = np.argmin(distances, axis = 1)
    
    centers_old = deepcopy(centers_new)
    # Calculate mean for every cluster and update the center
    for i in range(k):
        centers_new[i] = np.mean(x[clusters == i], axis=0)
    error = np.linalg.norm(centers_new - centers_old)
    # error가 일정값 이상 감소하면 루프를 종료한다. 
print(centers_new)
plt.subplot(211)
plt.scatter(x[:,0], x[:,1], c=y, s=7)
plt.scatter(centers_new[:,0], centers_new[:,1], marker='*', c='g', s=150)
plt.title("non scikit-learn")

# 2. using scikit-learn 이게 좋다.
from sklearn.cluster import KMeans

y_pred = KMeans(n_clusters=3, random_state=170).fit_predict(x)

plt.subplot(212)
plt.scatter(x[:,0], x[:,1], c=y_pred, s=7)
plt.scatter(centers_new[:,0], centers_new[:,1], marker='*', c='g', s=150)
plt.title("scikit-learn")
plt.show()