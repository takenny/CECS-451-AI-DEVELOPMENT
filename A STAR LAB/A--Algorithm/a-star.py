import re
import math
import networkx as nx

class Node: #Arad, Craiova
        def __init__(self, name, neighbors, g, h, f, previous_cities):
            self.name = name
            self.f = f
            self.neighbors = neighbors
            self.g = g
            self.h = h
            self.previous_cities = previous_cities #added this to store previous cities already visited.


def a_star(self, start):
    #initializing this because i dont want it to be infinity so i can start somewhere.
    MAP[start].f = 0
    MAP[start].g = 0
    MAP[start].previous_cities = ""

    open_list = dict() #initialize open ditionary with node and f value
    closed_list = dict() #intilaize close list
    open_list.update({MAP[start].name: MAP[start].f}) #put startin node on the open list
    while open_list: #while open list is not empty
        #find node with the least f on open list call it q
        #access value from dictionary
        q = min(open_list, key=open_list.get) #finds min
        #print("Smallest Node ", q)
        #pop q off the open list
        open_list.pop(q)
        #generate q 8 successors and set their parents to q
        #look at nieghbors
        for neighbors in MAP[q].neighbors:
            g = MAP[q].g + MAP[q].neighbors[neighbors]  # g = q.g + distance btewtwen sucess or and q
            h = MAP[neighbors].h  # h = distance from goal to sucessor
            f = g + h  # f = succesor g + succesor h
            if(neighbors == "Bucharest"): #successor is goal stop search
                open_list = {} #cler open list
                MAP[neighbors].g = g #update values into nodes
                MAP[neighbors].f = f
                MAP[neighbors].previous_cities = q
                break #for debug

            #if node with the same position as sucecssor is in the open list which has a lwoer f than scuessorm,  skip the succesor
            elif(neighbors in open_list and f < MAP[neighbors].f):
                MAP[neighbors].f = f #updating values
                open_list[neighbors] = f
                MAP[neighbors].g = g
                MAP[neighbors].previous_cities = q

            #if node with the same position as succcessor is in the closed list which has a lower f than sccessor , skip this sucvesor, otherwise
            #add node to the open list
            elif(neighbors in closed_list and f < MAP[neighbors].f): #if conditions met, dont skip.
                MAP[neighbors].f = f
                MAP[neighbors].g = g
                MAP[neighbors].previous_cities = q
                open_list.update({neighbors:f}) #added node to open list

            else:
                open_list.update({neighbors:f})
                MAP[neighbors].f = f
                MAP[neighbors].g = g
                MAP[neighbors].previous_cities = q

        #push q on the closed list
        closed_list.update({q:MAP[q].f})
        bestRoute.append(q)
        #end while loop


print('Give us the Starting City')
start = input()
destination = "Bucharest"
bestRoute = []

#map is a dictionary here.
MAP = dict()
mapFile = open("map.txt", "r")

for mapLine in mapFile:
   # print(mapLine)
    mapLine = mapLine.split("-") #whatever in front of dash ooohhhh
    cityName = mapLine[0] #got city name
    # nodes = Node(mapLine[0],"",math.inf,math.inf,math.inf,"") #alg told me to set to inf to compare
    # print(mapLine)
    #print(cityName)
    neighbors = mapLine[1].split(',')
   # nodes = Node(cityName, neighbors,math.inf,math.inf,math.inf,"")

    #MAP[cityName] = cityName

#make dictionary to store neighborname and cost
    neighborNameAndCost = dict()
    for element in neighbors: #find element in neighbors
         neighborName = element[:element.find('(')]
         # print(neighborName)
         cost = int(element[element.find('(') + 1: element.find(')')]) #cost is not g
         #print(element)
         #print(cost)
         neighborNameAndCost.update({neighborName: cost}) #add to dictionary

    nodes = Node(cityName, neighborNameAndCost, math.inf,math.inf,math.inf, "") #add to node
    MAP.update({cityName: nodes}) #add node of neighbor names and cost to dictionary MAP
#Find H from using this stuff
HDistanceFile = open("distances.txt","r")

for line in HDistanceFile: #get line
    #look for start
    #extract numerical value and put into something
    mapLine = line.split("-")  # whatever in front of dash ooohhhh
    cityName = mapLine[0]
    h = re.findall(r'\d+', line)
    IntVar = int("".join(filter(str.isdigit, h)))
    #print(IntVar)
    #put h into node and f into node
    MAP[cityName].h = IntVar

#bestRoute.append(cityNameZ.neighbors)

#print(MAP)
#for nodes in MAP:
   # print(MAP[nodes].neighbors)
#Output for File
a_star(MAP, start)
print('From City: ' + start)
print('To City: Bucharest')
bestRoute.append('Bucharest')
print('Best route:', bestRoute)
print('Total distance: ' + str(MAP['Bucharest'].g)) #g is sum of distance travelled so far.


