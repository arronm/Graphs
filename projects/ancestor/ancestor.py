from util import Stack


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
    
    def get_member(self, member):
        return self.family[member]


def earliest_ancestor(ancestors, starting_node):
    tree = AncestorTree()

    for relation in ancestors:
        tree.add_member(relation[0])
        tree.add_member(relation[1])
        tree.add_relation(relation)

    stack = Stack()
    stack.push(starting_node)
    visited = {}
    visited[starting_node] = 0
    furthest = starting_node

    while stack.size() > 0:
        member = stack.pop()

        for relation in tree.get_member(member):
            if relation in visited:
                continue

            visited[relation] = visited[member] + 1
            stack.push(relation)

        if visited[member] >= visited[furthest]:
            if visited[member] == visited[furthest] and member > furthest:
                continue

            furthest = member

    if furthest == starting_node:
        return -1

    return furthest


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (11, 8), (8, 9), (4, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 7))
