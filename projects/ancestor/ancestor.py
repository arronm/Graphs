# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
def earliest_ancestor(ancestors, starting_node):
    # For each Tuple in ancestors, create a node and a directed edge
    # Tuple(1) -> Tuple(0)
    # Perform a DFT from this node
    # At the end of each path (no further nodes)
    # if this path is longer than the current longest, replace longest
    pass