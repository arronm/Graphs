from util import Stack
# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

class AncestorTree:
    def __init__(self):
        self.family = {}
    
    def add_member(self, member):
        '''
            Takes a family member and adds it to the tree
        '''
        if member in self.family:
            return
        self.family[member] = set()

    def add_relation(self, relation):
        '''
            Takes a (Parent, Child) relationship Tuple
            and adds their connection to the tree
        '''
        parent = relation[0]
        child = relation[1]
        if not (child in self.family and parent in self.family):
            raise KeyError("Child or parent are missing in family, cannot connect")
        self.family[child].add(parent)

def earliest_ancestor(ancestors, starting_node):
    # For each Tuple in ancestors, create a node and a directed edge
    # Tuple(1) -> Tuple(0)
    # For (1, 3)
    # create node(1), create node(3)
    # create edge(3, 1)
    tree = AncestorTree()
    for relation in ancestors:
        tree.add_member(relation[0])
        tree.add_member(relation[1])
        tree.add_relation(relation)
    print(tree.family)
    # Perform a DFT from starting node
    stack = Stack()
    # At the end of each path (no further nodes)
    # if this node distance >= furthest
    #   if node distance == furthest and node > furthest:
    #       continue
    #   replace furthest

    '''
            6   7   9
           / \ /   /
          3   5   8
         / \   \ / \
        1   2   4   11
         \
          10
    '''
    # pass


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(test_ancestors, 6)
