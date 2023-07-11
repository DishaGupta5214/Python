#!/usr/bin/env python
# coding: utf-8

# # Travelling Salesman Using Hill Climbing approach

# In[18]:


import random

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength

def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(tsp, neighbours):
    bestRouteLength = routeLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength

def hillClimbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    return currentSolution, currentRouteLength

def main():
    tsp = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]

    print(hillClimbing(tsp))

if __name__ == "__main__":
    main()


# In[19]:


list(range(len(tsp)))


# In[20]:


tsp = [
       [0, 400, 500, 300],
       [400, 0, 300, 500],
       [500, 300, 0, 400],
       [300, 500, 400, 0]
   ]

import matplotlib.pyplot as plt
plt.plot(tsp,'--o')


# In[21]:


import matplotlib.pyplot as plt

# Create a list of TSP instances of varying sizes
tsp_instances = [
    [[0, 400, 500], [400, 0, 300], [500, 300, 0]],
    [[0, 400, 500, 300], [400, 0, 300, 500], [500, 300, 0, 400], [300, 500, 400, 0]],
    [[0, 5, 2, 7, 8], [5, 0, 6, 9, 4], [2, 6, 0, 3, 1], [7, 9, 3, 0, 6], [8, 4, 1, 6, 0]],
    [[0, 2, 9, 10, 7, 5], [2, 0, 4, 8, 11, 6], [9, 4, 0, 3, 8, 10], [10, 8, 3, 0, 7, 11], [7, 11, 8, 7, 0, 2], [5, 6, 10, 11, 2, 0]]
]

# Run hill climbing algorithm for each TSP instance and store the results
results = []
for tsp in tsp_instances:
    solution, length = hillClimbing(tsp)
    results.append((len(tsp), length))

# Create a line graph to compare the performance of hill climbing on different TSP instances
x_values = [result[0] for result in results]
y_values = [result[1] for result in results]
plt.plot(x_values, y_values)
plt.xlabel('Number of cities')
plt.ylabel('Total distance')
plt.title('Performance of Hill Climbing Algorithm on TSP')
plt.show()

# Create a scatter plot to visualize the solutions found by the algorithm for a single TSP instance
tsp = tsp_instances[1]
solution, length = hillClimbing(tsp)
x_values = [tsp[i][0] for i in solution]
y_values = [tsp[i][1] for i in solution]
plt.scatter(x_values, y_values)
for i, (x, y) in enumerate(zip(x_values, y_values)):
    plt.annotate(str(i), (x, y))
plt.plot(x_values + [x_values[0]], y_values + [y_values[0]])
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Solution Found by Hill Climbing Algorithm')
plt.show()


# In[ ]:




