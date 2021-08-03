# Traveling Salesman Problem
Traveling Salesman Problem is the problem of finding the shortest path. 
In this problem, the starting point, the ending point and the distances between each points are certain. 
Various approaches have been proposed in the literature to solve the traveling salesman problem. 
One of the most popular approach to solve this problem is the Ant Colony Optimization Algorithm. 
In this repository, An Ant Colony Optimization Algorithm was proposed to solve Traveling Salesman Problem. 
The purpose of this algorithm is to find the shortest path by visiting each points.
<br><br>
## Ant Colony Optimization Algorithm
Ants can find the shortest route from the nest to the food. While moving, it deposits a compound called pheromone on the ground. 
It is more likely to take the route with a large amount of pheromones. 
More pheromones accumulate in the short path. Therefore, it prefers the shortest path.
<br><br>
## Solving Traveling Salesman Problem By Using Ant Colony Optimization Algorithm
In this algorithm, there are 10 provinces from Turkey. The starting and ending point was determined as Istanbul. 
<br>
All provinces is given below;
![GitHub Logo](/results/provinces.jpg)<br>
The distances between each province are taken from the website of the General Directorate of Highways. <br>
The distances between each province and initial routes of each ants are given in the aco_provinces.py
<br>
The Initial random routes of the ants and the total distance of these routes are given in the dataframe below;<br><br>
![GitHub Logo](/results/initial_routes.jpg)<br><br>
As seen in the dataframe above, the minimum total distance is 1764 km.
<br>
After running the aco.py, the new routes of ants and the new total distances are given in the dataframe below;
<br><br>
![GitHub Logo](/results/result.jpg)<br><br>
After running the algorithm, the minimum total distance is 1536 km.<br>
As a result, when the last value compared to first value, the last value lesser than the first value. 
A shorter route was obtained by using Ant Colony Optimization Algorithm.
