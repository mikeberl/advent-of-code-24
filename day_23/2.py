# Find the largest LAN in the list of computer (set of computers where ALL computers have connections to each other)
from collections import defaultdict

def read_graph(file_path):
    graph = defaultdict(set)

    with open(file_path, 'r') as file:
        for line in file:
            node1, node2 = line.strip().split('-')
            graph[node1].add(node2)
            graph[node2].add(node1)

    return graph

def find_largest_clique(graph):
    def is_clique(subset):
        for node in subset:
            if not all(neighbor in graph[node] for neighbor in subset if neighbor != node):
                return False
        return True

    def find_clique_recursive(nodes, current_clique):
        if not nodes:
            return current_clique

        largest_clique = current_clique

        for i, node in enumerate(nodes):
            new_clique = current_clique + [node]
            if is_clique(new_clique):
                clique = find_clique_recursive(nodes[i + 1:], new_clique)
                if len(clique) > len(largest_clique):
                    largest_clique = clique

        return largest_clique

    nodes = list(graph.keys())
    return find_clique_recursive(nodes, [])

def main():
    file_path = 'input.txt'

    graph = read_graph(file_path)
    largest_clique = find_largest_clique(graph)
    largest_clique.sort()

    print("Largest clique found:")
    print(",".join(largest_clique))

if __name__ == "__main__":
    main()
