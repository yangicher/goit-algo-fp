import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        #add node with color and label
        graph.add_node(node.id, color=node.color, label=node.val)
        
        #add left edges
        if node.left:
            graph.add_edge(node.id, node.left.id)
            new_x_left = x - 1 / 2 ** layer
            pos[node.left.id] = (new_x_left, y - 1)
            add_edges(graph, node.left, pos, x=new_x_left, y=y - 1, layer=layer + 1)
        
        #add right edges
        if node.right:
            graph.add_edge(node.id, node.right.id)
            new_x_right = x + 1 / 2 ** layer
            pos[node.right.id] = (new_x_right, y - 1)
            add_edges(graph, node.right, pos, x=new_x_right, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, algorithm_name=None):
    plt.clf()  #clear before draw
    
    if algorithm_name:
        plt.gcf().canvas.manager.set_window_title(algorithm_name)
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)} #pos
    tree = add_edges(tree, tree_root, pos)
    
    colors = [data['color'] for node_id, data in tree.nodes(data=True)]
    labels = {node_id: data['label'] for node_id, data in tree.nodes(data=True)}
    
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.draw()

def main():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    
    draw_tree(root)
    plt.show()

if __name__ == "__main__":
    main()