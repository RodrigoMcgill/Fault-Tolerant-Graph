# Fault-Tolerant-Graph
\The File Graph.py is the source code for our program and it needs to be compiled for the program to run. This program was developed in python 3.6.0 which isn't currently supported by Pyinstaller.

The libraries required for this program are listed below:
-Matplorlib.pyplot
-networkx
-operator
-pandas
-operator
-time
-warnings
-random
-sys

The program should run automatically after compiling.

The program will ask for a mode of operation, please select Prim or Djikstra

In Prim mode, the program will request an input .xlsx file and a method of optimization(select Cost or Reliability), make sure to input the file path if the input.xlsx is located else where.

In Djikstra mode the program will request manual input of the nodes and their location.
After the program will request manual edge selection between the given nodes, select source node, target node and reliability.
The program will then generate the graphs accordingly, and simulate the message transfer.