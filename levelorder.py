import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrder(root):
    if root is None:
        return []

    queue = collections.deque([root])
    res = []

    while queue:
        size = len(queue)
        tmp = []

        while size > 0:
            node = queue.popleft()
            tmp.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            size -= 1
        res.append(tmp)

    return res


a = Node(3)
b = Node(9)
c = Node(20)
d = Node(15)
e = Node(7)

a.left = b
a.right = c
c.left = d
c.right = e

print(levelOrder(a))


!!



import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrder(root):
    if root is None:
        return []

    queue = collections.deque([root])
    res = []

    while queue:
        size = len(queue)
        tmp = []

        for i in range(size):
            node = queue.popleft()
            tmp.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            size -= 1
        res.append(tmp)

    return res[::-1]


a = Node(3)
b = Node(9)
c = Node(20)
d = Node(15)
e = Node(7)

a.left = b
a.right = c
c.left = d
c.right = e

print(levelOrder(a))
