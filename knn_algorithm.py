function weight():
    pass

function distance(x_i, x_j):
    pass

function knn(x_i, data):
    pass

#function
#distance(x_i, x_j)
#d = 0
#foreach
#property in x_i
#s = (x_i.property - x_j.property) ** 2
#d += s

#return d ** (1 / 2)

#function
#knn(x_i, points)
#k_nearest = []
#foreach
#x_j in points
#d_j = distance(x_i, x_j)
#if d_j < max(d(k_nearest))
#    replace
#    max(k_nearest)
#    with x_j

#category = {}
#foreach
#nearest in k_nearest
#category[nearest] += 1

#return max(category)