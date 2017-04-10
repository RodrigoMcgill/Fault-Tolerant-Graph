import matplotlib.pyplot as plt
import networkx as nx
import operator
import os
import pandas as pd

G = nx.Graph()


# Draw a node given the |Graph 'G'|node|position|
def draw_node(G, node, x, y):
    G.add_node(node, id=node, position=(x, y))


# Draw a edge given the |Graph 'G'|source node|target node|reliability|
def draw_edge(G, source, target, r):
    G.add_edge(source, target, r=r)


# Automatically draws and plots the graph G
def draw_graph(G):
    pos = nx.get_node_attributes(G, 'position')
    nx.draw(G, pos, node_size=2000, node_color='black')
    node_labels = nx.get_node_attributes(G, 'id')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='w')
    edge_labels = nx.get_edge_attributes(G,'id')
    nx.draw_networkx_edge_labels(G, pos, labels=edge_labels)
    plt.show()


# Obtain all simple paths between source node and target node
def modify_djikstra(G, source, target):
    paths = list(nx.all_simple_paths(G, source=source, target=target))
    reliabilities = []
    for p in paths:
        tolRel = 1
        for i in range(len(p) - 1):
            tolRel = tolRel * G[p[i]][p[i + 1]]['r']
        reliabilities.append(tolRel)
    path_sorted = []
    reliabilities_sorted = []
    for i in range(len(reliabilities)):
        index, value = max(enumerate(reliabilities), key=operator.itemgetter(1))
        print("index: " + str(index) + " value" + str(value))
        print(paths[index])
        path_sorted.append(paths[index])
        reliabilities_sorted.append(value)
        del paths[index]
        del reliabilities[index]
    return path_sorted, reliabilities_sorted


def clear():
    cls = '\n' * 5
    print(cls)


# Create nodes and edges
def Djikstra_arguments():
    done = 'yes'
    while done == 'yes':
        try:
            name, x, y = input("Create a node [name of node] [position x] [position y] \n").split(' ')
            draw_node(G, name, int(x), int(y))
            done = input("continue?: [yes] [no] \n")
            if done != 'no':
                if done != 'yes':
                    done = 'yes'
            clear()
        except:
            print('Oops, an error occurred, please try again \n')
    done = 'yes'
    while done == 'yes':
        try:
            print("This is a list of all nodes")
            print(G.nodes(data=False))
            source, target, r = input("Which nodes you want to connect and what's the reliability [Source] [Target] [Reliability] \n").split(' ')
            draw_edge(G, source, target, r)
            done = input("continue?: [yes] [no] \n")
            clear()
        except:
            print('Oops, an error occurred, please try again \n')


def prim_optimization(inp, mode):
    inp = pd.read_excel('Input.xlsx')

    if mode == "Cost":
        inp.sort_values('Cost', ascending=True, inplace=True)
        print(inp)
    else:
        inp.sort_values('Reliability', ascending=False, inplace=True)
        print(inp)

    for index, row in inp.iterrows():
        nameA = row['First Edge']
        nameB = row['Second Edge']

        G.add_node(nameA, id=nameA)
        G.add_node(nameB, id=nameB)
        if not nx.has_path(G, nameA, nameB):
            G.add_edge(nameA, nameB, r=row['Reliability'])


def prim_arguments():
    inp, mode = input(
        "Copy the Path of the excel file you would like to use, and the optimization parameter [Path] [Cost or Reliability]\n").split(
        ' ')
    prim_optimization(inp, mode)

    nx.draw_networkx(G)
    plt.show()


def main():
    while True:
        select = input("Select mode of Operation [Prim or Djikstra] \n")
        if select == "Prim":
            prim_arguments()
        elif select == "Djikstra":
            Djikstra_arguments()
            draw_graph(G)
        else:
            print('Oops, there was an error in the input, please write correctly the method \n')


main()

"""
x,y= input("fff \n").split(' ')
path_sorted,reliabilities_sorted = modify_djikstra(G,'U','Z')
print("path sorted \n:" + str(path_sorted)+ "\n reliabilities sorted" + str(reliabilities_sorted))
"""