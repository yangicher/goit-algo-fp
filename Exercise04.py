import uuid
import networkx as nx
import matplotlib.pyplot as plt

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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [data['color'] for node_id, data in tree.nodes(data=True)]
    labels = {node_id: data['label'] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap, index=0):
    if index < len(heap):
        node = Node(heap[index])
        node.left = build_heap_tree(heap, 2 * index + 1)
        node.right = build_heap_tree(heap, 2 * index + 2)
        return node
    return None

def draw_heap(heap):
    root = build_heap_tree(heap)
    draw_tree(root)

def main():
    heap = [0, 4, 5, 10, 1, 3]
    draw_heap(heap)

if __name__ == "__main__":
    main()