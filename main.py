#todo try to fix triangle graph bug

# Import pandas
import pandas as pd
import matplotlib.pyplot as graph
import sys

# Bypassing recursion limit
sys.setrecursionlimit(2975)

# 2d list sort
def list_sort(list,d):
    j=0
    for i in range(0,len(d)):
        if list[i][0] == list[0][0] or list[i][0] > list[j][0]:
            j = i
            continue
        if list[i][0] < list[j][0]:
            list[i],list[j] = list[j],list[i]
            list_sort(list,d)
# list maker
def make_list(list,d1,d2):
    for i in range(0,len(d1)):
        list.append([d1[i],d2[i]])
# list extractor
def extract_list(lst,index):
    return [item[index] for item in lst]

# converting to dataframe
data =  pd.read_csv("gravity_data.csv")

mass = data["Mass"].to_list()
radius = data["Radius"].to_list()
gravity = data["Gravity"].to_list()

mr = []
mg = []
rg = []

make_list(mr, mass, radius)
make_list(mg, mass, gravity)
make_list(rg, radius, gravity)

# 2d argument does not matter here
list_sort(mr,radius)
list_sort(mg,gravity)
list_sort(rg,mass)

#mass vs radius (scatter)
graph.subplot(2,3,1)
graph.plot(extract_list(mr,0),extract_list(mr,1),'.')
graph.title("Mass v/s Radius")
graph.xlabel("Mass")
graph.ylabel("Radius")
graph.grid(color = 'green', linestyle = '--')

#mass vs gravity (scatter)
graph.subplot(2,3,2)
graph.plot(extract_list(mg,0),extract_list(mg,1),'.')
graph.title("Mass v/s Gravity")
graph.xlabel("Mass")
graph.ylabel("Gravity")
graph.grid(color = 'green', linestyle = '--')

#radius vs gravity (scatter)
graph.subplot(2,3,3)
graph.plot(extract_list(rg,0),extract_list(rg,1),'.')
graph.title("Radius v/s Gravity")
graph.xlabel("Radius")
graph.ylabel("Gravity")
graph.grid(color = 'green', linestyle = '--')

#mass vs radius (line)
graph.subplot(2,3,4)
graph.plot(extract_list(mr,0),extract_list(mr,1),linewidth = '0.5')
graph.xlabel("Mass")
graph.ylabel("Radius")
graph.grid(color = 'green', linestyle = '--')

#mass vs gravity (line)
graph.subplot(2,3,5)
graph.plot(extract_list(mg,0),extract_list(mg,1),linewidth = '0.5')
graph.xlabel("Mass")
graph.ylabel("Gravity")
graph.grid(color = 'green', linestyle = '--')

#radius vs gravity (line)
graph.subplot(2,3,6)
graph.plot(extract_list(rg,0),extract_list(rg,1),linewidth = '0.5')
graph.xlabel("Radius")
graph.ylabel("Gravity")
graph.grid(color = 'green', linestyle = '--')

graph.suptitle("Planet Plot Chart")
graph.show()