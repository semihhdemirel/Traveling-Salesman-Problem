# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-


import numpy as np
import random
import math

#distances between provinces
distance=np.array([[0,113,148,216,453,178,244,248,323,354],[113,0,37,106,342,65,131,137,213,244],[148,37,0,68,305,103,157,100,176,206],[216,106,68,0,237,171,225,168,244,275],[453,342,305,237,0,407,385,314,234,312],[178,65,103,171,407,0,69,124,219,250],[244,131,157,225,385,69,0,95,152,182],[248,137,100,168,314,124,95,0,80,111],[323,213,176,244,234,219,152,80,0,79],[354,244,206,275,312,250,182,111,79,0]])
#initial pheromone amount
pheromone=np.array([[0,1,1,1,1,1,1,1,1,1],[1,0,1,1,1,1,1,1,1,1],[1,1,0,1,1,1,1,1,1,1],[1,1,1,0,1,1,1,1,1,1],[1,1,1,1,0,1,1,1,1,1],[1,1,1,1,1,0,1,1,1,1],[1,1,1,1,1,1,0,1,1,1],[1,1,1,1,1,1,1,0,1,1],[1,1,1,1,1,1,1,1,0,1],[1,1,1,1,1,1,1,1,1,0]])
p=0.5#pheromone evaporation rate
alfa=1
beta=3


#The following loop calculates the 1/distance.
dij=np.zeros((10,10))
for i in range(0,10):
    for j in range(0,10):
        if distance[i,j]==0:
            dij[i,j]=0
        else:
            dij[i,j]=1/distance[i,j]
            

#initial random route            
route=np.array([[0,7,3,4,2,1,9,6,8,5,0],[0,9,5,4,3,1,8,2,7,6,0],[0,2,6,9,7,4,8,1,3,5,0],[0,9,6,5,4,3,2,1,8,7,0],[0,6,5,4,1,8,2,9,3,7,0],[0,1,4,2,9,8,7,3,6,5,0],[0,7,1,8,5,6,9,2,3,4,0],[0,9,6,5,2,8,4,3,7,1,0],[0,8,3,1,2,4,6,9,7,5,0],[0,2,7,5,8,1,3,4,9,6,0]])


pheromone1=np.zeros((10,10))
possible_path=np.zeros((45,2))
pheromone2=np.zeros((10,10))
k=0
#The following loop find out possible paths.
for i in range(0,10):
    for j in range(0,10):
        if j>i:
            possible_path[k,0]=i
            possible_path[k,1]=j
            k=k+1


#The following loop calculates the sum of distances. 
           
first_total=np.zeros((10,1))
for i in range(0,10):
    for j in range(0,10):
        first_total[i,0]=first_total[i,0]+distance[route[i,j],route[i,j+1]]          
            
t=0
while(t<50):
    
    
    total=np.zeros((10,1))
    #Sum of the distances
    for i in range(0,10):
        for j in range(0,10):
            total[i,0]=total[i,0]+distance[route[i,j],route[i,j+1]]
    
    #initial pheromone amounts multiplyed by p-1.        
    for i in range(0,10):
        for j in range(0,10):
            if j>i:
                pheromone1[i,j]=pheromone[i,j]*(1-p)
    
    #pheromone amounts are updated by taking into account routes.
    for i in range(0,10):              
            j=0
            k=0
            while(k<10):
                x=route[i,j]
                y=route[i,j+1]
                if x>y:
                    pheromone1[y,x]=(pheromone1[y,x]+pheromone2[y,x]+1/total[i,0])
                else:
                    pheromone1[x,y]=(pheromone1[x,y]+pheromone2[x,y]+1/total[i,0])
                k=k+1
                j=j+1
    
 
    for i in range(0,10):
        j=0
        k=0
        while(k<10):
            x=route[i,j]
            y=route[i,j+1]
            if x>y:
                pheromone2[y,x]=pheromone2[y,x]+1/total[i,0]
            else:
                pheromone2[x,y]=pheromone2[x,y]+1/total[i,0]
            k=k+1
            j=j+1
    
    #Probabilities are calculated.
    Pij=np.zeros((10,10))    
    for i in range(0,10):
        for j in range(0,10):
            if j>i:
                Pij[i,j]=pheromone1[i,j]*math.pow(dij[i,j],3) 
    
    for i in range(0,10):
        for j in range(0,10):
            if i>j:
                Pij[i,j]=Pij[j,i]
    
    total_probabilities=np.zeros((10,1))
    for i in range(0,10):
        for j in range(0,10):
            total_probabilities[i,0]=total_probabilities[i,0]+Pij[i,j]
    PijSon=np.zeros((10,10))
    for i in range(0,10):
        for j in range(0,10):
            PijSon[i,j]=Pij[i,j]/total_probabilities[i,0]        
    
    
    #Sum of each rows have to be calculated as 1.
    total1=np.zeros((10,1))
    for i in range(0,10):
        for j in range(0,10):
            total1[i,0]=total1[i,0]+PijSon[i,j]     
    
    
    #Cumulative is calculated.     
    cumulative=np.zeros((10,10))
    for i in range(0,10):
        cumulative[i,0]=PijSon[i,0]        
            
    for i in range(0,10):
        for j in range(1,10):
            cumulative[i,j]=PijSon[i,j]+cumulative[i,j-1]        
    
    
    #Random numbers are returned. New routes will be determined according to random numbers.
    random_numbers=np.zeros((1,10))
    for i in range(0,10):
        random_numbers[0,i]=random.random()    
    
    new_route=np.zeros((10,11))
    path=np.zeros((10,10))       
    a=np.zeros((1,10)) 
      
    #The new routes determined with random numbers using cumulative values.
    
    for z in range(0,10):
        for i in range(1,10):
            while(new_route[z,i]==0):
                for k in range(0,10):
                    random_numbers[0,k]=random.random()
                for j in range(0,9):
                    x=int(a[0,z])
                    if random_numbers[0,z]>cumulative[x,j] and random_numbers[0,z]<cumulative[x,j+1]:
                        if path[z,j+1]==0:
                            new_route[z,i]=j+1
                            path[z,j+1]=1
                            x=j+1
                            break
                        else:
                            for k in range(0,10):
                                random_numbers[0,k]=random.random()
    
    #The last sum of the distances are calculated.
    last_total_distances=np.zeros((10,1))
    for i in range(0,10):
         for j in range(0,10):
             last_total_distances[i,0]=last_total_distances[i,0]+distance[int(new_route[i,j]),int(new_route[i,j+1])]
    
    #The route and the pheromones are updated for next loop.
    route1=new_route.copy()
    route=route1.astype(int)
    pheromone=pheromone1.copy()
    t=t+1

     

