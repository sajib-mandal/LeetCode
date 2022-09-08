# recursive   


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

print(count_nodes(a))



# better divide the problem and using recursion


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0

    def lheight(node):
        if node is None:
            return 0
        return 1 + lheight(node.left)

    def rheight(node):
        if node is None:
            return 0
        return 1 + rheight(node.right)

    l, r = lheight(root), rheight(root)

    if l > r:
        return 1 + count_nodes(root.left) + count_nodes(root.right)
    else:
        return (2 ** l) - 1


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

print(count_nodes(a))
