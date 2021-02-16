import random
import numpy as np
import matplotlib.pyplot as plt

num_city = 100
num_air = 3
num_center = 5
sigma = 0.1
alpha = 0.002
cities = set()
airports = []
city_groups = []


def generate_city_groups():
    city_groups.clear()
    temp = [(city[0], city[1], 0) for city in cities]
    for i in range(len(airports)): #1-3
        for j in range(len(temp)): #temp 33?
            temp[i] = (temp[i][0], temp[i][1], np.linalg.norm(np.array(airports[i]) - np.array((temp[i][0], temp[i][1]))))
        temp.sort(key=lambda tup: tup[2])
        city_groups.append([(cord[0], cord[1]) for cord in temp[0:33]])
        temp = temp[33:]

#for each city, find the clsest, then add the current city to the corresponding airport group by comparing them to all three airport distances
#finding minimum euclidian distance then add city to set

def objective_function():
    obj = 0
    cx = [cord[0] for cord in cities]
    cy = [cord[1] for cord in cities]
    for i in range(len(airports)):
        for j in range(len(cities)):
            obj += (airports[i][0] - cx[j]) ** 2 + (airports[i][1] - cy[j]) ** 2
    # print(obj)
    return obj


# i - the index of the airport or city group
# j - is the x or y component. 0 = x and 1 = y
def gradient(i, j):
    grad = 0
    for cord in city_groups[i]:
        grad += airports[i][j] - cord[j]
        # print(2*grad)
    return 2 * grad


for i in range(num_center):
    x = random.random()
    y = random.random()
    xc = np.random.normal(x, sigma, num_city // num_center)
    yc = np.random.normal(y, sigma, num_city // num_center)
    cities = cities.union(zip(xc, yc))

for i in range(num_air):
    x = random.random()
    y = random.random()
    airports.append((x, y))

generate_city_groups()
for z in range(100):
    # print([cord[0] for cord in airports])
    for i in range(len(airports)):
        x = airports[i][0] - alpha * gradient(i, 0)
        y = airports[i][1] - alpha * gradient(i, 1)
        airports[i] = (x, y)
    print(airports)
    print(objective_function())

zip_cities = zip(*cities)
plt.scatter(*zip_cities, marker='+', color='b', label='Cities')
zip_airs = zip(*airports)
plt.scatter(*zip_airs, marker='*', color='r', s=100, label='Airports')
plt.legend()
plt.show()