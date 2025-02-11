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
        graph.add_node(node.id, color=node.color, label=node.val)
        
        if node.left:
            graph.add_edge(node.id, node.left.id)
            new_x_left = x - 1 / 2 ** layer
            pos[node.left.id] = (new_x_left, y - 1)
            add_edges(graph, node.left, pos, x=new_x_left, y=y - 1, layer=layer + 1)
        
        if node.right:
            graph.add_edge(node.id, node.right.id)
            new_x_right = x + 1 / 2 ** layer
            pos[node.right.id] = (new_x_right, y - 1)
            add_edges(graph, node.right, pos, x=new_x_right, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, algorithm_name=None):
    plt.clf()
    
    if algorithm_name:
        plt.gcf().canvas.manager.set_window_title(algorithm_name)
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    colors = [data['color'] for node_id, data in tree.nodes(data=True)]
    labels = {node_id: data['label'] for node_id, data in tree.nodes(data=True)}
    
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.draw()
    plt.pause(1)  

def count_nodes(root):
    if not root:
        return 0
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        count += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count

def get_color(order, total, start_color=(0, 0, 139), end_color=(173, 216, 230)):
    if total <= 1:
        return f'#{start_color[0]:02X}{start_color[1]:02X}{start_color[2]:02X}'
    t = order / (total - 1)
    R = int(start_color[0] + (end_color[0] - start_color[0]) * t)
    G = int(start_color[1] + (end_color[1] - start_color[1]) * t)
    B = int(start_color[2] + (end_color[2] - start_color[2]) * t)
    return f'#{R:02X}{G:02X}{B:02X}'

def dfs_traversal(root):
    total = count_nodes(root)
    order = 0  
    stack = [root]
    
    while stack:
        node = stack.pop()
        node.color = get_color(order, total)
        order += 1
        
        draw_tree(root, algorithm_name="DFS")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def bfs_traversal(root):
    total = count_nodes(root)  
    order = 0  
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        node.color = get_color(order, total)
        order += 1
        
        draw_tree(root, algorithm_name="BFS")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def reset_tree_colors(root, default_color="skyblue"):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        node.color = default_color
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def main():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    
    plt.ion()#enable iterative
    print("DFS")
    dfs_traversal(root)
    plt.pause(1) 

    reset_tree_colors(root)
    draw_tree(root)
    plt.pause(1)

    print("BFS")
    bfs_traversal(root)
    plt.pause(1)
    
    plt.ioff()#disable iterative
    plt.show()

if __name__ == "__main__":
    main()