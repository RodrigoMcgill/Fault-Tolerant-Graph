
import matplotlib.pyplot as plt
import networkx as nx
import operator
import os
import time
import pandas as pd
import _thread
import warnings
import random


warnings.filterwarnings("ignore")
G = nx.Graph()

def clear():
    cls = '\n' * 3
    print(cls)

# Draw a node given the |Graph 'G'|node|position|
def draw_node(G, node, x, y):
    G.add_node(node, id=node, position=(x, y))


# Draw a edge given the |Graph 'G'|source node|target node|reliability|
def draw_edge(G, source, target, r, color,width):
    G.add_edge(source, target,r=r, color=color,width=width)



# Automatically draws and plots the graph G
def draw_graph(G):
    pos = nx.get_node_attributes(G, 'position')
    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]
    nx.draw(G, pos, node_size=2000, node_color='black', edges=edges, edge_color=colors)
    node_labels = nx.get_node_attributes(G, 'id')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='w')
    labels = nx.get_edge_attributes(G, 'r')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


#changing the reliability of an edge
def change_rel(source,target,new_weight):
    G[source][target]['r'] = new_weight


# Obtain all simple paths between source node and target node
def modify_djikstra(G, source, target):
    paths = list(nx.all_simple_paths(G, source=source, target=target))
    reliabilities = []
    for p in paths:
        tolRel = 1
        for i in range(len(p) - 1):
            tolRel = tolRel * float(G[p[i]][p[i + 1]]['r'])
        reliabilities.append(tolRel)
    path_sorted = []
    reliabilities_sorted = []
    for i in range(len(reliabilities)):
        index, value = max(enumerate(reliabilities), key=operator.itemgetter(1))
        path_sorted.append(paths[index])
        reliabilities_sorted.append(value)
        del paths[index]
        del reliabilities[index]
    return path_sorted, reliabilities_sorted

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
        except:
            print('Oops, an error occurred, please try again \n')
    done = 'yes'
    while done == 'yes':
        try:
            print("This is a list of all nodes")
            print(G.nodes(data=False))
            source, target, r = input("Which nodes you want to connect and what's the reliability [Source] [Target] [Reliability] \n").split(' ')
            draw_edge(G, source, target, r,'k',2)
            done = input("continue?: [yes] [no] \n")
            if done != 'no':
                if done != 'yes':
                    done = 'yes'
        except:
            print('Oops, an error occurred, please try again \n')
    print('Here is your customized graph...')
    time.sleep(1)
    draw_graph(G)
    time.sleep(1)
    Fault_Tolerant_G(G)


def Fault_Tolerant_G(G):

    while True:
        try:
            source, target = input('choose two nodes for message transmission [target] [source] \n').split(' ')
            paths_sorted, reliabilities_sorted = modify_djikstra(G, source, target)
            break
        except Exception as e:
            print(e)

    first_list = paths_sorted[0]
    for i in range(len(first_list) - 1):  # changes the width color and size to green
        G[first_list[i]][first_list[i + 1]]['color'] = 'w'
        G[first_list[i]][first_list[i + 1]]['width'] = 9
    plt.title('Rel =' + str(reliabilities_sorted[0]))
    draw_graph(G)

    sending_message(G,paths_sorted,reliabilities_sorted)


 #sending message
def sending_message(G,paths_sorted,reliabilities_sorted):
    current_path = paths_sorted[0]
    print('message will be forwarded through the path given \n')

    for i in range(len(current_path)-1):
        tries = 3
        while tries > 0:
            S = current_path[i]
            T = current_path[i+1]
            print('Attempts remaining  :' + str(tries) + '\n')
            prob = random_num(G[S][T]['r'])
            result = mess_animation(S,T,prob)
            if result == True:
                print('message reached node ' + T + '\n')
                break
            else:
                print('WARNING! message has failed to reach its destination. Error happened between node ' + S + '--' +  'T \n')
                time.sleep(2)
                tries = tries -1

    print('doneeeeeeeee')




#returns  TRUE or FALSE , the message did went through or did not
def random_num(edge_rel):
    return random.random() < float(edge_rel)

def mess_animation(source,target,condition):
    print(str(source)+  'm.................'+str(target)+'\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '.m................' + str(target)+'\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '..m...............' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '...m..............' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '.....m............' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '......m...........' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '.......m..........' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '........m.........' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '.........m........' + str(target) + '\n')
    clear()
    if condition == False:
        return False
    print(str(source) + '..........m.......' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '...........m......' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '............m.....' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '.............m....' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '..............m...' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '...............m..' + str(target) + '\n')
    time.sleep(0.25)
    print(str(source) + '................m.' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    print(str(source) + '.................m' + str(target) + '\n')
    time.sleep(0.25)
    clear()
    return True



#######...............................

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

# main method
def main():
    while True:
        select = input("Select mode of Operation [Prim or Djikstra] \n")
        if select == "Prim":
            prim_arguments()
        elif select == "Djikstra":
            Djikstra_arguments()
        else:
            print('Oops, there was an error in the input, please write correctly the method \n')

main()


