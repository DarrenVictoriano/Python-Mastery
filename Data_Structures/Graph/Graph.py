class Graph:
    def __init__(self):
        self.graph_dict = dict()

    def add_edge(self, node, neighbors):
        if node not in self.graph_dict:
            self.graph_dict[node] = list(neighbors)
        else:
            self.graph_dict[node].append(neighbors)
