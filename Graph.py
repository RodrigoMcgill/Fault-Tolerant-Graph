import matplotlib.pyplot as plt
import networkx as nx
import operator
import os


G = nx.Graph()

#Draw a node given the |Graph 'G'|node|position|
def draw_node(G, node,x,y):
    G.add_node(node, id=node, position=(x,y))

#Draw a edge given the |Graph 'G'|source node|target node|reliability|
def draw_edge(G,source,target,r):
    G.add_edge(source, target, r=r)

#Automatically draws and plots the graph G
def draw_graph(G):
    pos = nx.get_node_attributes(G, 'position')
    nx.draw(G, pos, node_size=2000, node_color='black')
    node_labels = nx.get_node_attributes(G, 'id')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='w')
    edge_labels = nx.get_edge_attributes(G, 'id')
    nx.draw_networkx_edge_labels(G, pos, labels=edge_labels)
    plt.show()

#Obtain all simple paths between source node and target node
def modify_djikstra(G, source, target):
      paths =list(nx.all_simple_paths(G, source=source, target=target))
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

def clear():
    cls = '\n'*50
    print(cls)

#Create nodes and edges
def arguments():
    done = 'yes'
    while done == 'yes':
        name, x,y = input("Create a node [name of node] [position x] [position y] \n").split(' ')
        draw_node(G, name,int(x),int(y))
        done = input("continue?: [yes] [no] \n")
        if done !='no':
            if done !='yes':
                done = 'yes'
        clear()
    done = 'yes'
    while done == 'yes':
        print("This is a list of all nodes")
        print(G.nodes(data=False))
        source, target, r = input("Which nodes you want to connect and what's the reliability [Source] [Target] [Reliability] \n").split(' ')
        draw_edge(G,source,target,r)
        done = input("continue?: [yes] [no] \n")
        clear()


def main():
    arguments()
    draw_graph(G)


main()


"""


x,y= input("fff \n").split(' ')
name= input("enter for x \n")
G.add_node(name, id=name, position=(int(x),int(y)))
G.add_node('V', id='V', position= (2,2))
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

draw_graph(G)


path_sorted,reliabilities_sorted = modify_djikstra(G,'U','Z')
print("path sorted \n:" + str(path_sorted)+ "\n reliabilities sorted" + str(reliabilities_sorted))
"""