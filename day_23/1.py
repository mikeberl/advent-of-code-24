# Find all the sets of three inter-connected computers. How many contain at least one computer with a name that starts with t?
# List of connections of computer is given in the input

from collections import defaultdict

def read_graph(file_path):
    graph = defaultdict(set)

    with open(file_path, 'r') as file:
        for line in file:
            node1, node2 = line.strip().split('-')
            graph[node1].add(node2)
            graph[node2].add(node1)

    return graph

def find_triangles(graph):
    triangles = set()

    for node in graph:
        for neighbor in graph[node]:
            common_neighbors = graph[node].intersection(graph[neighbor])
            for common in common_neighbors:
                triangle = tuple(sorted([node, neighbor, common]))
                triangles.add(triangle)

    return triangles

def main():
    file_path = 'input.txt'

    graph = read_graph(file_path)
    triangles = find_triangles(graph)

    count = 0
    print("Triangles found:")
    for triangle in triangles:
        t = False
        for computer in triangle:
            if computer[0] == 't':
                t = True
                count += 1
                break
        if t:
            print(triangle)
    print("Result: ", count)

if __name__ == "__main__":
    main()
