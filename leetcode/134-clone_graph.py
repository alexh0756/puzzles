class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adjList):

    nodes = []
    for i in range(1, len(adjList)+1):
        nodes.append(Node(i))

    for i, node in enumerate(nodes):
        for neighbour in adjList[i]:
            node.neighbors.append(nodes[neighbour-1])

    return nodes[0]


def cloneGraph(node):

    all_nodes = [node]
    for n in all_nodes:
        for neigh in n.neighbors:
            if neigh not in all_nodes:
                all_nodes.append(neigh)

    # print([hex(id(n)) for n in all_nodes])
    adjList = {n.val:[a.val for a in n.neighbors] for n in all_nodes}
    adjList = [adjList[k] for k in sorted(adjList.keys())]
    nodes = []
    for i in range(1, len(adjList)+1):
        nodes.append(Node(i))

    for i, node in enumerate(nodes):
        for neighbour in adjList[i]:
            node.neighbors.append(nodes[neighbour-1])

    return nodes[0]


adjList = [[2,4],[1,3],[2,4],[1,3]]
node = build_graph(adjList)
cloneGraph(node)