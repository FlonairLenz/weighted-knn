import matplotlib.pyplot as plt
import random
import knn_algorithm as knn

random.seed(200)

points = []
for i in range(700):  
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)

    label = "#177ACC"
    if x < 4 and y >= 3: label = "#E8B542"
    if x >= 4 and y >= 3: label = "#BF0001"
    if x >= 4 and y < 3: label = "#04CA95"

    points.append(knn.DataPoint([x, y], label))

x, y, l = zip(*points)
plt.scatter(x, y, color=l)

pred = []
for i in range(300):  
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    pred.append(knn.DataPoint([x, y]))

for p in pred:
    p.label = knn.knn(5, p, points)

x, y, l = zip(*pred)
plt.scatter(x, y, color=l, s = 100, marker = "D")

plt.show()
