import matplotlib.pyplot as plt
import networkx as nx
import operator
from collections import defaultdict

# Automatically draws and plots the graph G
def draw_graph(G):
    pos = nx.get_node_attributes(G, 'position')
    nx.draw(G, pos, node_size=2000, node_color='black')
    node_labels = nx.get_node_attributes(G, 'id')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='w')
    edge_labels = nx.get_edge_attributes(G, 'id')
    nx.draw_networkx_edge_labels(G, pos, labels=edge_labels)
    plt.show()

# Define a graph
G = nx.Graph()
# Defines nodes
G.add_node('U', id='U', position=(0, 0))
G.add_node('V', id='V', position=(2, 2))
G.add_node('X', id='X', position=(2, -2))
G.add_node('W', id='W', position=(4, 2))
G.add_node('Y', id='Y', position=(4, -2))
G.add_node('Z', id='Z', position=(6, 0))
# Defines edges between nodes and their weights
G.add_edge('U', 'V', r=2)
G.add_edge('U', 'X', r=1)
G.add_edge('U', 'W', r=5)
G.add_edge('V', 'W', r=3)
G.add_edge('V', 'X', r=2)
G.add_edge('X', 'W', r=3)
G.add_edge('X', 'Y', r=1)
G.add_edge('W', 'Y', r=1)
G.add_edge('W', 'Z', r=5)
G.add_edge('Y', 'Z', r=3)
"""
draw_graph(G)
"""

def modify_djikstra(G, source, target):
      paths =list(nx.all_simple_paths(G, source="U", target="Z"))
      reliabilities = []
      for p in paths:
          tolRel=1
          for i in range(len(p)-1):
              tolRel = tolRel*G[p[i]][p[i+1]]['r']
          reliabilities.append(tolRel)
      path_sorted = []
      reliabilities_sorted= []

      for i in range(len(reliabilities)):
            index, value = max(enumerate(reliabilities), key=operator.itemgetter(1))
            print("index: "+str(index)+" value"+str(value))
            print(paths[index])
            path_sorted.append(paths[index])
            reliabilities_sorted.append(value)
            del paths[index]
            del reliabilities[index]
      return  path_sorted,reliabilities_sorted


path_sorted,reliabilities_sorted = modify_djikstra(G,'U','Z')
print("path sorted \n:" + str(path_sorted)+ "\n reliabilities sorted" + str(reliabilities_sorted))



"""
paths = list(nx.all_simple_paths(G, source="U", target="Z"))
a = paths[0]
print("printing first thing in list \n"+str(a))
print("length of a is \n"+str(len(a)))
print("obtaining weight of U-X \n"+str(G['U']['X']['r']))
print("calculating total reliability in that list \n")
rel = 1
for i in range(len(a)-1):
    rel = rel*G[a[i]][a[i+1]]['r']

print(rel)

"""
"""
mylist =[0.44,0.45,0.9,0.9]
index,value = max(enumerate(mylist),key=operator.itemgetter(1))

print("get max value \n"+str(value)+"\n get the index \n"+str(index))
del mylist[index]
print(mylist)
print("get max value \n"+str(value)+"\n get the index \n"+str(index))
index,value = max(enumerate(mylist),key=operator.itemgetter(1))
print("get max value \n"+str(value)+"\n get the index \n"+str(index))
del mylist[index]
print(mylist)
"""



