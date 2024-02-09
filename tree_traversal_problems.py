"""
- Preorder
  Root -> left ->right

- Inorder
  left ->root->right

- Postorder
  left ->right ->root

- Diagonal Traversal
  we need to print all diagonal elements in a binary tree belonging to the same line.

- Level order traversal

- Vertical Order Traversal

- Zig Zag Traversal (leetcode - level order zig zag) - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
from collections import defaultdict


class Node:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

def pre_order_recursive(root, pre_order_data):
    if not root:
        return
    pre_order_data.append(root.val)
    pre_order_recursive(root.left, pre_order_data)
    pre_order_recursive(root.right, pre_order_data)

def pre_order_iterative(root):
    if not root:
        return []

    stack = [root]
    pre_order_data_iterative = []
    while stack:
        _node = stack.pop()
        if _node.left:
            stack.append(_node.left)
        pre_order_data_iterative.append(_node.val)
        if _node.right:
            stack.append(_node.right)

    return pre_order_data

def in_order_recursive(root, in_order_data):
    if not root:
        return

    in_order_recursive(root.left, in_order_data)
    in_order_data.append(root.val)
    in_order_recursive(root.right, in_order_data)

def in_order_iterative(root):
    if not root:
        return []

    stack = []
    in_order_data_iterative = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        _node = stack.pop()
        in_order_data_iterative.append(_node.val)
        root = _node.right

    return in_order_data_iterative

def post_order_recursive(root, post_order_data):
    if not root:
        return

    post_order_recursive(root.left, post_order_data)
    post_order_recursive(root.right, post_order_data)
    post_order_data.append(root.val)

def post_order_iterative(root):
    if not root:
        return []

    stack = [root]
    post_order_data_iterative = []
    while stack:
        _node = stack.pop()
        post_order_data_iterative.append(_node.val)
        if _node.left:
            stack.append(_node.left)
        if _node.right:
            stack.append(_node.right)
    # meaning first put root, then dump all right node values, then left node values [root, right, left] -> the reverse it
    # to get [left, right, node] -> post order
    return post_order_data_iterative[::-1]


def diagonal_order_traversal(root, diagonal, diagonal_node_val_map):
    if not root:
        return
    diagonal_node_val_map[diagonal].append(root.val)

    diagonal_order_traversal(root.left, diagonal+1, diagonal_node_val_map)
    diagonal_order_traversal(root.right, diagonal, diagonal_node_val_map)


def level_order_traversal(root):
    if not root:
        return []
    level_order_data = []

    queue = [root]
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            p = queue.pop(0)
            level_order_data.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)

    return level_order_data

def vertical_order_traversal(root, vertical, vertical_node_val_map):
    if not root:
        return
    vertical_node_val_map[vertical].append(root.val)

    vertical_order_traversal(root.left, vertical-1, vertical_node_val_map)
    vertical_order_traversal(root.right, vertical+1, vertical_node_val_map)

# will return level wise
def vertical_order_traversal_iterative(root):
    if not root:
        return []
    vertical_node_val_map_iterative = defaultdict(list)
    vertical_order_values_iterative = []
    queue = [(root, 0)]

    while queue:
        queue_size = len(queue)

        for i in range(queue_size):
            q, vertical = queue.pop(0)
            vertical_node_val_map_iterative[vertical].append(q.val)
            if q.left:
                queue.append((q.left, vertical-1))
            if q.right:
                queue.append((q.right, vertical+1))

    print(vertical_node_val_map_iterative)
    for q, _values in vertical_node_val_map_iterative.items():
        vertical_order_values_iterative.extend(_values)

    return vertical_order_values_iterative


def zig_zag_traversal(root):
    if not root:
        return []
    queue = [root]
    zig_zag_values = []
    level = 0
    while queue:
        level_values = []
        queue_size = len(queue)

        for i in range(queue_size):
            q = queue.pop(0)
            level_values.append(q.val)
            if q.left:
                queue.append(q.left)
            if q.right:
                queue.append(q.right)

        if level % 2 == 0:  # if even level, left to right
            zig_zag_values.append(level_values)
        else:
            zig_zag_values.append(level_values[::-1])
        level += 1

    return zig_zag_values



if __name__ == "__main__":
    # ****************** PRE-ORDER VIEW *********************** #
    pre_order_data = []
    root = Node(5)
    root.left = Node(8)
    root.right = Node(10)
    root.left.left = Node(13)
    root.left.right = Node(23)
    root.right.left = Node(25)
    root.right.right = Node(30)
    root.left.left.left = Node(32)
    root.left.left.right = Node(40)
    root.left.right.left = Node(50)

    pre_order_recursive(root, pre_order_data)
    print("PreOrder traversal using Recursion")
    print(pre_order_data)

    print("PreOrder traversal using Iteration")
    print(pre_order_iterative(root))

    # ****************** IN-ORDER VIEW *********************** #
    in_order_data = []
    print("InOrder traversal using Recursion")
    in_order_recursive(root, in_order_data)
    print(in_order_data)

    print("InOrder traversal using Iteration")
    print(in_order_iterative(root))

    # ****************** POST-ORDER VIEW *********************** #
    post_order_data = []
    print("InOrder traversal using Recursion")
    post_order_recursive(root, post_order_data)
    print(post_order_data)

    print("InOrder traversal using Iteration")
    print(post_order_iterative(root))

    # ****************** DIAGONAL Traversal *********************** #
    root_diagonal = 0
    diagonal_node_val_map = defaultdict(list)
    diagonal_order_traversal(root, root_diagonal, diagonal_node_val_map)
    diagonal_order_values = []
    for d, values in diagonal_node_val_map.items():
        diagonal_order_values.extend(values)
    print("Diagonal Order Traversal using Recursion")
    print(diagonal_order_values)

    # ****************** LEVEL ORDER Traversal *********************** #
    print("Level Order Traversal using BFS")
    print(level_order_traversal(root))
    print(level_order_traversal(root3))

    # ****************** VERTICAL Traversal *********************** #
    root_vertical = 0
    vertical_node_val_map = defaultdict(list)
    vertical_order_traversal(root, root_vertical, vertical_node_val_map)
    vertical_order_values = []
    print(vertical_node_val_map)
    for d, values in vertical_node_val_map.items():
        vertical_order_values.extend(values)
    print("Vertical Order Traversal using Recursion")
    print(vertical_order_values)

    print("Vertical Order Traversal using Iteration")
    print(vertical_order_traversal_iterative(root))

    # ****************** ZIG-ZAG Traversal *********************** #
    print("Zig-Zag Order Traversal using Iteration")
    print(zig_zag_traversal(root))
