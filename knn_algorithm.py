class DataPoint:
    def __init__(self, features, label):
        self.features = features
        self.label = label

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

def weight(d_j):
    return 1 / d_j

def distance(x_i, x_j):
    return sum([(x_i.features[i] - x_j.features[i]) ** 2 for i in range(len(x_i.features))]) ** 1 / 2 

def knn(k, x_i, dataPoints):
    knearest = []
    for x_j in dataPoints:
        d_j = distance(x_i, x_j)
        wd_j = weigth(d_j)
        x_j.setDistance(wd_j)

        if len(knearest) < k:
            knearest.append(x_j)
        elif wd_j < knearest[-1].getDistance():
            knearest[-1] = x_j
            knearest.sort(key = lambda x: x.distance)

    labels = {}
    nearest = (None, 0)
    for neighbor in knearest:
        if neighbor.label in labels: labels[neighbor] += neighbor.distance
        else: labels[neighbor] = neighbor.distance

        if labels[neighbor] > nearest[1]:
            nearest = (neighbor, labels[neighbor])
    
    return nearest[0]
