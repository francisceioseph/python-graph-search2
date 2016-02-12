from node import Node


class Graph:
    def __init__(self, max_size):
        self.max_size = max_size
        self.nodes = []
        self.adjacency_matrix = []

        for idx in range(max_size):
            line = [0] * max_size
            self.adjacency_matrix.append(line)

    def find_index_for_label(self, label):
        index = -1

        for idx, node in enumerate(self.nodes):
            if node.label == label:
                index = idx

        return index

    def add_node_with_label(self, label):

        if len(self.nodes) <= self.max_size:
            node = Node(label)
            self.nodes.append(node)
        else:
            print 'Graph max size reached'

    def add_arc_with_labels(self, label_from, label_to):
        index_from = self.find_index_for_label(label_from)
        index_to = self.find_index_for_label(label_to)

        if index_from != -1 and index_to != -1:
            self.adjacency_matrix[index_from][index_to] = 1
            #self.adjacency_matrix[index_to][index_from] = 1
        else:
            print "{0} or {1} not found in the graph".format(label_from, label_to)

    def __connected_to(self, label):
        connexions = []

        node_idx = self.find_index_for_label(label)

        if node_idx != -1:
            for idx, node in enumerate(self.nodes):
                if self.adjacency_matrix[node_idx][idx] == 1:
                    connexions.append(node.label)

        return connexions

    def connexions(self):
        connexions = []

        for i in range(len(self.nodes)):
            label_from = self.nodes[i].label
            
            for j in range(len(self.nodes)):
                label_to = self.nodes[j].label
                if (self.adjacency_matrix[i][j] == 1):
                    connexions.append((label_from, label_to))

        return connexions

    def depth_search(self, label):
        visited = []
        frontier = [self.nodes[0].label]

        while True:
            if not frontier:
                return None

            node_label = frontier.pop()

            if node_label == label:
                return node_label

            if node_label not in visited:
                visited.append(node_label)

                for l in self.__connected_to(node_label):
                    frontier.append(l)

    def breadth_search(self, label):
        visited = []
        frontier = [self.nodes[0].label]

        while True:
            if not frontier:
                return None

            node_label = frontier.pop(0)

            if node_label == label:
                return node_label

            if node_label not in visited:
                visited.append(node_label)

                for l in self.__connected_to(node_label):
                    frontier.append(l)