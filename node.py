class Node:

    def __init__(self, label):
        self.label = label

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.node.label == other.label
        else:
            return NotImplemented

    def __str__(self):
        return "{0}".format(self.label)