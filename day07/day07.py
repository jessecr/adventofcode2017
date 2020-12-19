"""
http://adventofcode.com/2017/day/6
"""

from collections import defaultdict

class TreeNode(object):
    def __init__(self, name, weight=None, parent=None):
        self.name = name
        self.weight = weight
        self.total_weight = None
        self.parent = parent
        self.children = []
        if parent is not None:
            parent.add_child(self)

    def add_child(self, node):
        """ Adds a Node as a child of this Node """
        self.children.append(node)
        node.parent = self

    def add_children(self, nodes):
        """ Adds Nodes as children of this Node """
        self.children.extend(nodes)
        for node in nodes:
            node.parent = self

    def get_root(self):
        """ Returns the root node """
        node = self
        while node.parent:
            node = node.parent

        return node

    def get_leaves(self):
        """ Returns all leaf nodes """
        to_visit = [self]
        leaves = []
        while to_visit:
            node = to_visit.pop()
            if node.children:
                to_visit.extend(node.children)
            else:
                leaves.append(node)

        return leaves

    def get_total_weight(self):
        """ Computes the weight of this node plus the weight of all its
        descendents
        """
        children = [child.get_total_weight() for child in self.children]
        return self.weight + sum(children)

    def __str__(self):
        return self.name

    def __repr__(self):
        cls = self.__class__
        return '{}({}, {}, {})'.format(cls, self.name, self.weight, self.parent)

def parse_text(text):
    return [line.strip() for line in text.splitlines()]


def build_tree(text):
    lines = parse_text(text)
    name_to_node = {}
    for line in lines:
        pieces = line.split(' -> ')
        name, weight = pieces[0].split()
        weight = int(weight.strip('(').strip(')'))
        try:
            node = name_to_node[name]
            node.weight = weight
        except KeyError:
            node = TreeNode(name, weight)
            name_to_node[node.name] = node

        # Add/create children
        if len(pieces) == 2:
            children = [name.strip() for name in pieces[1].split(',')]
            for child in children:
                if child not in name_to_node:
                    # Create the node now
                    child_node = TreeNode(child, parent=node)
                    name_to_node[child] = child_node
                else:
                    node.add_child(name_to_node[child])

    root = name_to_node.itervalues().next().get_root()

    return root

def main(text):
    root = build_tree(text)

    return root.name

def part2(text):
    root = build_tree(text)

    node = root
    while True:
        weights = {}
        for child in node.children:
            weights.setdefault(child.get_total_weight(), []).append(child)
        if len(weights) > 1:
            bad, good = sorted(weights.items(), key=lambda x: len(x[1]))
            if len(set(child.get_total_weight() for child in bad[1][0].children)) == 1:
                return bad[1][0].weight - (bad[0] - good[0])
            node = bad[1][0]
        else:
            raise ValueError("Everything looks good")

if __name__ == '__main__':
    steps = []
    with open('input', 'r') as fp:
        text = fp.read()

    print main(text)
    print part2(text)
    text = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''

    # print main(text)
    # print part2(text)
